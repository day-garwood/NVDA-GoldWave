# GoldWave #

* Автори: Joseph Lee, учасники спільноти NVDA.
* Завантажити [стабільну версію][1]
* NVDA compatibility: 2021.2 and beyond

This app module enhances access and usage of GoldWave audio editor.

## Гарячі клавіші ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: Повідомити поточну позицію трека.
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+NVDA+1: Оголошує канал, який ви редагуєте.
* Control+NVDA+2: Оголошує загальну довжину аудіофайла.
* Control+NVDA+3: announces a summary on audio selection information.
* Control+NVDA+4: Оголошує рівень.

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

## Version 17.05

* Added ability to provide debug information when NVDA is running with debug
  logging enabled (NVDA 2017.1 or later).
* Updated translations.

## Version 16.12

* Version scheme is now year.month instead of major.minor.

## Changes for 4.0

* Add-on repository has moved to GitHub (now located at
  https://github.com/josephsl/goldwave).
* Performance improvements when looking up information such as channel name
  and other status information.

## Changes for 3.0

* Added a command to announce remaining time for the current track
  (NVDA+Shift+R).
* Slight improvements when announcing status information such as channel
  information.

## Зміни у версії 2.0

* Підтримка GoldWave 6, включно з 64-бітними версіями програми
  (див. примітку вище).
* Починаючи з версії NVDA 2014.3, довідка додатка доступна у диспетчері
  додатків.
* NVDA тепер повідомляє про вибраний канал при натисканні команди вибору
  каналу, наприклад, Control+Shift+L для лівого каналу.
* Були виправлені різні проблеми з числовими полями редагування, такі як
  поле цензури і виділення часу в діалозі міксування, в тому числі виділення
  тексту, оновлення значень і так далі.
* Налаштування оголошень команд запам'ятовується при перемиканні на інші
  програми.

## Зміни у версії 1.2

* Виправлено помилку, коли NVDA з проблемами промовляла деякі поля
  редагування.
* Нові та оновлені переклади.
* Будь ласка,, зверніть увагу, що у зв'язку з останніми змінами в NVDA,
  виділення аудіо та інші команди стану можуть не працювати належни чином на
  деяких системах.

## Зміни у версії 1.1

* Підтримка оголошення повідомлень за допомогою брайля.
* Сумарне оголошення виділеної звукової інформації доступне мовами,
  відмінними від англійської.
* Додано більше команд оголошень, включно з переміщенням положення мітки і
  операцій видалення/обрізання.
* Виправлено проблему з числовыми полями редагування, наприклад, у різних
  діалогах ефектів, коли не оголошувалося нічого або неправильні назви
  полів.
* Нові та оновлені переклади.

## Зміни у версії 1.0

* Перша версія.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv
