Requirements traceability
=========================

Requirements are the engineering source of truth. Verification and implementation
evidence are linked into the same Sphinx-Needs graph.

Implementation evidence
-----------------------

Implementation markers live next to the code they justify::

   # @impl Short implementation title, IMPL_EXAMPLE, [REQ_EXAMPLE[revision==1]]

The marker creates an ``IMPL_*`` need with a source link and an ``implements``
edge to the referenced requirement revision. Requirements that request ``impl``
evidence must have at least one such incoming edge; a requirement revision bump
invalidates stale implementation links until they are reviewed and repinned.

.. src-trace::
   :project: python

Verification evidence
---------------------

Pytest evidence links to an exact requirement revision and declares its evidence
kind. A requested verification kind is satisfied only by a testcase whose result
is ``passed``; skipped and expected-failure results remain visible evidence but do
not satisfy the requirement obligation. Revision bumps invalidate stale
``verifies`` links until the verification has been reviewed and repinned.

Graph inventory
---------------

.. needtable::
   :columns: id;title;type;needs_artifacts
   :filter: type in ["goal", "feature", "req", "treq", "impl", "testcase"]
