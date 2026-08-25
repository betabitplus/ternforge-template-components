# Tests Layout

The `tests/` tree contains technical verification. Human-readable product behavior belongs in executable specifications under `features/` when the project has Living Specifications.

## Reusable Support

`py_lib_testkit` exposes reusable testing infrastructure from its supported public root. Project-specific builders, assertions, fixtures, and media helpers belong in `tests/[[[ package_name ]]]/support/` when more than one test needs them.

Root `tests/conftest.py` should stay reusable and free of product imports. Product-wide fixtures live in `tests/<package>/conftest.py`.

## Test Layers

- `test_examples.py` checks that caller-facing examples import with network access blocked.
- `unit/` checks focused public and private seams.
- `integration/` checks collaboration across package components and controlled local boundaries.
- `property_based/public_contract/` checks public invariants.
- `property_based/internal/` checks private implementation invariants.
- `e2e/` is optional and reserved for genuine broad-stack or deployed-system verification when that execution depth adds value.

Unit/integration/e2e describe execution depth. Living Specifications describe the role of a behavioral contract; they are a separate axis and may execute through different technical boundaries.

For external HTTP verification, use deterministic replay in automation and keep live execution explicit. Do not create a parallel manual-demo implementation of the same behavior.
