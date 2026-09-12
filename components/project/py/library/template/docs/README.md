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

Traceability and assurance views need the same retained evidence produced by the
required CI run. Generate JUnit, Allure results, and coverage.py test contexts from
one hermetic pytest execution, then pass those standard artifacts to DocOps:

```bash
mkdir -p test-results/allure-results
COVERAGE_FILE=test-results/.coverage uv run pytest -c pyproject.toml -n 2 \
    --record-mode=none \
    --block-network \
    --allowed-hosts='localhost,127\\.0\\.0\\.1' \
    --cov-context=test \
    --junitxml=test-results/pytest-junit.xml \
    --alluredir=test-results/allure-results
COVERAGE_FILE=test-results/.coverage uv run coverage json \
    --show-contexts \
    -o test-results/coverage.json
uv run ternforge-docops build portal \
    --junit test-results/pytest-junit.xml \
    --allure-results test-results/allure-results \
    --coverage test-results/coverage.json
```

When the platform libraries required by WeasyPrint are available, build the release
PDF from the same retained documentation and test evidence with:

```bash
uv run ternforge-docops build dossier \
    --junit test-results/pytest-junit.xml \
    --allure-results test-results/allure-results \
    --coverage test-results/coverage.json
```

Live publication is orchestrated by the shared Ternforge docs workflow on its configured
trusted runner. It checks out the exact release and asks DocOps to build the full portal
with live Sphinx-Gallery examples plus the retained Allure perspectives; deterministic
local and required-CI DocOps builds keep live examples disabled.

Required CI passes the same JUnit evidence artifact to DocOps before publication. Open
`docs/_build/html/index.html` in a browser to inspect a local generated site.
