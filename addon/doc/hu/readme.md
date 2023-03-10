# GoldWave #

* Készítők: Joseph Lee, NVDA közreműködők
* [Stabil verzió][1]
* NVDA compatibility: 2022.4 and later

This app module enhances access and usage of GoldWave audio editor.

## Gyorsbillentyűk ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: Az aktuális sávpozíció bemondása.
* NVDA+Shift+R: Bemondja a szerkesztés alatt lévő sávból hátra lévő időt.
* Control+NVDA+1: A szerkesztés alatt álló csatorna bemondása.
* Control+NVDA+2: A hangfájl teljes hosszának bemondása.
* Control+NVDA+3: announces a summary on audio selection information.
* Control+NVDA+4: A nagyítási szint bemondása.

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

* Added ability to provide debug information when NVDA is running with debug
  logging enabled (NVDA 2017.1 or later).
* Updated translations.

## Version 16.12

* Version scheme is now year.month instead of major.minor.

## A 4.0 verzió változásai

* A bővítmény tárolóját áthelyezték a GitHubra (jelenleg a
  https://github.com/josephsl/goldwave webhelyen található).
* Performance improvements when looking up information such as channel name
  and other status information.

## A 3.0 verzió változásai

* Added a command to announce remaining time for the current track
  (NVDA+Shift+R).
* Kissebb javítások történtek az állapot információk bemondásában, úgy mint
  csatorna információk.

## A 2.0 verzió változásai

* A GoldWave 6 támogatása, beleértve a 64-bites változatot is. (Lásd a fenti
  megjegyzést!).).
* A kiegészítő súgója már elérhető az NVDA Bővítménykezelő
  párbeszédpanelén. NVDA 2014.3 és újabb verziói esetén.
* Az NVDA már bejelenti a kiválasztott csatornát csatornák kijelölésére
  szolgáló parancsok használatakor (Control+Shift+L a bal oldali csatorna
  kijelöléséhez).
* Különböző számokkal dolgozó szerkesztőmezőkkel (szűrőmező, vagy
  időválasztó a mix párbeszédpanelen) kapcsolatos hiba javítva, beleértve
  szöveg kijelölése, érték módosítása, stb.
* A parancsok bejelentésére vonatkozó beállítás más programokra váltás
  esetén is megmarad.

## Az 1.2 verzió változásai

* Kijavításra került az a hiba, mely néhány szerkesztő mező bemondásakor
  lépett fel.
* Új, és frissített fordítások.
* Kérjük, vegye figyelembe, hogy a legújabb NVDA változások miatt, az audio
  kijelölés és egyéb státusz billentyűparancsok nem minden rendszeren
  működnek megfelelően.

## Az 1.1 verzió változásai

* Támogatott az üzenetek Braille megjelenítése
* A kijelölt hang tulajdonságai már nem csak angol nyelven elérhetők.
* Több parancs bemondása hozzáadva, köztük a hellyelző mozgása, törlés/trim
  műveletek.
* Hibajavítás a numerikus szerkesztőmezőkben, olykor hibás mező megnevezés
  került bemondásra.
* Új, és frissített fordítások.

## Az 1.0 verzió változásai

* Kezdeti verzió.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
