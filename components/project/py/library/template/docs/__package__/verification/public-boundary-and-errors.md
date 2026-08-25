---
name: public-boundary-and-errors-verification
doc_type: verification
description: High-level walkthrough of the public boundary guarantees proved by tests and checks. Use when you need the technical verification story for package-boundary behavior.
---

# Public Boundary And Errors

## Overview

The baseline verifies the supported top-level package boundary, config lifecycle, public errors, and import direction without turning those technical checks into a separate behavioral documentation system.

## Proof Areas

## 1. Proof: Public Config Boundary Stays Usable

This proof area shows that public names resolve through the supported package entrypoint and config installation/readback works without private imports.

### Seen In Tests

[test_public_package.py](../../../tests/[[[ package_name ]]]/unit/test_public_package.py) proves the expected top-level exports, public error type, and version metadata.

[test_config_lifecycle.py](../../../tests/[[[ package_name ]]]/integration/test_config_lifecycle.py) proves invalid installs are rejected, installed snapshots become active, and explicit snapshots remain readable through the public API.

Would fail if:

- top-level exports drifted away from the supported caller surface
- config install/read helpers stopped working through public imports
- the public exception or distribution metadata disappeared

## 2. Proof: Import Direction Keeps Internals Private

This proof area shows that public, private, support, example, test, and workbench code keep the intended dependency direction.

### Seen In Checks

`uv run lint-imports --config pyproject.toml` proves the declared package-boundary contracts.

`uv run pytest tests/[[[ package_name ]]]/unit tests/[[[ package_name ]]]/integration -q --no-cov` exercises the baseline public and collaborative package behavior.

`uv run pytest tests/test_examples.py -q --no-cov` checks committed caller-facing examples structurally with external network access blocked.

Would fail if:

- examples imported private modules
- public facades crossed unapproved import boundaries
- technical tests started depending on the wrong package layer
