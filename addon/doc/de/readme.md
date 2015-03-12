# Goldwave #

* Autoren: Joseph Lee, NVDA-Entwicklergemeinde
* [stabile Version][1] herunterladen
* [Testversion][2] herunterladen

Dieses Anwendungsmodul verbessrt die Zugänglichkeit des Audio-Editors
Goldwave

## Tastenkürzel ##

* strg+Umschalt+P: gibt die aktuelle Audio-Position an.
* strg+NvDA+3: gibt eine Zusammenfassung zur Audio-Auswahl an
* strg+NVDA+2: Gibt die Gesamtlänge der Audiospur an
* strg+NVDA+1: Gibt die Audiokanäle an, die Sie momentan bearbeiten
* NvDA+Umschalt+C: Schaltet die ansage von Befehlen während der
  Audiobearbeitung ein oder aus.
* strg+NVDA+4: Gibt die aktuelle Zoom-Stufe an.

Weitere Informationen über Goldwave und seine Tastenkombinationen finden Sie
im Benutzerhandbuch von Goldwave

Bitte beachten Sie: GoldWave 6 benötigt die 64-bit-Version von Windows 7
oder neuer. NVDA 2014.1 oder neuer ist erforderlich, um Version 2 dieser
Erweiterung einzusetzen.

## Änderungen in 2.0

* Support for GoldWave 6, including 64-bit version of GoldWave (see note
  above).
* Die Hilfe zur Erweiterung ist nun über den Erweiterungs-Manager
  verfügbar. (Ab NVDA 2014.3 und neuer.)
* NVDA now announces selected channel if you press channel selection
  commands such as Control+Shift+L for the left channel.
* Various issues with numeric edit fields such as censor field and time
  selector in mix dialog has been fixed, including selecting text, updating
  values and so on.
* Command announcement setting will be remembered when switching to other
  programs.

## Änderungen in 1.2

* Fixed an issue where NVDA had difficulty announcing some edit fields.
* Neue und aktualisierte Übersetzungen.
* Please note that due to recent changes in NVDA, audio selection and other
  status commands may not work as expected in some systems.

## Änderungen in 1.1 ##

* Nachrichten werden nun in Braille ausgegeben.
* Audio selection summary is presented in languages other than English.
* More command announcements added including cue position movement and
  delete/trim operations.
* Fixed an issue in numeric edit fields such as various effects dialogs
  where nothing or wrong field name was announced.
* Neue und aktualisierte Übersetzungen.

## Änderungen in 1.0 ##

* anfängliche Version

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=gwv

[2]: http://addons.nvda-project.org/files/get.php?file=gwv-dev
