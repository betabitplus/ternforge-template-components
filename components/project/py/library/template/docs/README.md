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
- `index.md` publishes the API reference and generated Sphinx-Gallery output.

## Build

Build documentation without executing live examples:

```bash
uv run sphinx-build -W --keep-going -D plot_gallery=0 -b html docs docs/_build/html
```

Build the full live gallery with the configured environment and credentials:

```bash
uv run sphinx-build -W --keep-going -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser to inspect the generated site.
