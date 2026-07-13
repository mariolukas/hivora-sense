Locktöpfe verwalten
===================

Unter **Meine Locktöpfe** verwaltest du alle Hivora Sense Locktöpfe, die mit
deinem Konto verbunden sind. Die Seite zeigt eine Übersicht aller Geräte mit
Status und letztem Kontakt und bietet die Aktionen, um Locktöpfe hinzuzufügen,
anzupassen und wieder zu entfernen.

.. note::

   Die vollständige Locktopf-Verwaltung ist Teil des Plans **Community Pro**
   (*Unterstützer*). Siehe :doc:`cloud_account`.

Einen Locktopf verbinden
------------------------

Es gibt zwei Wege, einen Locktopf mit deinem Konto zu verbinden:

**Eigener, neuer Locktopf**
   Über die Schaltfläche **Locktopf hinzufügen** legst du einen neuen Locktopf
   an. Dabei wird ein einmaliges **Geräte-Secret** erzeugt.

   .. important::

      Das Geräte-Secret wird **nur ein einziges Mal** angezeigt. Bewahre es
      sicher auf – es verbindet das Gerät mit deinem Konto.

**Workshop-Locktopf übernehmen**
   Vorbereitete Locktöpfe aus Workshops übernimmst du über **Workshop-Locktopf**.
   **Geräte-ID** und **PIN** stehen auf dem Aufkleber des Geräts. Du kannst den
   **QR-Code auf dem Aufkleber scannen** oder Geräte-ID und PIN manuell eingeben.

   Bist du beim Scannen des QR-Codes noch nicht angemeldet, wirst du zunächst
   zur Anmeldung bzw. Registrierung geführt. Öffne den QR-Code danach erneut, um
   die Übernahme abzuschließen.

.. tip::

   Der Ablauf, mit dem ein frisch aufgebauter Locktopf zum ersten Mal
   eingerichtet und mit dem Konto verbunden wird, ist ausführlich unter
   :doc:`software_installation` beschrieben.

Nach dem Verbinden solltest du als Nächstes den **Standort** des Locktopfs
festlegen – er wird für das öffentliche Lagebild und für die Alarmierung über
die :doc:`HornetLog App <cloud_hornetlog>` benötigt.

Die Locktopf-Liste
------------------

Die Liste **Locktöpfe** zeigt zu jedem Gerät folgende Spalten:

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Spalte
     - Bedeutung
   * - **Geräte-ID**
     - Eindeutige Kennung des Locktopfs (SSID).
   * - **Name**
     - Frei wählbarer Name zur Wiedererkennung.
   * - **Status**
     - Aktueller Zustand des Geräts (siehe unten).
   * - **Letzter Kontakt**
     - Zeitpunkt der letzten Verbindung mit der Cloud.
   * - **Erstellt**
     - Zeitpunkt, zu dem der Locktopf angelegt wurde.

Mögliche Status-Werte:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Status
     - Bedeutung
   * - **Online**
     - Der Locktopf ist aktiv und hatte kürzlich Kontakt zur Cloud.
   * - **Offline**
     - Aktuell keine Verbindung – z. B. ausgeschaltet oder ohne Netz.
   * - **Einrichtung ausstehend**
     - Der Locktopf ist angelegt, aber noch nicht vollständig eingerichtet.
   * - **Widerrufen**
     - Das Geräte-Secret wurde ungültig gemacht; das Gerät kann keine neuen
       Erkennungen mehr übermitteln.

Software-Updates
----------------

Ist für einen Locktopf eine neuere Software verfügbar, erscheint in der Liste
der Hinweis **Update verfügbar (v…)**. Ein Tooltip zeigt die installierte und
die in der Cloud verfügbare Version. Über das Symbol **Software installieren**
lässt sich die neue Software direkt aus dem Browser auf den Locktopf übertragen.

Weitere Aktionen je Locktopf
----------------------------

Locktopf anpassen
~~~~~~~~~~~~~~~~~~

Über **Locktopf anpassen** änderst du z. B. den Namen des Geräts.

Secret rotieren
~~~~~~~~~~~~~~~

Mit **Secret rotieren** erzeugst du ein neues Geräte-Secret. Das bisherige
Secret wird dabei **sofort ungültig**; das neue Secret wird – wie beim Anlegen –
nur einmalig angezeigt. Nutze dies, wenn das alte Secret kompromittiert sein
könnte.

Hotspot-Zugangsdaten
~~~~~~~~~~~~~~~~~~~~~

Für den Fall, dass der Locktopf nicht mehr über das WLAN erreichbar ist, zeigt
die Verwaltung die **Hotspot-Zugangsdaten** an. Damit kannst du dich direkt mit
dem geräteeigenen Hotspot verbinden. Damit sich der Hotspot einschaltet, trenne
den Locktopf kurz vom Strom und stecke ihn wieder ein.

Locktopf entfernen
~~~~~~~~~~~~~~~~~~

Mit **Locktopf entfernen** löst du das Gerät aus deiner Verwaltung. Danach kann
es keine neuen Erkennungen mehr übermitteln.

.. note::

   Bereits gemeldete **öffentliche** Sichtungen dieses Locktopfs bleiben für das
   allgemeine Lagebild erhalten, auch wenn der Locktopf entfernt wird.
