"""Verify the requirements graph against imported JUnit evidence."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

from sphinx.cmd.build import build_main

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "components/project/py/library/template"
UBPROJECT = TEMPLATE / "ubproject.toml"
SCHEMAS = TEMPLATE / "docs/_traceability/schemas.json"
TRACEABILITY = TEMPLATE / "docs/traceability.rst"

INDEX = """Synthetic traceability
======================

.. goal:: Reliable routing
   :id: GOAL_ROUTING

.. feature:: Route fallback
   :id: FEAT_ROUTING
   :derives: GOAL_ROUTING

.. req:: Failed routes fall back
   :id: REQ_FALLBACK
   :revision: 1
   :needs_artifacts: impl;bdd;integration
   :derives: FEAT_ROUTING

.. test-file:: Pytest evidence
   :id: PYTEST_FILE
   :file: junit.xml
   :auto_suites:
   :auto_cases:

.. toctree::
   :hidden:

   traceability
"""


def _testcase(
    name: str, *, kind: str | None = None, verifies: str | None = None
) -> str:
    properties: list[str] = []
    if kind is not None:
        properties.append(
            f'<property name="verification_kind" value="{escape(kind)}" />'
        )
    if verifies is not None:
        properties.append(f'<property name="verifies" value="{escape(verifies)}" />')
    if kind == "bdd":
        properties.extend(
            [
                '<property name="gherkin_feature" value="features/fallback.feature" />',
                '<property name="gherkin_scenario" value="Failed route falls back" />',
            ]
        )
    properties_xml = ""
    if properties:
        properties_xml = f"<properties>{''.join(properties)}</properties>"
    return (
        f'<testcase classname="synthetic" name="{escape(name)}" time="0.001">'
        f"{properties_xml}</testcase>"
    )


def _junit(*, include_integration: bool, include_unwanted_unit: bool) -> str:
    cases = [
        _testcase("test_behavior", kind="bdd", verifies="REQ_FALLBACK"),
        _testcase("test_untraced_diagnostic"),
    ]
    if include_integration:
        cases.append(
            _testcase("test_integration", kind="integration", verifies="REQ_FALLBACK")
        )
    if include_unwanted_unit:
        cases.append(_testcase("test_unit", kind="unit", verifies="REQ_FALLBACK"))
    return (
        '<?xml version="1.0" encoding="utf-8"?>'
        f'<testsuites tests="{len(cases)}" failures="0" errors="0" skipped="0">'
        f'<testsuite name="pytest" tests="{len(cases)}" failures="0" errors="0" '
        f'skipped="0" time="0.01">{"".join(cases)}</testsuite></testsuites>'
    )


def build(
    junit: str, *, include_impl: bool = True, include_manual_impl: bool = False
) -> int:
    """Build one isolated graph with source and JUnit evidence."""
    with tempfile.TemporaryDirectory(prefix="ternforge-trace-schema-") as tmp:
        project = Path(tmp)
        docs = project / "docs"
        source = project / "src" / "synthetic.py"
        schema_dir = docs / "_traceability"
        schema_dir.mkdir(parents=True)
        source.parent.mkdir(parents=True)
        source.write_text(
            (
                "# @impl Fallback implementation, IMPL_FALLBACK, [REQ_FALLBACK]\n"
                if include_impl
                else "def fallback() -> None:\n    pass\n"
            ),
            encoding="utf-8",
        )
        shutil.copy2(UBPROJECT, project / "ubproject.toml")
        shutil.copy2(SCHEMAS, schema_dir / "schemas.json")
        shutil.copy2(TRACEABILITY, docs / "traceability.rst")
        (docs / "conf.py").write_text(
            'extensions = ["sphinx_needs", "sphinx_codelinks", "sphinxcontrib.test_reports"]\n'
            'project = "Synthetic"\n'
            'needs_from_toml = "../ubproject.toml"\n'
            'src_trace_config_from_toml = "../ubproject.toml"\n'
            'tr_extra_options = ["verification_kind", "gherkin_feature", "gherkin_scenario"]\n'
            'tr_property_link_types = {"verifies": "verifies"}\n'
            "tr_suite_id_length = 8\n"
            "tr_case_id_length = 8\n",
            encoding="utf-8",
        )
        index = INDEX
        if include_manual_impl:
            index += """

.. impl:: Handwritten fallback implementation
   :id: IMPL_MANUAL_FALLBACK
   :implements: REQ_FALLBACK
"""
        (docs / "index.rst").write_text(index, encoding="utf-8")
        (docs / "junit.xml").write_text(junit, encoding="utf-8")
        subprocess.run(["git", "init", "--quiet"], cwd=project, check=True)
        subprocess.run(
            ["git", "config", "user.name", "Ternforge trace acceptance"],
            cwd=project,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.email", "trace@ternforge.invalid"],
            cwd=project,
            check=True,
        )
        subprocess.run(
            ["git", "remote", "add", "origin", "https://github.com/example/trace.git"],
            cwd=project,
            check=True,
        )
        subprocess.run(["git", "add", "."], cwd=project, check=True)
        subprocess.run(
            ["git", "commit", "--quiet", "-m", "test: trace fixture"],
            cwd=project,
            check=True,
        )
        return build_main(["-W", "-b", "html", str(docs), str(project / "_build")])


def main() -> None:
    """Prove required and unwanted source and test evidence semantics."""
    valid = _junit(include_integration=True, include_unwanted_unit=False)
    missing_test = _junit(include_integration=False, include_unwanted_unit=False)
    unwanted_test = _junit(include_integration=True, include_unwanted_unit=True)
    if build(valid) != 0:
        raise SystemExit("valid imported traceability graph must pass")
    if build(valid, include_impl=False) == 0:
        raise SystemExit("missing requested implementation evidence must fail")
    if build(valid, include_impl=False, include_manual_impl=True) == 0:
        raise SystemExit(
            "handwritten implementation evidence without source link must fail"
        )
    if build(missing_test) == 0:
        raise SystemExit("missing requested integration evidence must fail")
    if build(unwanted_test) == 0:
        raise SystemExit("unwanted unit evidence must fail")


if __name__ == "__main__":
    main()
