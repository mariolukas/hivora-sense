# hivora-sense

Hivora Sense: AI Edge Monitoring for Asian Hornet Wick Traps

## Dokumentation lokal bauen

Wenn `sphinx-build` fehlt (`command not found`), nutze eine virtuelle Umgebung:

```bash
cd /Users/mariolukas/workspace/beeguard/hivora-sense
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r docs/requirements.txt
cd docs
make html
```

Danach findest du die gebaute Doku unter:

- `docs/_build/html/index.html`
