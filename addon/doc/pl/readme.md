# Goldwave #

* Autorzy: Joseph Lee, współpracownicy NVDA.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* NVDA compatibility: 2019.1 to 2019.2

This app module enhances access and usage of GoldWave audio editor.

## Skróty ##

* NvDA+Shift+C: przełącza wypowiadanie komend podczas edycji audio.
* Control+Shift+P: odczytuje aktualną pozycję ścieżki.
* NVDA+Shift+R: Oznajmia pozostały czas dla aktualnie edytowanego utworu.
* Control+NVDA+1: wypowiada aktualnie edytowany kanał.
* Control+NVDA+2: wypowiada całkowitą długość pliku dźwiękowego.
* Control+NvDA+3: czyta informacje o aktualnym zaznaczeniu audio.
* Control+NVDA+4: wypowiada aktualny poziom powiększenia.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this
add-on, NVDA 2019.1 or later is required.

## Wersja 19.11

* Windows 7 SP1, GoldWave 6.x, i NVDA 2019.1 i nowsze są wymagane.
* Dodano wiadomość kontekstową doa okna dźwięku (dostępne jeśli dodatek
  Control usage assistant jest zainstalowany).

## wersja 18.12

* NVDA will no longer appear to do nothing or play error tones when
  performing certain GoldWave commands with command announcement set to off
  (this may result in odd behaviors in some cases).
* Internal changes to support future NVDA releases.

## Wersja 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Wersja 17.05

* Dodano możliwość dostarczania informacji o debugowaniu po uruchomieniu
  NVDA w trybie debugowania (NVDA w wersji 2017.1 lub nowszej).
* Aktualizacja tłumaczeń

## Wersja 16.12

* Schemat wersjonowania został zmieniony i teraz brzmi on rok.miesiąc
  zamiast duży.mniejszy.

## Zmiany dla wersji 4.0

* Repozytorium tego dodatku zostało przeniesione na Github (teraz znajdujący
  się pod adresem https://github.com/josephsl/goldwave).
* Ulepszona wydajność przy pobieraniu informacji takich jak nazwa kanału i
  inne informacje statusu.

## Zmiany dla wersji 3.0

* Dodano komendę wypowiadania czasu trwania aktualnego utworu
  (NvDA+Shift+R).
* Trochę większe ulepszenia czytania informacji stanu takich jak informacji
  o kanale.

## Zmiany dla wersji 2.0

* Wsparcie dla GoldWave 6, włącznie z 64-bitową wersją GoldWave (zobacz
  powyższą uwagę).
* Pomoc dodatku dostępna w managerze dodatków (NVDA 2014.3 i nowsze).
* NVDA oznajmia wybrany kanał po wciśnięciu polecenia zmiany zaznaczonego
  kanału np. Control+Shift+L dla zaznaczenia lewego kanału.
* Rozwiązano różne problemy z edycją pól numerycznych, np. pole cenzora i
  wybór czasu w oknie miksowania, w tym zaznaczanie tekstu, aktualizowanie
  wartości itd.
* Przełącznik oznajmiania komend jest zapamiętywany po przejściu do innych
  programów.

## Zmiany dla wersji 1.2

* Poprawiono problem dotyczący odczytywania przez NVDA niektórych pól
  edycji.
* Nowe i zaktualizowane tłumaczenia.
* Proszę zwrócić uwagę, że w związku z ostatnimi zmianami w NVDA,
  zaznaczanie audio i inne polecenia statusu mogą nie działać na niektórych
  systemach zgodnie z oczekiwaniami.

## Zmiany dla wersji 1.1

* Obsługa powiadomień w brajlu.
* Podsumowanie zaznaczenia audio jest prezentowane w językach innych niż
  angielski.
* Dodane oznajmianie większej liczby komend, uwzględniające takie polecenia
  jak przemieszczenia wskaźników, operacje usuwania i przycinania.
* Poprawiono problem w polach edycji liczb, np. w różnych okienkach efektów,
  gdzie oznajmiana była nieprawidłowa nazwa, albo brak nazwy kontrolki.
* Nowe i zaktualizowane tłumaczenia.

## Zmiany dla wersji 1.0

* Początkowa wersja.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
