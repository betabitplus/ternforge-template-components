"""Sphinx configuration for [[[ project_name ]]] documentation."""

from __future__ import annotations

project = "[[[ project_name ]]]"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_gallery.gen_gallery",
    "sphinxcontrib.mermaid",
]

root_doc = "index"
exclude_patterns = ["_build", "README.md"]
myst_fence_as_directive = {"mermaid"}
html_theme = "pydata_sphinx_theme"

sphinx_gallery_conf = {
    "examples_dirs": "../examples/[[[ package_name ]]]",
    "gallery_dirs": "auto_examples",
    "filename_pattern": r"^(?!.*__init__\.py$).*\.py$",
    "ignore_pattern": r"__init__\.py$",
    "backreferences_dir": "generated/backreferences",
    "doc_module": ("[[[ package_name ]]]",),
    "reference_url": {"[[[ package_name ]]]": None},
    "copyfile_regex": r".*\.(?:png|jpe?g|gif|svg|pdf|mp4|webm|wav|mp3)$",
}
