# Goldwave #

* Autori: Joseph Lee, tím NVDA.
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][3] compatible with NVDA 2019.2.1 and earlier

This app module enhances access and usage of GoldWave audio editor.

## Klávesové skratky ##

* NVDA+Shift+C: prepína oznamovanie príkazov NVDA počas strihania.
* ctrl+Shift+P: Oznámy pozíciu v aktuálnej stope.
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+NVDA+1: oznámy kanál, ktorý upravujete.
* Control+NVDA+2: Oznámy celkovú dĺžku audio súboru.
* Control+NVDA+3: Oznámy informácie o aktuálnom výbere.
* Control+NVDA+4: oznamuje úroveň priblíženia.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this
add-on, NVDA 2019.3 or later is required.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 19.11

* Windows 7 SP1, GoldWave 6.x, and NVDA 2019.1 or later is required.
* Added help message for sound window (accessible if Control Usage Assistant
  add-on is installed).

## Version 18.12

* NVDA will no longer appear to do nothing or play error tones when
  performing certain GoldWave commands with command announcement set to off
  (this may result in odd behaviors in some cases).
* Internal changes to support future NVDA releases.

## Version 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Version 17.05

* Added ability to provide debug information when NVDA is running with debug
  logging enabled (NVDA 2017.1 or later).
* Updated translations.

## Version 16.12

* Version scheme is now year.month instead of major.minor.

## Changes for 4.0

* Add-on repository has moved to GitHub (now located at
  https://github.com/josephsl/goldwave).
* Performance improvements when looking up information such as channel name
  and other status information.

## Changes for 3.0

* Added a command to announce remaining time for the current track
  (NvDA+Shift+R).
* Slight improvements when announcing status information such as channel
  information.

## Zmeny vo verzii 2.0

* Podpora pre Goldwave 6 vrátane 64-bitovej verzie (pozrite poznámku vyššie)
* Pomocník doplnku si môžete pozrieť priamo zo správcu doplnkov (od verzie
  2014.3)
* NVDA odteraz oznamuje vybratý kanál, ak na výber použijete skratky,a ko
  napr ctrl+shift+l.
* Vyriešené problémy s editačnými poliami v dialógu mix, takže správne
  funguje výber textu a úprava údajov.
* Oznamovanie funkcií si NVDA zapamätá aj po prechode do okna inej
  aplikácie.

## Zmeny pre verziu 1.2

* opravená chyba, pri ktorej NVDA neoznamovalo správne niektoré editačné
  polia
* Nové a aktualizované preklady.
* Berte prosím na vedomie, že vvzhľadom na posledné zmeny v NVDA, niektoré
  príkazy na označovanie audia nemusia fungovať korektne.

## Zmeny pre verziu 1.1

* Podpora pre zobrazovanie správ na brailovských riadkoch.
* Súhrn výberu je oznamovaný aj v iných jazykoch, nie len v angličtine.
* Pridané oznamovanie odstránenia za označeným úsekom a oznamovanie
  vkladania rozdeľovačov.
* opravený problém, keď boli nesprávne oznamované popisy editačných polí v
  dialógoch s efektami.
* Nové a aktualizované preklady.

## Zmeny pre verziu 1.0

* prvé vydanie.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev

[3]: https://addons.nvda-project.org/files/get.php?file=gwv-2019
