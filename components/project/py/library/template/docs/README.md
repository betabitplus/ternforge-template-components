---
name: docs
doc_type: index
description: Repository documentation index. Use when you need the right docs entry point.
---

# Documentation

## Overview

These docs describe the [[[ project_title_lower ]]] architecture, dependency roles,
verification approach, API reference, and generated live-example gallery.

## Files

- [Package Docs]([[[ package_name ]]]/README.md)
  Indexes the package documentation.
  Use it to enter the package architecture, examples, dependency, and verification docs.
- [Sphinx Site Source](index.md)
  Defines the generated documentation home page and navigation.
  Build the site to inspect the live-example gallery and API reference.

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
