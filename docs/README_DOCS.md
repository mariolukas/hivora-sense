# Documentation Workflow

Diese Dokumentation basiert auf Sphinx mit deutscher Quellsprache und englischer Übersetzung via gettext.

## Lokaler HTML-Build

```bash
cd docs
make html
```

Das Ergebnis liegt unter:

- `_build/html/index.html`

## Übersetzungsdateien aktualisieren

```bash
cd docs
make gettext
sphinx-intl update -p _build/gettext -l en
```

Hinweise:

- Die Locale-Struktur liegt unter `docs/locale/`.
- `-l en` aktualisiert bzw. erzeugt englische `.po`-Dateien.
