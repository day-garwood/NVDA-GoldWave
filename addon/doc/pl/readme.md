# GoldWave #

* Autorzy: Joseph Lee, współpracownicy NVDA.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* NVDA compatibility: 2019.3 to 2020.1

Ten dodatek zwiększa dostępność i użyteczność edytora audio Goldwave.

## Skróty ##

* NvDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: odczytuje aktualną pozycję ścieżki.
* NVDA+Shift+R: Oznajmia pozostały czas dla aktualnie edytowanego utworu.
* Control+NVDA+1: wypowiada aktualnie edytowany kanał.
* Control+NVDA+2: wypowiada całkowitą długość pliku dźwiękowego.
* Control+NvDA+3: announces a summary on audio selection information.
* Control+NVDA+4: wypowiada aktualny poziom powiększenia.

Więcej informacji o Goldwave i jego klawiszach skrótów, znajduje się w
podręczniku Goldwave.

Uwaga: GoldWave 6 wymaga 64-bitowej wersji Windows 7 lub nowszej. Aby używać
tego dodatku, potrzebna jest wersja NVDA 2019.3 lub nowsza.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Added input help messages for remainig time command (NVDA+Shift+R).
* Toggle command announcement command (NVDA+Shift+C) will now show up under
  "GoldWave" category in NVDA's input gestures dialog.

## Wersja 20.01

* Wymaga wersji NVDA 2019.3 lub nowszej.

## Wersja 19.11

* Windows 7 SP1, GoldWave 6.x, i NVDA 2019.1 i nowsze są wymagane.
* Dodano wiadomość kontekstową doa okna dźwięku (dostępne jeśli dodatek
  Control usage assistant jest zainstalowany).

## wersja 18.12

* NVDA już nie będzie odtwarzała dźwięk tonu lub robiła nic gdy niektóre
  polecenia goldwawe są wypełniane z wyłączonym wymawianiem poleceń (może to
  w niektórych sytuacjach dźiwnie działać).
* Zmiany wewnętrzne dla wsparcia nowych wersji NVDA.

## Wersja 18.07

* Naprawiony błąd w którym wiodące zera nie były wyświetlane gdy próbowało
  się dostarczyć pozostały czas dla utworu aktualnego.

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

* Added a command to announce remaining time for the current track
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
