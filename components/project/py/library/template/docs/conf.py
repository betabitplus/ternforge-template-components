"""Sphinx configuration for [[[ project_name ]]] documentation."""

from __future__ import annotations

import os

project = "[[[ project_name ]]]"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_gallery.gen_gallery",
    "sphinxcontrib.mermaid",
]

root_doc = "index"
exclude_patterns = ["_build", "README.md"]
myst_fence_as_directive = {"mermaid"}
html_theme = "pydata_sphinx_theme"

# Required CI stays offline; live docs explicitly opt into external inventories.
intersphinx_mapping = {}
if os.getenv("SPHINX_ENABLE_INTERSPHINX") == "1":
    intersphinx_mapping = {
        "python": ("https://docs.python.org/3/", None),
    }

sphinx_gallery_conf = {
    "examples_dirs": "../examples/[[[ package_name ]]]",
    "gallery_dirs": "auto_examples",
    "filename_pattern": r".*\.py$",
    "backreferences_dir": "generated/backreferences",
    "doc_module": ("[[[ package_name ]]]",),
    "reference_url": {"[[[ package_name ]]]": None},
    "junit": "../test-results/sphinx-gallery/junit.xml",
    "remove_config_comments": True,
}
