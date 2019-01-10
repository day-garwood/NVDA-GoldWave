# Goldwave #

* Autori: Joseph Lee, vari collaboratori di NVDA.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* Compatibilità con NVDA: dalla 2017.3 alla 2019.1

Questo componente aggiuntivo migliora l'utilizzo e l'accessibilità per
l'editor audio GoldWave 

## Comandi rapidi: ##

* NVDA+Shift+C: Attiva o disattiva la lettura dei comandi quando si lavora
  con l'audio.
* Control+Shift+P: legge la posizione attuale nella traccia. 
* NVDA+Shift+R: legge il tempo restante nella traccia che si sta
  modificando.
* Control+NVDA+1: legge il canale che si sta modificando.
* Control+NVDA+2: legge il tempo totale della traccia audio.
* Control+NvDA+3: legge alcune informazioni sull'audio  selezionato.
* Control+NVDA+4: legge il livello zoom.

Per maggiori informazioni su  Goldwave ed i comandi rapidi, consultare il
Manuale del programma.

Nota: GoldWave 6 richiede la versione a 64-bit di windows 7 o superiori. E'
necessario NVDA 2014.1 o superiore per la versione 2.0 del componente
aggiuntivo.

## Version 18.07

* Risolto un problema per cui gli zeri iniziali non dovrebbero essere
  visualizzati quando si tenta di ottenere il tempo rimanente in una
  traccia. 

## Version 17.05

* Aggiunta la possibilità di fornire informazioni di debug quando NVDA è in
  esecuzione con la registrazione di debug abilitato (NVDA 2017.1 o versione
  successiva). 
* Traduzioni aggiornate. 

## Version 16.12

* Version scheme is now year.month instead of major.minor.

## Changes for 4.0

* Add-on repository has moved to GitHub (now located at
  https://github.com/josephsl/goldwave).
* Miglioramenti delle prestazioni per la ricerca di informazioni come il
  nome del canale e altre situazioni. 

## Changes for 3.0

* Aggiunto un comando per annunciare il tempo residuo del brano corrente
  (NvDA+Shift+R). 
* Lievi miglioramenti, lettura di informazioni sullo  stato come ad esempio
  informazioni sul canale. 

## Changes for 2.0

* Supporto per GoldWave 6, tra cui la versione a 64 bit di GoldWave (vedi la
  nota precedente). 
* La guida di aiuto si può ora aprire dalla finestra  Gestore Componenti
  Aggiuntivi (NVDA 2014.3 e superiori).
* NVDA ora legge il canale selezionato premendo il comando per il canale
  selezionato, come ad esempio ctrl+Maiusc+L per il canale sinistro. 
* Various issues with numeric edit fields such as censor field and time
  selector in mix dialog has been fixed, including selecting text, updating
  values and so on.
* Command announcement setting will be remembered when switching to other
  programs.

## Changes for 1.2

* Fixed an issue where NVDA had difficulty announcing some edit fields.
* New and updated translations.
* Please note that due to recent changes in NVDA, audio selection and other
  status commands may not work as expected in some systems.

## Changes for 1.1

* Support for message announcements in braille.
* Audio selection summary is presented in languages other than English.
* More command announcements added including cue position movement and
  delete/trim operations.
* Fixed an issue in numeric edit fields such as various effects dialogs
  where nothing or wrong field name was announced.
* New and updated translations.

## Changes for 1.0

* Initial version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
