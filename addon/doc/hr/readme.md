# Goldwave #

* Autori: Joseph Lee, NVDA doprinositelji.
* Preuzmite [stabilnu inačicu][1]
* Preuzmite [razvojnu inačicu][2]
* NVDA compatibility: 2019.1 to 2019.2

This app module enhances access and usage of GoldWave audio editor.

## prečaci ##

* NvDA+Shift+C: uključuje /isključuje izgovor komandi prilikom uređivanja
  zvuka.
* Control+Shift+P: izvještava trenutnu poziciju u zapisu.
* NVDA+Shift+R: Izgovara preostalo vrijeme zapisa koji se trenutno uređuje.
* Control+NVDA+1: Izgovara kanal kojeg uređujete.
* Control+NVDA+2: Izgovara cjelokupnu dužinu zvučne datoteke.
* Control+NvDA+3: izgovara sadržaj audio označavanja.
* Control+NVDA+4: Izvještava o razini povećanja.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this
add-on, NVDA 2019.1 or later is required.

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

## Inačica 17.05

* Dodana mogućnost slanja informacija o greškama kad je NVDA pokrenut i
  omogućen otkrivač grešaka (NVDA inačica 2017.1 ili novija).
* Updated translations.

## Inačica 16.12

* Shema inačice je sada godina.mjesec umjesto glavna.minimalna.

## Changes for 4.0

* Repozitorij dodatka je premješten na GitHub (sada je dostupan na
  https://github.com/josephsl/goldwave).
* Poboljšanja pri pregledavanju informacija kao što su ime kanala i druge
  statusne informacije.

## Changes for 3.0

* Dodana naredba za izgovaranje preostalog vremena trenutnog zapisa
  (NVDA+Shift+R).
* Manja poboljšanja pri izgovoru statusnih informacija kao što je
  informacija o kanalu.

## Izmjene u inačici 2.0

* Podrška za Gold Wave 6, uključujući 64 bitnu inačicu goldwavea (pogledajte
  napomenu iznad).
* Pomoći dodatka sada se može pristupiti iz upravitelja dodataka (NVDA
  2014.3 i noviji).
* NVDA sada izgovara označeni kanal kada pritisnete prečace za označavanje
  kanala poput Control+Shift+L za lijevi kanal.
* razni problemi sa numeričkim poljima za uređivanje, kao što su to polje
  censor i označivać vremena u dijaloškom okviru za miksanje su ispravljene,
  uključujući označavanje teksta, osvježavanje vrijednosti i tako dalje.
* Obavještavanje o izgovoru prečaca su izgovorena kad se prebacujete na
  druge programe.

## Promjene u inačici 1.2

* Ispravljene greške označavanja i izgovaranja polja za uređivanje u nekim
  situacijama.
* novi i osvježeni prijevodi.
* Imajte na umu da zbog zadnjih promjena u NVDA, prečaci za označavanje
  zvuka i ostali prečaci neće možda raditi onako kako se to očekuje na nekim
  sustavima.

## Promjene u inačici 1.1

* Podrška prikaz poruka na brajičnom pismu.
* Sadržaj označenog zvuka je prezentiran i na drugim jezicima osim
  engleskog.
* Dodane nove obavjesti o prečacima uključujući cue poziciju kretanja i
  brisanje / trimming operacije.
* Ispravljena greška u numeričkim poljima za uređivanje kao što su to razni
  dijaloški okviri efekata gdje jje oznaka polja čitana polovično ili j
  nema.
* novi i osvježeni prijevodi.

## promjene u inačici 1.0

* Prva inačica.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
