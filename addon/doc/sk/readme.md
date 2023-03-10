# GoldWave #

* Autori: Joseph Lee, tím NVDA.
* Stiahnuť [stabilnú verziu][1]
* NVDA compatibility: 2022.4 and later

Tento aplikačný modul zvyšuje prístupnosť a použiteľnosť zvukového editoru
goldwave.

## Klávesové skratky ##

* NVDA+Shift+C: prepína oznamovanie príkazov počas úpravy zvuku.
* ctrl+Shift+P: Oznámy pozíciu v aktuálnej stope.
* Nvda+shift+R: oznámuje zostávajúci čas otvoreného súboru.
* Ctrl+NVDA+1: oznámy kanál, ktorý upravujete.
* Ctrl+NVDA+2: Oznámy celkovú dĺžku audio súboru.
* Ctrl+NVDA+3: Oznámy informácie o aktuálnom výbere.
* Ctrl+NVDA+4: oznamuje úroveň priblíženia.

pre viac informácii o klávesových skratkách programu Goldwave si prečítajte
návod k programu Goldwave.

Note: GoldWave 6 or later is required.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.
* In GoldWave 6.57 and later, NVDA will no longer repeat the name of the
  loaded file when pressing play/rewind/stop keys.

## Version 21.06

* Resolved additional coding style issues and potential bugs with Flake8.

## Verzia 20.04

* Opravené drobné chyby v kóde.

## Verzia 20.04

* Pridaný popis skratky na zisťovanie ostávajúceho času do nápovedy vstupu
  (skratka nvda+shift+r).
* Skratka na nastavenie hlásení (nvda+shift+c) sa odteraz dá upravovať v
  dialógu klávesové skratky, vetva Goldwave.

## Verzia 20.01

* Funguje s NVDA od verzie 2019.3.

## Verzia 19.11

* Vyžaduje sa Windows 7 SP1, GoldWave 6.x, a NVDA 2019.1.
* Pridaná pomocná správa pre okno so zvukom (funguje ak sa používa doplnok
  Pomoc na práci s prvkami).

## Verzia 18.12

* NVDA viac nehlási chybu pri opužití skratiek a súčasnom vypnutí
  výrečnosti.
* Interné zmeny ako príprava na budúce verzie NVDA.

## Verzia 18.07

* Odteraz sa zobrazujú nuly, ak sú na začiatku ostávajúceho času súboru.

## Verzia 17.05

* Od verzie NVDA 2017.1 sa informácie o činosti doplnku zapisujú do logu
  NVDA ak je nastavené zaznamenávanie na debug.
* Nové a aktualizované preklady.

## Verzia 16.12

* Verzie číslujeme ako rok.mesiac.

## Zmeny vo verzii 4.0

* Repozitár dopnku presunutý na GitHub
  (https://github.com/josephsl/goldwave).
* Zrýchlená odozva pri zisťovaní informácie o kanáloch a iných stavových
  údajoch.

## Zmeny vo verzii 3.0

* Pridaná skratka, ktorá oznamuje ostávajúci čas ( nvda+shift+r).
* Mierne upravené oznamovanie stavových informácií.

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
  polia.
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

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
