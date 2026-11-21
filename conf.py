import json
import posixpath
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
project = "BoundaryKit"
extensions = ["myst_parser", "sphinx.ext.autodoc", "sphinx_copybutton", "sphinx_reredirects"]
exclude_patterns = ["_build", ".venv", "README.md"]
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_favicon = "_static/assets/favicon.svg"
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "assets/logo/logo-wide-wordmark.svg",
    "dark_logo": "assets/logo/logo-wide-wordmark-dark.svg",
}
redirects = {
    item["source"].strip("/"): posixpath.relpath(
        item["destination"].strip("/") + ".html",
        posixpath.dirname(item["source"].strip("/")),
    )
    for item in json.loads((ROOT / "redirects.json").read_text())
}

templates_path = ["_templates"]
myst_enable_extensions = ["dollarmath"]
myst_heading_anchors = 3
html_theme_options.update({"light_css_variables":{"color-brand-primary":"#1D4ED8","color-brand-content":"#1D4ED8"},"dark_css_variables":{"color-background-primary":"#090D16","color-brand-content":"#38BDF8","color-brand-primary":"#F59E0B"},"announcement":"BoundaryKit v2 · Policy evaluation and audit reference"})

html_additional_pages = {"404": "missing.html"}
