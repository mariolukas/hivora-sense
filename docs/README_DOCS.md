# Documentation Workflow

Diese Dokumentation basiert auf Sphinx mit **deutscher Quellsprache** und
**englischer Übersetzung** via gettext. Deutsch ist die Quellsprache (die
`.rst`-Dateien), Englisch wird über Übersetzungskataloge (`.po`) gepflegt.

## Lokaler HTML-Build

Nur Deutsch:

```bash
cd docs
make html          # -> _build/html/index.html
```

Alle Sprachen (Deutsch im Wurzelverzeichnis, Englisch unter `en/`):

```bash
cd docs
make html-all      # -> _build/html/index.html und _build/html/en/index.html
```

## Live-Vorschau (Watcher)

Baut bei jeder Änderung automatisch neu und lädt den Browser-Tab neu:

```bash
cd docs
make live            # Deutsch, öffnet http://127.0.0.1:8000
make live L=en       # englische Vorschau (benötigt übersetzte .po)
```

Optionen: `make live LIVEPORT=9000 LIVEHOST=0.0.0.0`. Der Watcher beobachtet
`source/` **und** `locale/`, d. h. auch Übersetzungsänderungen werden live
sichtbar (in der jeweils gebauten Sprache).

## Sprachumschalter

Der Sprachumschalter in der Seitenleiste verlinkt absolut auf
`/hivora-sense/...` (GitHub-Pages-Projektpfad). Für eine lokale Vorschau ohne
diesen Präfix:

```bash
DOCS_BASE_PATH="" make html-all
```

## Übersetzungsdateien aktualisieren

Nach Änderungen an den deutschen `.rst`-Quellen die Kataloge aktualisieren:

```bash
cd docs
make update-po     # = make gettext + sphinx-intl update -l en
```

Danach in `docs/locale/en/LC_MESSAGES/*.po` die `msgstr`-Felder übersetzen und
mit `make html-all` neu bauen.

Hinweise:

- Die Locale-Struktur liegt unter `docs/locale/`.
- Weitere Sprachen: in `docs/Makefile` die Variable `LANGUAGES` erweitern
  (z. B. `LANGUAGES = en fr`).

## Deployment

- **GitHub Pages** (`.github/workflows/docs.yml`): baut via `make html-all`
  Deutsch + Englisch und deployt beide (DE unter `/`, EN unter `/en/`).
- **Read the Docs** (`.readthedocs.yaml`): Mehrsprachigkeit über getrennte
  RTD-Projekte je Sprache (Hauptprojekt Deutsch + Übersetzungsprojekt
  Englisch, im Dashboard verknüpft). RTD liefert ein eigenes Sprach-Flyout;
  der eingebaute Umschalter wird auf RTD automatisch ausgeblendet.
