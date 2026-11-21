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
    "light_logo": "assets/logo/logo-light.svg",
    "dark_logo": "assets/logo/logo-dark.svg",
}
redirects = {
    item["source"].strip("/"): posixpath.relpath(
        item["destination"].strip("/") + ".html",
        posixpath.dirname(item["source"].strip("/")),
    )
    for item in json.loads((ROOT / "redirects.json").read_text())
}
