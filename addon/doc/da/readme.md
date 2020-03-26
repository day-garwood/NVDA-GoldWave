# GoldWave #

* Forfattere: Joseph Lee, NVDA bidragydere.
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2019.3 to 2020.1

This app module enhances access and usage of GoldWave audio editor.

## Genveje ##

* NvDA+Shift+C: Toggles speaking of commands during audio editing.
* Ctrl+Skift+P: Annoncerer aktuelle sporposition.
* NVDA+Skift+R: Annoncerer resterende tid for det spor du er i færd med at
  redigere.
* NVDA+Ctrl+1: Annoncerer kanalen du redigere.
* NVDA+Ctrl+2: Annoncerer den fulde længde af lydfilen.
* Control+NvDA+3: announces a summary on audio selection information.
* NVDA+Ctrl+4: Annoncere det aktuelle niveau for zoom.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this
add-on, NVDA 2019.3 or later is required.

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

* Tilføjet mulighed for at give fejlfindingsoplysninger, når NVDA kører med
  logføring aktiveret (NVDA 2017.1 eller senere).
* Opdaterede oversættelser.

## Version 16.12

* Versionsordning er nu year.month i stedet for major.minor.

## Ændringer i 4.0

* Depotet til tilføjelsen er flyttet til GitHub (nu placeret på
  https://github.com/josephsl/goldwave).
* Ydelsesforbedringer, når du slår op information som kanalnavn og anden
  statusinformation.

## Ændringer i 3.0

* Added a command to announce remaining time for the current track
  (NvDA+Shift+R).
* Små forbedringer når NVDA annoncerer statusoplysninger såsom
  kanaloplysninger.

## Ændringer i 2.0

* Understøttelse for GoldWave 6, herunder 64-bit version af GoldWave (se
  bemærkning ovenfor).
* Hjælp til tilføjelsen kan nu tilgås ved hjælp fra dialogen "Styring af
  tilføjelsesprogrammer" (NVDA 2014.3 og nyere).
* NVDA annoncerer nu den valgte kanal, hvis du trykker på
  kanalvalgskommandoer som Ctrl+Skift+L for den venstre kanal.
* Forskellige problemer med numeriske redigere felter som censor felt og
  time selector i mix dialog er blevet rettet, herunder valg af tekst,
  opdatering værdier, osv.
* Indstilling til annoncering af kommandoer vil blive husket, når der
  skiftes til andre programmer.

## Ændringer i 1.2

* Rettede et problem, hvor NVDA havde svært ved at annoncere nogle
  editfelter.
* Nye og opdaterede oversættelser.
* Bemærk venligst at på grund af de seneste ændringer i NVDA, vil kommandoer
  til valg af lyd og statuskommandoer ikke nødvendigvis fungerer korrekt på
  nogle systemer.

## Ændringer i 1.1

* Understøtter meddelelser på punkt, når informationer annonceres.
* Opsummeringer af den markerede del af lydfilen vil nu blive præsenteret i
  andre sprog udover engelsk.
* Flere kommandomeddelelser tilføjet, herunder bevægelser af
  startmarkeringer samt beskæring og sletning.
* Rettede et problem i flere redigeringsfelter, såsom forskellige
  effect-dialoger hvor intet eller forkert feltnavn blev annonceret.
* Nye og opdaterede oversættelser.

## Ændringer i 1.0

* Første version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
