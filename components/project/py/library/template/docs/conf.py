"""Sphinx configuration for [[[ project_name ]]] documentation."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

project = "[[[ project_name ]]]"
extensions = ["ternforge_docops._api.sphinx_python"]
root_doc = "index"
exclude_patterns = ["_build", "README.md"]

_docs_root = Path(__file__).resolve().parent
_repo_root = _docs_root.parent
with (_repo_root / "pyproject.toml").open("rb") as _pyproject_file:
    release = tomllib.load(_pyproject_file)["project"]["version"]

_source_ref = f"v{release}"
_source_base = "https://github.com/[[[ github_owner ]]]/[[[ repository_name ]]]/blob"
needs_render_context = {
    "source_base": _source_base,
    "source_ref": _source_ref,
}
# Generic source-link mappings and JUnit ingestion are owned by DocOps.

# Required CI stays offline; live docs explicitly opt into external inventories.
intersphinx_mapping = {}
if os.getenv("SPHINX_ENABLE_INTERSPHINX") == "1":
    intersphinx_mapping = {
        "python": ("https://docs.python.org/3/", None),
    }
