Problembehebung
===============

Dieser Abschnitt fasst häufige Probleme und Lösungsansätze rund um Aufbau,
Installation und Betrieb der Hivora-Sense-Station zusammen.

Erste Beobachtungen prüfen
--------------------------

Nach der ersten Inbetriebnahme sollte regelmäßig geprüft werden:

- Sind Bilder verwertbar?
- Gibt es Fehlalarme?
- Ist der Lockstoff noch vorhanden?
- Beschlägt die Kamera?
- Bleibt die Stromversorgung stabil?
- Ist das Gehäuse dicht?
- Muss die Kamera neu ausgerichtet werden?

Erfahrungen aus dem Außeneinsatz sind besonders wertvoll. Wenn du etwas
beobachtest, teile es gerne in der Community.

Software-Installation
---------------------

- **Serieller Port nicht sichtbar**: USB-Kabel (Datenkabel, nicht nur Ladekabel)
  und Browserrechte für WebSerial prüfen.
- **Flash-Vorgang fehlgeschlagen**: Verbindung trennen, Gerät neu starten und
  den Vorgang erneut ausführen.
- **Keine Gerätedaten nach dem Flash**: Baudrate und Board-Profil im Installer
  verifizieren.
- **Browser unterstützt WebSerial nicht**: Ein aktuelles Chromium-basiertes
  Release verwenden (empfohlen: Google Chrome).
- **Mehrere Geräte in der Portauswahl**: Alle anderen USB-Geräte vom Computer
  trennen, sodass nur noch das Kameramodul übrig bleibt.

XIAO ESP32-S3 nicht mehr erreichbar (Firmware-Recovery)
-------------------------------------------------------

In seltenen Fällen kann es vorkommen, dass ein Seeed Studio XIAO ESP32-S3 Sense
nach fehlgeschlagenen Flash-Versuchen weder unter Windows noch unter macOS
zuverlässig erkannt wird. Abhilfe schafft dann eine Wiederherstellung über den
browserbasierten Meshtastic-Flasher (Community-Tipp):

1. Mit **Google Chrome** den Meshtastic-Flasher öffnen:
   https://flasher.meshtastic.org
2. Das Seeed-Studio-XIAO-ESP32-S3-Modul mit **gedrücktem BOOT-Taster**
   (sehr klein) per USB anschließen.
3. „Zielgerät auswählen“ aufrufen. Der *Seeed Studio XIAO ESP32-S3* findet sich
   ganz unten in der Abteilung „Eigenbaugeräte“.
4. Eine Firmware auswählen (z. B. die aktuell vorgeschlagene Beta) und den
   Anweisungen folgen.
5. Modul von USB trennen, nach ca. 5 Sekunden mit **gedrückter BOOT-Taste**
   wieder einschalten.
6. Anschließend über `hivora.eu <https://hivora.eu/>`_ einen neuen Locktopf
   anlegen und die Hivora-Sense-Firmware erneut installieren.

Hardware / Aufbau
-----------------

- **Gerät startet nicht**: Stromversorgung und USB-C-Kabel kontrollieren
  (Datenkabel verwenden).
- **Kein Bild / schlechte Bildqualität**: Prüfen, ob die Schutzfolie von der
  Linse entfernt wurde und die Kamera korrekt im Gehäuse und am Ständer sitzt.
- **Kamera beschlägt / Kondensation**: Auf ausreichende Belüftung und Dichtheit
  des Gehäuses achten.
- **WiFi-Verbindung instabil**: Festen Sitz der WLAN-Antenne prüfen.
- **Keine Sichtungen auf der SD-Karte**: Prüfen, ob die SD-Karte korrekt im Slot
  unter dem Kameramodul sitzt (sie ragt sichtbar heraus).

Weitere Hilfe
-------------

Lässt sich ein Problem nicht beheben, kann ein Issue im Projekt-Repository
angelegt werden: https://github.com/mariolukas/hivora-sense

Weiterer Austausch und Hilfe ist im `Hivora Community Forum
<https://hivora.discourse.group/>`_ möglich.
