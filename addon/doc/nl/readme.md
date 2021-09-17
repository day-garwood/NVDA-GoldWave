# GoldWave #

* Auteurs: Joseph Lee, NVDA contributors.
* Download [stabiele versie][1]
* NVDA compatibility: 2021.2 and beyond

This app module enhances access and usage of GoldWave audio editor.

## Sneltoetsen ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* NVDA+Shift+P: Kondigt de positie aan in het huidige bestand.
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+NVDA+1: Kondigt het kanaal aan dat u aan het bewerken bent.
* Control+NVDA+2: Kondigt de totale lengte aan van het geluidsbestand.
* Control+NVDA+3: announces a summary on audio selection information.
* NVDA+Shift+Z: Kondigt het zoomniveau aan.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 or later is required.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.06

* Resolved additional coding style issues and potential bugs with Flake8.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Added input help messages for remainig time command (NVDA+Shift+R).
* Toggle command announcement command (NVDA+Shift+C) will now show up under
  "GoldWave" category in NVDA's input gestures dialog.

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
  (NVDA+Shift+R).
* Slight improvements when announcing status information such as channel
  information.

## Veranderingen voor 2.0

* Ondersteuning voor GoldWave 6, inclusief 64-bit versie van GoldWave (zie
  opmerking hierboven).
* Add-onhelp kan nu geopend worden vanuit Add-ons beheren (NVDA 2014.3 en
  nieuwer).
* NVDA meldt nu het geselecteerde kanaal bij het gebruik van commando's voor
  kanaalselectie, zoals Control+Shift+L voor het linker kanaal.
* Verschillende problemen in numerieke invoervelden met betrekking tot
  selecteren en het veranderen van waarden opgelost.
* De instelling voor het aankondigen van commando's wordt nu onthouden bij
  het schakelen naar andere programma's.

## Veranderingen voor 1.2

* Een probleem opgelost waarbij NVDA moeilijkheden had om sommige
  invoervelden aan te kondigen.
* Nieuwe en bijgewerkte vertalingen.
* Merk op dat tengevolge recente veranderingen in NVDA, in sommige systemen
  audioselectie en andere statuscommando's misschien niet werken zoals
  verwacht.

## Veranderingen voor 1.1

* Ondersteuning voor berichtaankondigingen in braille.
* Audio selection summary wordt weergegeven in andere talen dan Engels.
* Meer aankondigingen van commando's toegevoegd inclusief cue position
  movement en delete/trim operations.
* Een probleem opgelost in numerieke invoervelden zoals in verschillende
  dialoogvensters met effecten waarbij geen of verkeerde veldnamen werden
  aangekondigd.
* Nieuwe en bijgewerkte vertalingen.

## Veranderingen voor 1.0

* Eerste versie.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv
