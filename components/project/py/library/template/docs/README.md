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
- `traceability` is a DocOps-owned generated view over the project engineering graph.

## Build

Traceability builds need current pytest evidence. Generate JUnit with the same
hermetic contract as required CI, then pass that standard artifact directly to
Ternforge DocOps:

```bash
uv run pytest -c pyproject.toml -n 2 \
    --record-mode=none \
    --block-network \
    --allowed-hosts='localhost,127\\.0\\.0\\.1' \
    --cov-context=test \
    --junitxml=test-results/pytest-junit.xml
uv run ternforge-docops build html --junit test-results/pytest-junit.xml
```

When the platform libraries required by WeasyPrint are available, build the release
PDF from the same retained documentation and test evidence with:

```bash
uv run ternforge-docops build dossier --junit test-results/pytest-junit.xml
```

Live Sphinx-Gallery publication is owned by the shared Ternforge docs workflow and its
configured trusted runner. It checks out the exact release and executes live examples
there; the deterministic DocOps build never contacts providers.

Required CI passes the same JUnit evidence artifact to DocOps before publication. Open
`docs/_build/html/index.html` in a browser to inspect a local generated site.
