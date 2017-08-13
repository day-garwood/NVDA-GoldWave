# Goldwave #

* Autorzy: Joseph Lee, współpracownicy NVDA.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ten dodatek zwiększa dostępność i użyteczność edytora audio Goldwave.

## Skróty ##

* NvDA+Shift+C: przełącza wypowiadanie komend podczas edycji audio.
* Control+Shift+P: odczytuje aktualną pozycję ścieżki.
* NVDA+Shift+R: Oznajmia pozostały czas dla aktualnie edytowanego utworu.
* Control+NVDA+1: wypowiada aktualnie edytowany kanał.
* Control+NVDA+2: wypowiada całkowitą długość pliku dźwiękowego.
* Control+NvDA+3: czyta informacje o aktualnym zaznaczeniu audio.
* Control+NVDA+4: wypowiada aktualny poziom powiększenia.

Więcej informacji o Goldwave i jego klawiszach skrótu, znajduje się w
podręczniku Goldwave.

Uwaga: GoldWave 6 wymaga 64-bitowej wersji Windows 7 lub nowszej. NVDA
2014.1 lub nowsze jest wymagane do używania dodatku 2.0.

## Wersja 16.12

* Schemat wersjonowania został zmienioni i teraz on brzmi rok.miesiąc
  zamiast duży.mniejszy.

## Zmiany dla wersji 4.0

* Repozytorium tego dodatku został przeniesiony na Github (teraz znajdujący
  się pod adresem https://github.com/josephsl/goldwave).
* Ulepszona wydajność przy pobieraniu informacji takich jak nazwa kanału i
  inne informacje statusu.

## Zmiany dla wersji 3.0

* Dodana komenda wypowiadania trwania aktualnego utworu (NvDA+Shift+R).
* Trochę większe ulepszenia czytania informacji stanu takich jak informacji
  o kanale.

## Zmiany dla wersji 2.0

* Wsparcie dla GoldWave 6, włączając w to 64-bitową wersję GoldWave (zobacz
  powyższą uwagę).
* Pomoc dodatku dostępna w managerze dodatków (NVDA 2014.3 and later).
* NVDA oznajmia wybrany kanał po wciśnięciu polecenia zmiany zaznaczonego
  kanału np. Control+Shift+L dla zaznaczenia lewego kanału.
* Rozwiązano różne problemy z edycją pól numerycznych, np. pole cenzora i
  wybór czasu w oknie miksowania, w tym zaznaczanie tekstu, aktualizowanie
  wartości itd.
* Przełącznik oznajmiania komend jest pamiętany po przejściu do innych
  programów.

## Zmiany dla wersji 1.2

* Poprawiono problem, że NVDA miał trudności z odczytywaniem niektórych pól
  edycji.
* Nowe i zaktualizowane tłumaczenia.
* Proszę zwrócić uwagę, że w związku z ostatnimi zmianami w NVDA,
  zaznaczanie audio i inne polecenia statusu mogą nie działać na niektórych
  systemach, tak jak to byłoby oczekiwane.

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
