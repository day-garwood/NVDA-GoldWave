# GoldWave #

* Autoren: Joseph Lee und die NVDA-Entwicklergemeinde.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2019.3 bis 2020.3

Diese Erweiterung verbessert die Zugänglichkeit des Audio-Editors GoldWave.

## Tastenkombinationen ##

* NVDA+Umschalt+C: Schaltet die Ansage beim Drücken der Tastenkombinationen
  während der Audio-Bearbeitung um.
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

Bitte beachten Sie: GoldWave 6 benötigt die 64-Bit-Version von Windows 7
oder neuer. NVDA 2019.3 oder neuer ist erforderlich, um diese Erweiterung
einzusetzen.

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

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
