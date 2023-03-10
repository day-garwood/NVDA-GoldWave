# GoldWave #

* Autori: Joseph Lee, vari collaboratori di NVDA.
* Scarica la [versione stabile][1]
* NVDA compatibility: 2022.4 and later

Questo componente aggiuntivo migliora l'utilizzo e l'accessibilità
dell'editor audio GoldWave.

## Comandi rapidi ##

* NVDA+Shift+C: Attiva/disattiva la lettura dei comandi quando si lavora con
  l'audio.
* Control+Shift+P: legge la posizione attuale nella traccia.
* NVDA+Shift+R: legge il tempo restante nella traccia che si sta
  modificando.
* Control+NVDA+1: legge il canale che si sta modificando.
* Control+NVDA+2: legge la durata totale della traccia audio.
* Control+NvDA+3: legge alcune informazioni sull'audio  selezionato.
* Control+NVDA+4: legge il livello di zoom.

Per maggiori informazioni su  Goldwave e i suoi comandi da tastiera,
consultare il Manuale del programma.

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

## Novità nella versione 20.06

* Risolti molti problemi legati allo stile del codice e bug potenziali con
  Flake8.

## Novità nella versione 20.04

* Aggiunti i messaggi di aiuto immissione dedicati al comando per il tempo
  rimanente (NVDA+Shift+R).
* Il comando "Attiva/disattiva la lettura dei comandi" (NVDA+Shift+C)  ora
  apparirà sotto la categoria "Goldwave" nella finestra Gesti e Tasti di
  Immissione di NVDA.

## Novità nella versione 20.01

* Richiede NVDA 2019.3 o versioni successive.

## Novità nella versione 19.11

* E' richiesto Windows 7 SP1, GoldWave 6.x e NVDA 2019.1 o versioni
  successive.
* Aggiunto il messaggio di aiuto per la finestra suono (disponible se è
  installato l'add-on Control Usage Assistant.

## Novità nella versione 18.12

* NVDA non sembrerà più bloccato e non emetterà segnali acustici di errore
  quando si eseguiranno alcuni comandi di Goldwave con la lettura comandi
  disattivata (in alcuni casi ciò può dar luogo a comportamenti strani).
* Modifiche interne per supportare le versioni future di NVDA.

## Novità nella versione 18.07

* Risolto un problema che causava la visualizzazione degli zeri iniziali
  quando si tentava di ottenere il tempo rimanente in una traccia.

## Novità nella versione 17.05

* Aggiunta la possibilità di fornire informazioni di debug quando NVDA è in
  esecuzione con il livello di log impostato su debug (NVDA 2017.1 o
  superiore).
* Traduzioni aggiornate.

## Novità nella versione 16.12

* Lo schema del numero di versione adesso è anno.mese invece di
  principale.secondario.

## Novità nella versione 4.0

* Il repository dell'Add-on si è spostato su GitHub (ora si trova
  all'indirizzo https://github.com/josephsl/goldwave).
* Miglioramenti delle prestazioni in caso di ricerca di informazioni come il
  nome del canale e altre informazioni di stato.

## Novità nella versione 3.0

* Aggiunto un comando per leggere il tempo rimanente del brano corrente
  (NVDA+Shift+R).
* Lievi miglioramenti nella vocalizzazione delle informazioni di  stato,
  come le informazioni sul canale.

## Novità nella versione 2.0

* Supporto per GoldWave 6, compresa la versione a 64 bit di GoldWave (vedi
  la nota precedente).
* L'aiuto per questo add-on si può ora aprire dalla finestra  Gestione
  Componenti Aggiuntivi (NVDA 2014.3 o superiore).
* NVDA ora legge il canale selezionato se si preme il relativo comando, come
  ad esempio ctrl+Maiusc+L per il canale sinistro.
* Sono stati risolti numerosi problemi con i campi editazione  numerici,
  come il campo Censura e il selettore del tempo, nella finestra mix,
  compresa la selezione del testo, l'aggiornamento dei valori e così via.
* L'impostazione della lettura comandi verrà salvata quando si passa ad
  altri programmi.

## Novità nella versione 1.2

* Risolto un problema per il quale NVDA aveva difficoltà a vocalizzare
  alcuni campi editazione.
* Traduzioni nuove e aggiornate.
* Si noti che, a causa di recenti modifiche ad NVDA, la selezione  audio e
  altri comandi di stato potrebbero non funzionare come ci si aspetta in
  alcuni sistemi.

## Novità nella versione 1.1

* Supporto per la rappresentazione in braille dei messaggi.
* Il riepilogo della selezione audio viene fornito anche in lingue diverse
  dall'inglese.
* Aggiunta la vocalizzazione di ulteriori comandi, compreso lo spostamento
  dei cue points e le opzioni di trim.
* Risolto un problema nei campi editazione  numerici, come le finestre degli
  effetti, nelle quali i nomi dei campi venivano vocalizzati in modo errato
  o non vocalizzati.
* Traduzioni nuove e aggiornate.

## Novità nella versione 1.0

* Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
