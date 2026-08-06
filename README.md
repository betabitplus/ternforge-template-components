# ternforge-template-components

Released reusable source components for Ternforge Copier templates.

Components are organized by responsibility and contain only `template/` files
or reusable Jinja `includes/`. A final template owns every output path and
selects released component files explicitly through Vendir.

The initial release contains only the components consumed by the minimal
infrastructure repository template:

- `components/agents/base`
- `components/repository/base`
- `components/repository/copier`

This repository is not a final template, registry, assembler, package manager,
runtime dependency, or fleet-management system.

