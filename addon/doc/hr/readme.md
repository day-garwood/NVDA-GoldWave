# Goldwave #

* Autori: Joseph Lee, NVDA doprinositelji.
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA compatibility: 2019.1 to 2019.2

This app module enhances access and usage of GoldWave audio editor.

## Prečaci ##

* NvDA+Shift+C: Uključuje ili isključuje izgovaranje naredbi prilikom
  uređivanja audio trake.
* Control+Shift+P: Najavljuje trenutačnu poziciju audio trake.
* NVDA+Shift+R: Najavljuje preostalo vrijeme trake koja se trenutačno
  uređuje.
* Control+NVDA+1: Najavljuje kanal koji se uređuje.
* Control+NVDA+2: Najavljuje cjelokupno trajanje audio datoteke.
* Control+NvDA+3: Najavljuje sažete informacije o odabranom dijelu audio
  trake.
* Control+NVDA+4: Najavljuje razinu zumiranja.

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

## Verzija 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Verzija 17.05

* Dodana je mogućnost slanja informacija o greškama kad je NVDA pokrenut s
  uključenim otkrivačem grešaka (NVDA verzija 2017.1 ili novija).
* Aktualizirani prijevodi.

## Verzija 16.12

* Shema verzije je sada godina.mjesec umjesto glavna.sporedna.

## Promjene u verziji 4.0

* Repozitorij dodatka je premješten na GitHub (sada je dostupan na
  https://github.com/josephsl/goldwave).
* Poboljšana performanca za pretraživanje informacija, kao što su ime kanala
  i druge informacije o stanju.

## Promjene u verziji 3.0

* Dodana je naredba za najavljivanje preostalog vremena trenutačne trake
  (NVDA+Shift+R).
* Manja poboljšanja pri najavljivanju informacija o stanju, kao što su
  informacije o kanalu.

## Promjene u verziji 2.0

* Podrška za GoldWave 6, uključujući 64-bitnu verziju GoldWavea (pogledajte
  napomenu iznad).
* Pomoć dodatka je sada dostupna u upravljaču dodataka (NVDA 2014.3 i
  noviji).
* NVDA sada najavljuje odabrani kanal tijekom pritiskanja prečaca za biranje
  kanala, kao što je Control+Shift+L za lijevi kanal.
* Ispravljeni su razni problemi s numeričkim poljima za uređivanje, kao što
  su polje censor i označivač vremena u dijaloškom okviru za miksanje,
  uključujući označavanje teksta, aktualiziranje vrijednosti i tako dalje.
* Postavke za najavljivanje prečaca će se zapamtiti prilikom prelaženja na
  druge programe.

## Promjene u verziji 1.2

* Ispravljena je greška, gdje je NVDA imao poteškoće najaviti neka polja za
  uređivanje.
* Novi i aktualizirani prijevodi.
* Napomena: zbog nedavnih promjena u NVDA čitaču, prečaci za biranje audio
  snimke i ostali prečaci za stanja, na nekim sustavima možda neće raditi
  onako kako se to očekuje.

## Promjene u verziji 1.1

* Podrška za najavljivanje poruka u brajici.
* Sažetak o odabranom dijelu audio trake se prikazuje i na drugim jezicima
  osim na engleskom.
* Dodana su nova najavljivanja za prečace, uključujući prečac za pomicanje
  pozicije signala te operacije za brisanje i kraćenje.
* Ispravljena je greška u numeričkim poljima za uređivanje kao što su razni
  dijaloški okviri efekata, gdje se ništa nije čitalo ili se čitalo krivo
  polje.
* Novi i aktualizirani prijevodi.

## Promjene u verziji 1.0

* Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
