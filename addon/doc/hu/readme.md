# Goldwave #

* Készítők: Joseph Lee, NVDA közreműködők
* [Stabil verzió][1]
* [Fejlesztői verzió][2]

Ez a kiegészítő javítja a Goldvawe hangszerkesztő hozzáférhetőségét, és
használatát.

## Gyorsbillentyűk ##

* NvDA+Shift+C: Hangszerkesztés közben átvált a parancsok bemondására.
* Control+Shift+P: Az aktuális sávpozíció bemondása.
* NVDA+Shift+R: Bemondja a szerkesztés alatt lévő sávból hátra lévő időt.
* Control+NVDA+1: A szerkesztés alatt álló csatorna bemondása.
* Control+NVDA+2: A hangfájl teljes hosszának bemondása.
* Control+NvDA+3: A kijelölt hang tulajdonságainak bemondása.
* Control+NVDA+4: A nagyítási szint bemondása.

Bővebb információt a programról és a hozzátartozó billentyűparancsokról a
Goldwave súgójában talál.

Megjegyzés: A GoldWave 6 futtatásához 64-bites Windows 7 vagy újabb verzió
szükséges. A kiegészítő 2.0 verziójának használatához NVDA 2014.1 vagy újabb
kiadás szükséges.

## Version 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a track.

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

* Billentyűparancs került hozzáadásra az aktuális sáv hátralévő idejének
  lekérésére (NVDA+Shift+r)
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

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
