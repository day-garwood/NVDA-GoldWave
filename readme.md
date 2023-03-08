# GoldWave #

* Authors: Joseph Lee, NVDA contributors.
* Download [stable version][1]
* NVDA compatibility: 2022.4 and later

Note: I (Joseph Lee) am looking for people who will maintain GoldWave add-on from April 1, 2022 onwards.

This app module enhances access and usage of GoldWave audio editor.

## Shortcuts ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: Announces current track position.
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+NVDA+1: Announces the channel you are editing.
* Control+NVDA+2: Announces the total length of the audio file.
* Control+NVDA+3: announces a summary on audio selection information.
* Control+NVDA+4: Announces the zoom level.

For more information about GoldWave and keyboard commands, refer to GoldWave Manual.

Note: GoldWave 6 or later and Windows 10 or later is required.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer supported by Microsoft as of January 2023.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on on Windows 7, 8, and 8.1.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.
* In GoldWave 6.57 and later, NVDA will no longer repeat the name of the loaded file when pressing play/rewind/stop keys.

## Version 21.06

* Resolved additional coding style issues and potential bugs with Flake8.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Added input help messages for remainig time command (NVDA+Shift+R).
* Toggle command announcement command (NVDA+Shift+C) will now show up under "GoldWave" category in NVDA's input gestures dialog.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 19.11

* Windows 7 SP1, GoldWave 6.x, and NVDA 2019.1 or later is required.
* Added help message for sound window (accessible if Control Usage Assistant add-on is installed).

## Version 18.12

* NVDA will no longer appear to do nothing or play error tones when performing certain GoldWave commands with command announcement set to off (this may result in odd behaviors in some cases).
* Internal changes to support future NVDA releases.

## Version 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to obtain remaining time for a trakc.

## Version 17.05

* Added ability to provide debug information when NVDA is running with debug logging enabled (NVDA 2017.1 or later).
* Updated translations.

## Version 16.12

* Version scheme is now year.month instead of major.minor.

## Changes for 4.0

* Add-on repository has moved to GitHub (now located at https://github.com/josephsl/goldwave).
* Performance improvements when looking up information such as channel name and other status information.

## Changes for 3.0

* Added a command to announce remaining time for the current track (NVDA+Shift+R).
* Slight improvements when announcing status information such as channel information.

## Changes for 2.0

* Support for GoldWave 6, including 64-bit version of GoldWave (see note above).
* Add-on help can now be accessed from add-ons manager (NVDA 2014.3 and later).
* NVDA now announces selected channel if you press channel selection commands such as Control+Shift+L for the left channel.
* Various issues with numeric edit fields such as censor field and time selector in mix dialog has been fixed, including selecting text, updating values and so on.
* Command announcement setting will be remembered when switching to other programs.

## Changes for 1.2

* Fixed an issue where NVDA had difficulty announcing some edit fields.
* New and updated translations.
* Please note that due to recent changes in NVDA, audio selection and other status commands may not work as expected in some systems.

## Changes for 1.1

* Support for message announcements in braille.
* Audio selection summary is presented in languages other than English.
* More command announcements added including cue position movement and delete/trim operations.
* Fixed an issue in numeric edit fields such as various effects dialogs where nothing or wrong field name was announced.
* New and updated translations.

## Changes for 1.0

* Initial version.

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
