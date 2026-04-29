Software Installation
=====================

Die Firmware-Bereitstellung erfolgt über einen browserbasierten Cloud-Installer mit **WebSerial**.

Voraussetzungen
---------------

- Unterstützter Browser (z. B. aktuelles Chromium-basiertes Release).
- USB-Datenkabel zwischen Rechner und Hivora-Sense-Gerät.
- Lokaler Zugriff auf die Installer-URL.

Schritt-für-Schritt
-------------------

1. Gerät per USB verbinden und einschalten.
2. Cloud-Installer im Browser öffnen.
3. Schaltfläche zum Verbinden über WebSerial wählen.
4. Den korrekten seriellen Port auswählen und Zugriff bestätigen.
5. Ziel-Firmware auswählen und Flash-Vorgang starten.
6. Abschlussmeldung abwarten und Gerät neu starten.
7. Nach dem Neustart Basisfunktion (Status/Erkennung) prüfen.

Fehlerbehebung (Kurz)
---------------------

- Port nicht sichtbar: USB-Kabel/Browserrechte prüfen.
- Flash fehlgeschlagen: Verbindung trennen, Gerät neu starten, erneut versuchen.
- Keine Gerätedaten nach Flash: Baudrate/Board-Profil im Installer verifizieren.
