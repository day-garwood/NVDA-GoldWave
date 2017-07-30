# Goldwave #

* Autori: Joseph Lee, NVDA doprinositelji.
* Preuzmite [stabilnu inačicu][1]
* Preuzmite [razvojnu inačicu][2]

Ova skripta unapređuje pristup i korištenje Goldwave uređivača zvuka.

## prečaci ##

* NvDA+Shift+C: uključuje /isključuje izgovor komandi prilikom uređivanja
  zvuka.
* Control+Shift+P: izvještava trenutnu poziciju u zapisu.
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+NVDA+1: Izgovara kanal kojeg uređujete.
* Control+NVDA+2: Izgovara cjelokupnu dužinu zvučne datoteke.
* Control+NvDA+3: izgovara sadržaj audio označavanja.
* Control+NVDA+4: Izvještava o razini povećanja.

Za više informacija o Goldwaveu i tipkovničkim prečacima, bacite pogled na
goldwave uputstvo.

Upozorenje: goldwave 6 zahtjeva 64 bitnu inačicu windowsa 7 ili
novijeg. NVDA 2014.1 or later is required to use add-on 2.0.

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
