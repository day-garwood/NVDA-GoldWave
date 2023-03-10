# GoldWave #

* Autori: Joseph Lee împreună cu contributorii NVDA.
* Descarcă [Versiunea Stabilă][1]
* NVDA compatibility: 2022.4 and later

This app module enhances access and usage of GoldWave audio editor.

## Scurtături ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: Anunță poziția curentă a melodiei.
* NVDA+Shift+R: Anunță timpul rămas pentru melodia care este în curs de
  editare.
* Control+NVDA+1: Anunță canalul în care editezi.
* Control+NVDA+2: Anunță durata totală a fișierului audio.
* Control+NVDA+3: announces a summary on audio selection information.
* Control+NVDA+4: Anunță nivelul zoom.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

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

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Added input help messages for remainig time command (NVDA+Shift+R).
* Toggle command announcement command (NVDA+Shift+C) will now show up under
  "GoldWave" category in NVDA's input gestures dialog.

## Version 20.01

* Necesită NVDA.2019.3 sau mai nou.

## Version 19.11

* Este necesar Windows 7 SP1, GoldWave 6.x, și NVDA 2019.1 sau mai nou.
* A fost adăugat un mesaj de ajutor pentru fereastra sonoră (accesibil dacă
  suplimentul Control Usage Assistant este i)

## Version 18.12

* NVDA nu va mai afișa nici un mesaj sau reda vreun sunet de eroare atunci
  când executați anumite comenzi GoldWave cu anunțul de comandă oprit
  (aceasta ar putea avea ca rezultat un comportament nefiresc în unele
  cazuri).
* Modificări interne în sprijinul  viitoarelor versiuni NVDA

## Versiunea 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Versiunea 17.05

* S-a adăugat abilitatea de furnizare a informațiilor diagnosticării atunci
  când NVDA rulează cu diagnosticarea activată.
* Traduceri actualizate.

## Versiunea 16.12

* Schema versiunii este acum an.lună în loc de major.minor.

## Modificări aduse în versiunea 4.0

* Depozitul add-onului a fost mutat (Acum el este la
  https://github.com/josephsl/goldwave).
* Îmbunătățiri la performanță referitor la primirea informațiilor cum ar fi
  numele canalului și alte informații de stare.

## Modificări aduse în versiunea 3.0

* Added a command to announce remaining time for the current track
  (NVDA+Shift+R).
* Ceva îmbunătățiri referitor la primirea informațiilor de stare cum ar fi
  informații despre canal.

## Modificări aduse în 2.0

* Suport pentru Goldwave 6, inclusiv versiunea Goldwave pentru 64 biți
  (citește nota de mai sus).
* Ajutorul add-on-ului acum poate fi accesat din managerul de add-on-uri
  (NVDA 2014.3 sau mai nou).
* NVDA acum anunță canalul selectat dacă apeși comenzile de selecție a
  canalului cum ar fi control+shift+L pentru canalul din stânga.
* Rezolvări ale problemelor referitoare la câmpurile de editare cum ar fi
  câmpul de cursor și selectorul de timp în dialogul de mix, inclusiv
  selectarea textului, actualizarea valorilor și așa mai departe.
* Setarea comenzii de anunțare va fi re-amintită când se comută la alte
  programe.

## Modificări aduse în versiunea 1.2

* S-a rezolvat o problemă datorită căreia  NVDA avea dificultăți anunțând
  câteva câmpuri de editare.
* Traduceri noi și actualizate.
* Te rugăm să reții! Din cauza schimbărilor recente în NVDA, selecția audio
  și alte comenzi de status pot să nu funcționeze cum ar trebui la unele
  dispozitive.

## Modificări aduse în versiunea 1.11

* Suport pentru anunțări de mesaje în braille.
* Rezumatul selecției audio este prezentat în mai multe limbi decât Engleza.
* Mai multe comenzi de anunțare au fost adăugate incusiv mișcarea poziției
  și ștergerea sau tăierea operațiunilor.
* S-a rezolvat o problemă în câmpurile de editare numerice cum ar fi
  dialoguri diverse de efecte unde nu se vorbea nimic sau se pronunța numele
  incorect a câmpului de editare.
* Traduceri noi și actualizate.

## Modificări aduse în 1.0

* Lansarea oficială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
