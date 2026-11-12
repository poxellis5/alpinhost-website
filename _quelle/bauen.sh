#!/bin/bash
# Baut alpinhost.ch aus den Quellen in _quelle/ und legt das Ergebnis ins Repo-Wurzelverzeichnis.
# Aufruf aus dem Repo:  bash _quelle/bauen.sh
# Danach pruefen (Ausgabe lesen), dann: git add -A && git commit && git push origin main
set -euo pipefail
cd "$(dirname "$0")"
python3 -c "import bs4" 2>/dev/null || pip install -q --break-system-packages beautifulsoup4
rm -rf site && mkdir -p site
ln -s ../../img site/img            # Bilder liegen im Repo unter /img
python3 build.py
python3 i18n_build.py               # muss "missing 0" melden
rm site/img                         # nur der Verweis, nicht die Bilder
cp -a site/. ../                    # Ergebnis ins Wurzelverzeichnis
ln -s ../../img site/img
echo "--- Pruefung (erlaubt sind nur die 3 bekannten Meldungen: Google-Datei ohne Titel/h1, '20 %' im Zweitwohnungstext)"
python3 tools/audit.py ..
rm -rf site
