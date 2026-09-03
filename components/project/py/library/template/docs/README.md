---
name: docs
doc_type: index
description: Repository documentation entry point for API reference and executable examples.
---

# Documentation

The committed documentation surface is intentionally small before project-specific
requirements and architecture are modeled explicitly.

- `api.md` defines the generated public API reference.
- `examples/[[[ package_name ]]]/` is the source of truth for runnable workflows.
- `traceability.rst` renders implementation and verification evidence from Sphinx-Needs.

## Build

Traceability builds need current pytest evidence. Generate the gitignored local JUnit
with the same hermetic contract as required CI, then let Ternforge DocOps build the
strict deterministic documentation surface:

```bash
uv run pytest -c pyproject.toml -n 2 \
    --record-mode=none \
    --block-network \
    --allowed-hosts='localhost,127\\.0\\.0\\.1' \
    --cov-context=test \
    --junitxml=docs/_traceability/local-pytest.xml
uv run ternforge-docops build html
```

When the platform libraries required by WeasyPrint are available, build the release
PDF from the same retained documentation and test evidence with:

```bash
uv run ternforge-docops build dossier
```

Live Sphinx-Gallery publication is owned by the shared Ternforge docs workflow and its
configured trusted runner. It checks out the exact release and executes live examples
there; the deterministic DocOps build never contacts providers.

Required CI imports JUnit evidence automatically before its documentation build. Open
`docs/_build/html/index.html` in a browser to inspect a local generated site.
