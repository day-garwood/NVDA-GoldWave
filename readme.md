# GoldWave #

* Authors: Joseph Lee, NVDA contributors.
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.3 and beyond

This app module enhances access and usage of GoldWave audio editor.

## Shortcuts ##

* NvDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: Announces current track position.
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+NVDA+1: Announces the channel you are editing.
* Control+NVDA+2: Announces the total length of the audio file.
* Control+NvDA+3: announces a summary on audio selection information.
* Control+NVDA+4: Announces the zoom level.

For more information about GoldWave and keyboard commands, refer to GoldWave Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this add-on, NVDA 2019.3 or later is required.

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

* Added a command to announce remaining time for the current track (NvDA+Shift+R).
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

[1]: http://addons.nvda-project.org/files/get.php?file=gwv

[2]: http://addons.nvda-project.org/files/get.php?file=gwv-dev
