# ternforge-template-components

Released reusable source components for Ternforge Copier templates.

Components are organized by responsibility and contain only `template/` files
or reusable Jinja `includes/`. A final template owns every output path and
selects released component files explicitly through Vendir.

Current released components cover the reusable responsibilities used by the
complete Python-library product:

- `components/agents/base` and `components/agents/py-library`
- `components/repository/base` and `components/repository/copier`
- `components/project/py/base` and `components/project/py/library`
- `components/quality/py`
- `components/delivery/ci/py-library`
- `components/delivery/docs/py-library`
- `components/delivery/release/library`
- `components/delivery/updates`

This repository is not a final template, registry, assembler, package manager,
runtime dependency, or fleet-management system.

