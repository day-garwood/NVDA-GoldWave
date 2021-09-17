# GoldWave #

* Авторы: Joseph Lee, участники сообщества NVDA.
* Загрузить [стабильную версию][1]
* NVDA compatibility: 2021.2 and beyond

This app module enhances access and usage of GoldWave audio editor.

## Горячие клавиши ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: Объявить текущую позицию дорожки.
* NVDA+Shift+R: Объявляет оставшееся время для текущего редактируемого
  трека.
* Control+NVDA+1: Объявляет канал, который вы редактируете.
* Control+NVDA+2: Объявляет общую длину аудиофайла.
* Control+NVDA+3: announces a summary on audio selection information.
* Control+NVDA+4: Объявляет уровень.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 or later is required.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

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

## Версия 17.05

* Added ability to provide debug information when NVDA is running with debug
  logging enabled (NVDA 2017.1 or later).
* Обновлены переводы.

## Версия 16.12

* Схема версий теперь год.месяц вместо major.minor.

## Изменения для версии 4.0

* Репозиторий дополнения перемещён на GitHub (теперь находится по адресу
  https://github.com/josephsl/goldwave).
* Улучшения производительности при поиске информации, такой как название
  канала и другой информации состояния.

## Изменения для версии 3.0

* Added a command to announce remaining time for the current track
  (NVDA+Shift+R).
* Незначительные улучшения объявлений информации о состоянии, например,
  информацию о канале.

## Изменения для версии 2.0

* Поддержка GoldWave 6, в том числе 64-битной версии GoldWave (см примечание
  выше).
* Справка дополнения доступна в диспетчере дополнений (NVDA 2014.3 и выше).
* NVDA теперь объявляет выбранный канал при нажатии команды выбора канала,
  например Control+Shift+L для левого канала.
* Были исправлены различные проблемы с числовыми полями редактирования,
  такие как поле цензуры и выделение времени в диалоге смешивания, в том
  числе выделение текста, обновление значений и так далее.
* Настройка объявлений команд запоминается при переключении на другие
  программы.

## Изменения для версии 1.2

* Исправлена ошибка, когда NVDA с трудом объявлял некоторые поля
  редактирования.
* Новые и обновлённые переводы.
* Пожалуйста, обратите внимание, что в связи с последними изменениями в
  NVDA, выделение аудио и другие команды состояния могут не работать должным
  образом на некоторых системах.

## Изменения для версии 1.1

* Поддержка объявлений сообщений по брайлю.
* сводное объявление выделеной звуковой информации предоставляется на
  языках, отличных от английского.
* Добавлено больше команд объявлений, включая перемещение положения метки и
  операций удаления/обрезки.
* Исправлена проблема с числовыми полями редактирования, например, в
  различных диалогах эффектов, когда не объявлялось ничего или неправильные
  названия полей.
* Новые и обновлённые переводы.

## Изменения для версии 1.0

* Начальная версия.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv
