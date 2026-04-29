from datetime import datetime

project = "Hivora Sense"
author = "Hivora Sense Team"
copyright = f"{datetime.now().year}, {author}"

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "de"
locale_dirs = ["../locale/"]
gettext_compact = False

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
