# Minimal Sphinx Makefile

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

# Sprachen fuer den mehrsprachigen Build: DE (Quelle, Wurzel) + Uebersetzungen.
LANGUAGES     = en

# Live-Preview: Standard Deutsch, andere Sprache via ``make live L=en``.
SPHINXAUTOBUILD ?= sphinx-autobuild
# Port 8000 ist im Dev-Stack vom hivora-backend belegt -> 8100 als Default.
LIVEHOST      ?= 127.0.0.1
LIVEPORT      ?= 8100

.PHONY: help Makefile html gettext html-all update-po live clean

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

html:
	@$(SPHINXBUILD) -a -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

gettext:
	@$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/gettext" $(SPHINXOPTS)

# .po-Kataloge aus den Quelltexten aktualisieren.
update-po: gettext
	sphinx-intl update -p "$(BUILDDIR)/gettext" $(foreach L,$(LANGUAGES),-l $(L))

# Mehrsprachiger Build: DE nach _build/html, jede weitere Sprache nach _build/html/<code>.
html-all:
	@$(SPHINXBUILD) -a -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)
	@for lang in $(LANGUAGES); do \
		echo "Building language: $$lang"; \
		$(SPHINXBUILD) -a -b html -D language=$$lang "$(SOURCEDIR)" "$(BUILDDIR)/html/$$lang" $(SPHINXOPTS); \
	done

# Live-Vorschau mit automatischem Rebuild + Browser-Reload.
# Standard: Deutsch. Andere Sprache: ``make live L=en`` (benoetigt uebersetzte .po).
# DOCS_BASE_PATH="" -> Umschalter-Links wurzelrelativ statt /hivora-sense/.
live:
	DOCS_BASE_PATH="" $(SPHINXAUTOBUILD) \
		-a \
		$(if $(L),-D language=$(L)) \
		--host $(LIVEHOST) --port $(LIVEPORT) --open-browser \
		--watch "locale" \
		--ignore "*/_build/*" \
		"$(SOURCEDIR)" "$(BUILDDIR)/live" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"
