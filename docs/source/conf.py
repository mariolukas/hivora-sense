import os
from datetime import datetime

project = "Hivora"
author = "Hivora Team"
copyright = f"{datetime.now().year}, {author}"

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = []

# Quellsprache; wird beim Build pro Sprache via ``-D language=<code>``
# (bzw. durch Read the Docs) überschrieben.
language = "de"
locale_dirs = ["../locale/"]
gettext_compact = False

# Sprachabhängige Bilder: Referenzen im Quelltext bleiben neutral
# (``_static/aufbauanleitung/bild.png``) und werden je Sprache aus dem
# passenden Unterordner geladen – ``.../de/bild.png`` bzw. ``.../en/bild.png``.
# Fehlt eine Sprachvariante, greift Sphinx auf die neutrale Referenz zurück.
figure_language_filename = "{path}{language}/{basename}{ext}"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["hivora-cloud-theme.css"]

# Verfügbare Sprachen für den eigenen Umschalter (GitHub Pages).
# DE liegt im Wurzelverzeichnis, weitere Sprachen im Unterordner ``<code>/``.
languages = [
    ("Deutsch", ""),
    ("English", "en"),
]

# Basispfad der GitHub-Pages-Seite (Projektseite -> "/<repo>").
# Lokal per ``DOCS_BASE_PATH=""`` überschreibbar. Auf Read the Docs wird der
# Umschalter ausgeblendet (RTD liefert ein eigenes Sprach-Flyout).
html_context = {
    "languages": languages,
    "base_path": os.environ.get("DOCS_BASE_PATH", "/hivora-sense"),
    "current_language": language,
}
