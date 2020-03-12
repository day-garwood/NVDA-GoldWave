# GoldWave #

* Autori: Joseph Lee, NVDA doprinositelji.
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2019.3 i novija

Ovaj modul aplikacije unapređuje pristup uređivaču zvuka GoldWave, kao i
njegovo korištenje.

## Prečaci ##

* NVDA+šift+C: Uključuje ili isključuje izgovaranje naredbi prilikom
  uređivanja audio trake.
* Kontrol+šift+P: Najavljuje trenutačnu poziciju audio trake.
* NVDA+šift+R: Najavljuje preostalo vrijeme trake koja se trenutačno
  uređuje.
* Kontrol+NVDA+1: Najavljuje kanal koji se uređuje.
* Kontrol+NVDA+2: Najavljuje cjelokupno trajanje audio datoteke.
* Kontrol+NVDA+3: Najavljuje sažete informacije o odabranom dijelu audio
  trake.
* Kontrol+NVDA+4: Najavljuje razinu zumiranja.

Daljnje informacije o GoldWaveu i tipkovničkim prečacima je moguće naći u
priručniku za GoldWave.

Napomena: GoldWave 6 zahtijeva 64-bitnu verziju Windowsa 7 ili novijeg
sustava. Za pokretanje ovog dodatka potreban je NVDA 2019.3 ili noviji.

## Verzija 20.01

* Zahtijeva NVDA 2019.3 ili noviju verziju.

## Verzija 19.11

* Potrebni su Windows 7 SP1, GoldWave 6.x i NVDA 2019.1 ili noviji.
* Dodana je poruka pomoći za zvučni prozor (dostupno, ako je instaliran
  dodatak „Pomoćnik za primjenu kontrola”).

## Verzija 18.12

* NVDA više neće izgledati kao da ništa ne radi ili svirati zvukove za
  greške pri izvršavanju određenih GoldWave naredbi s isključenim
  najavljivanjem naredbi (u nekim slučajevima to može prouzročiti čudna
  ponašanja).
* Unutarnje promjene, kako bi se podržala buduća NVDA izdanja.

## Verzija 18.07

* Ispravljena je greška, gdje se prednje nule nisu prikazivale pri dobivanju
  preostalog vremena zvučnog zapisa.

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
  (NVDA+šift+R).
* Manja poboljšanja pri najavljivanju informacija o stanju, kao što su
  informacije o kanalu.

## Promjene u verziji 2.0

* Podrška za GoldWave 6, uključujući 64-bitnu verziju GoldWavea (pogledajte
  napomenu iznad).
* Pomoć dodatka je sada dostupna u upravljaču dodataka (NVDA 2014.3 i
  noviji).
* NVDA sada najavljuje odabrani kanal tijekom pritiskanja prečaca za biranje
  kanala, kao što je Kontrol+šift+L za lijevi kanal.
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
* Sažetak o odabranom dijelu audio trake prikazuje se i na drugim jezicima
  osim engleskog.
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
