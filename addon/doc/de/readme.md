# GoldWave #

* Autoren: Joseph Lee und die NVDA-Entwicklergemeinde.

Diese Erweiterung verbessert die Zugänglichkeit des Audio-Editors GoldWave.

## Tastenkombinationen ##

All commands support speech on demand mode.

* Strg+Umschalt+P: Gibt die aktuelle Audio-Position an.
* NVDA+Umschalt+R: Gibt die verbleibende Zeit des gerade bearbeiteten Titels
  aus.
* Strg+NVDA+1: Gibt den Audio-Kanal an, den Sie momentan bearbeiten.
* Strg+NVDA+2: Gibt die Gesamtlänge der Audio-Spur an.
* Strg+NVDA+3: Meldet eine Zusammenfassung der Informationen zur
  Audio-Auswahl an.
* Strg+NVDA+4: Gibt die aktuelle Zoom-Stufe an.

Weitere Informationen über GoldWave und die Tastenkombinationen finden Sie
im GoldWave-Benutzerhandbuch.

Note: GoldWave 6 or later and Windows 10 or later is required.

## Version 25.04

* Removed command announcement mode, replaced with speech on demand mode. In
  speech on demand mode, GoldWave specific commands such as setting start
  marker will stay silent while informational commands such as audio
  position will be spoken.

## Version 25.02

* NVDA 2024.1 or later is required.
* Restored limited support for Windows 8.1.

## Version 25.01

* Support for GoldWave 7 (requires 64-bit Windows 10 or later).
* Download links for add-on releases are no longer included in add-on
  documentation. You can download the add-on from NV Access add-on store.
* Switched linting tool from Flake8 to Ruff and reformatted add-on modules
  to better align with NVDA coding standards.
* Removed support for automatic add-on updates feature from Add-on Updater
  add-on.

## Version 23.02

* NVDA 2022.4 oder neuer wird benötigt.
* Windows 10 Version 21H2 (November 2021 Update bzw. Build 19044) oder neuer
  wird benötigt.

## Version 23.01

* NVDA 2022.3 oder neuer wird benötigt.
* Windows 10 oder neuer ist erforderlich, da Windows 7, 8 und 8.1 ab Januar
  2023 nicht mehr von Microsoft unterstützt werden.

## Version 22.03

* NVDA 2021.3 oder neuer wird benötigt.
* Beim Versuch, die Erweiterung unter Windows 7 und 8/8.1 zu installieren,
  wird eine Warnung angezeigt.

## Version 21.10

* NVDA 2021.2 oder neuer ist auf Grund von Änderungen in NVDA erforderlich,
  die diese Erweiterung betreffen.
* In GoldWave 6.57 und neuer wiederholt NVDA den Namen der geladenen Datei
  nicht mehr, wenn die Wiedergabe-/Rücklauf-/Stopp-Tasten gedrückt werden.

## Version 21.06

* Zusätzliche Probleme mit dem Codierungsstil und potenzielle Fehler mit
  Flake8 behoben.

## Version 20.06

* Mit Flake8 wurden viele Code-Probleme und potenzielle Fehler behoben.

## Version 20.04

* Meldungen bei der Eingabehilfe für für die Tastenkombination zur Ansage
  der Restlaufzeit (NVDA+Umschalt+R) hinzugefügt.
* Der Befehl zur Ansage zum Umschalten des Befehls (NVDA+Umschalt+C) wird
  nun unter der Kategorie "GoldWave" unter "Tastenbefehle" von NVDA
  angezeigt.

## Version 20.01

* Benötigt NVDA 2019.3 oder neuer.

## Version 19.11

* Windows 7 SP1, GoldWave 6.x und NVDA 2019.1 oder höher wwird benötigt.
* Hilfemeldungen für das Sound-Fenster hinzugefügt. (Diese sind verfügbar,
  falls die Erweiterung "Hilfe zur Verwendung von Steuerelementen"
  installiert ist).

## Version 18.12

* NVDA wird nun nicht mehr einfrieren oder Fehlertöne erzeugen, wenn Sie
  bestimmte GoldWave-Befehle auslösen, während die Ansage der
  Funktionstasten deaktiviert ist. (Dies kann u. U. zu komischem verhalten
  Führen).
* Interne Änderungen zur Unterstützung zukünftiger NVDA-Versionen.

## Version 18.07

* Es wurde ein Problem behoben, bei dem führende Nullen nicht angezeigt
  wurden, wenn versucht wurde, die verbleibende Zeit für einen Track zu
  erhalten.

## Version 17.05

* Möglichkeit der Anzeige von Debug-Informationen wurde hinzugefügt, wenn
  NVDA mit aktiviertem Debug-Logging läuft (NVDA 2017.1 oder höher).
* Neue und aktualisierte Übersetzungen.

## Version 16.12

* Das Versionsschema lautet nun Jahr.Monat.

## Änderungen in 4.0

* Das Repository der Erweiterung ist nach GitHub umgezogen
  [https://github.com/josephsl/goldwave](https://github.com/josephsl/goldwave).
* Leichte Verbesserungen bei der Ansage von Statusinformationen zu Kanälen.

## Änderungen in 3.0

* Ein Befehl zur Ankündigung der verbleibenden Zeit für den aktuellen Titel
  (NVDA+Umschalt+R) wurde hinzugefügt.
* Leichte Verbesserungen bei der Ansage von Statusinformationen wie
  Senderinformationen.

## Änderungen in 2.0

* Unterstützung für Goldwave 6, einschließlich 64-Bit-Version von Goldwave
  (siehe Anmerkung oben).
* Die Hilfe zur Erweiterung ist nun über den Erweiterungs-Manager
  verfügbar. (Ab NVDA 2014.3 und neuer.)
* Wenn sie einen Befehl zur Kanalauswahl auslösen, sagt NVDA nun den
  ausgewählten Kanal an. Beispiel: STRG+Umschalt+L für den linken Kanal.
* Verbesserungen bei numerischen Eingabefeldern.
* Die Einstellungen zur Ansage von Befehlen werden gespeichert, wenn sich
  der Fokus außerhalb von Goldwave befindet.

## Änderungen in 1.2

* Fehler mit einigen Eingabefeldern behoben.
* Neue und aktualisierte Übersetzungen.
* Bitte beachten Sie, dass aufgrund der jüngsten Änderungen in NVDA in
  einigen Systemen die Audio-Auswahl und andere Statusbefehle möglicherweise
  nicht wie erwartet funktionieren.n.

## Änderungen in 1.1

* Nachrichten werden nun in Braille ausgegeben.
* Die Zusammenfassung der Audio-Auswahl wird in anderen Sprachen als
  Englisch präsentiert.
* Mehr Befehlsansagen hinzugefügt (wie z.B. Mischen/Trimmen oder das
  Verschieben von Cue-Positionen)
* Fehler mit Eingabefeldern in Effektdialogen behoben, in denen die
  Eingabefelder nicht oder falsch benannt wurden.
* Neue und aktualisierte Übersetzungen.

## Änderungen in 1.0

* Erstveröffentlichung.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=goldwave
