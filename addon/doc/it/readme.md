# GoldWave #

* Autori: Joseph Lee, vari collaboratori di NVDA.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* NVDA compatibility: 2019.3 to 2020.2

Questo componente aggiuntivo migliora l'utilizzo e l'accessibilità
dell'editor audio GoldWave.

## Comandi rapidi ##

* NVDA+Shift+C: Attiva o disattiva la lettura dei comandi quando si lavora
  con l'audio.
* Control+Shift+P: legge la posizione attuale nella traccia.
* NVDA+Shift+R: legge il tempo restante nella traccia che si sta
  modificando.
* Control+NVDA+1: legge il canale che si sta modificando.
* Control+NVDA+2: legge la durata totale della traccia audio.
* Control+NvDA+3: legge alcune informazioni sull'audio  selezionato.
* Control+NVDA+4: legge il livello zoom.

Per maggiori informazioni su  Goldwave e i comandi da tastiera, consultare
il Manuale del programma.

Nota: GoldWave 6 richiede la versione a 64-bit di windows 7 o superiori. Per
utilizzare questo componente aggiuntivo è necessario NVDA 2019.3 o superiore
.

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

* Richiede NVDA 2019.3 o superiore.

## Novità nella versione 19.11

* E' richiesto Windows 7 SP1, GoldWave 6.x e NVDA 2019.1 o superiore.
* Aggiunto il messaggio di aiuto per la finestra suono (accessible se è
  installato l'add-on Control Usage Assistant.

## Novità nella versione 18.12

* NVDA non sembrerà più bloccato e non emetterà segnali acustici di errore
  quando si eseguiranno alcuni comandi di Goldwave con la lettura comandi
  disattivata (in alcuni casi ciò può dar luogo a comportamenti strani).
* Modifiche interne per supportare le versioni future di NVDA.

## Novità nella versione 18.07

* Risolto un problema per cui gli zeri iniziali non dovrebbero essere
  visualizzati quando si tenta di ottenere il tempo rimanente in una
  traccia.

## Novità nella versione 17.05

* Aggiunta la possibilità di fornire informazioni di debug quando NVDA è in
  esecuzione con il log di debug abilitato (NVDA 2017.1 o superiore).
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

* Aggiunto un comando per annunciare il tempo rimanente del brano corrente
  (NVDA+Shift+R).
* Lievi miglioramenti quando si vocalizzano informazioni di  stato, come le
  informazioni sul canale.

## Novità nella versione 2.0

* Supporto per GoldWave 6, tra cui la versione a 64 bit di GoldWave (vedi la
  nota precedente).
* L'aiuto per questo add-on si può ora aprire dalla finestra  Gestione
  Componenti Aggiuntivi (NVDA 2014.3 o superiore).
* NVDA ora legge il canale selezionato se si preme il comando per il canale
  selezionato, come ad esempio ctrl+Maiusc+L per il canale sinistro.
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
* Il riepilogo della selezione audio è presentato in lingue diverse
  dall'inglese.
* Aggiunta la vocalizzazione di ulteriori comandi, compreso lo spostamento
  dei cue points e le opzioni di trim.
* Risolto un problema nei campi editazione  numerici, come le finestre degli
  effetti, nelle quali i nomi dei campi venivano vocalizzati errati o non
  vocalizzati.
* Traduzioni nuove e aggiornate.

## Novità nella versione 1.0

* Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
