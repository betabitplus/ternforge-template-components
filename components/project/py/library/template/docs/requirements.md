# Product requirements

The generated library starts with a deliberately small specification for the behavior
that already exists in the template. Replace or extend these contracts as the product
grows; do not keep tests or production behavior without a path back to the authored
requirements graph.

```{goal} Provide a stable Python library foundation
:id: GOAL_LIBRARY_FOUNDATION
:collapse: true

The library exposes a predictable public package, coherent configuration lifecycle,
and executable examples that remain safe to import offline.
```

```{feature} Public library foundation
:id: FEAT_LIBRARY_FOUNDATION
:collapse: true
:derives: GOAL_LIBRARY_FOUNDATION

The initial generated package provides the minimum supported behavior needed to start
product development without unowned starter code or tests.
```

```{req} Public package exports resolve
:id: REQ_PUBLIC_PACKAGE_SURFACE
:collapse: true
:status: accepted
:revision: 1
:required_evidence: impl;unit
:derives: FEAT_LIBRARY_FOUNDATION

**Statement.** Names declared as supported by the top-level package shall resolve from
that public package boundary, including public errors, configuration helpers, and
version metadata.

**Rationale.** The generated repository should begin with one explicit public boundary
rather than requiring callers to depend on private implementation modules.

**Verification intent.** Resolve the declared public exports and representative public
types directly from the top-level package.
```

```{req} Installed configuration round-trips through the public API
:id: REQ_CONFIG_LIFECYCLE
:collapse: true
:status: accepted
:revision: 1
:required_evidence: impl;unit
:derives: FEAT_LIBRARY_FOUNDATION

**Statement.** Installing a valid configuration snapshot shall make that same snapshot
observable through the public configuration API, while unsupported objects shall be
rejected at the public boundary.

**Rationale.** The starter configuration API should have deterministic semantics before
product-specific configuration fields are added.

**Verification intent.** Exercise public installation, active snapshot lookup, explicit
snapshot lookup, and invalid-object rejection.
```

```{req} Executable examples remain importable offline
:id: REQ_EXAMPLE_IMPORTABILITY
:collapse: true
:status: accepted
:revision: 1
:required_evidence: integration
:derives: FEAT_LIBRARY_FOUNDATION

**Statement.** Committed executable examples shall be importable without initiating
network access or live workflows.

**Rationale.** Documentation examples are part of the maintained product surface and
must remain safe for hermetic CI and documentation tooling to inspect.

**Verification intent.** Import every committed example while network connection
creation is blocked.
```
