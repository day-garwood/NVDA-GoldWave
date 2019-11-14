# गोल्डवेभ #

* लेखकहरू: जोसेफ ली, नेत्रवाणी योगदान कर्ताहरू
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.1 to 2019.2

This app module enhances access and usage of GoldWave audio editor.

## द्रुतमार्ग ##

* नेत्रवाणी+Shift+C: ध्वनी सम्पादन गर्दा आदेश वाचनको  साटोफेरो गर्छ ।
* Control+Shift+P: हालको ट्याकको स्थान बताउने छ ।
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+नेत्रवाणी+1: तपाइले सम्पादन गर्दै गरेको च्यानेल बताउने छ ।
* Control+नेत्रवाणी+2: ध्वनी फाइलको कूल लम्वाई बताउने छ ।
* Control+नेत्रवाणी+3: ध्वनि चयनको शारांश बताउने छ ।
* Control+नेत्रवाणी+4: अभिवर्धनको स्तर बताउने छ ।

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this
add-on, NVDA 2019.1 or later is required.

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

## ३.० मा गरिएका परिवर्तनहरू

* Added a command to announce remaining time for the current track
  (NvDA+Shift+R).
* Slight improvements when announcing status information such as channel
  information.

## २.० संस्करणमा गरिएका परिवर्तनहरू

* Support for GoldWave 6, including 64-bit version of GoldWave (see note
  above).
* Add-on help can now be accessed from add-ons manager (NVDA 2014.3 and
  later).
* NVDA now announces selected channel if you press channel selection
  commands such as Control+Shift+L for the left channel.
* Various issues with numeric edit fields such as censor field and time
  selector in mix dialog has been fixed, including selecting text, updating
  values and so on.
* Command announcement setting will be remembered when switching to other
  programs.

## १.2 मा गरिएका परिवर्तनहरू

* कुनै सम्पादन भूमीमा नेत्रवाणीलाई घोषणा गर्न कठिनाई भएको मुद्दा समाधान
  गरियो ।
* नया र अद्यावधिक अनुवादहरू
* कृपया ख्याल राखौं कि हालै नेत्रवाणीमा गरिएको परिवर्तनका कारण केही
  पर्णालीमा श्रव्य चयन र अरू आदेशहरूले सोचे जस्तो काम नगर्न सक्छन् ।

## १.1 मा गरिएका परिवर्तनहरू

* ब्रेलमा सन्देसको घोषणालाई समर्थन गर्छ ।
* श्रव्य चयन सारांस अङ्ग्रेजी भन्दा अरू भाषामा पनि प्रस्तुत हुन्छ ।
* क्यु स्थान र कटाइ/मेटाइ स्थान सहित अन्य आदेस घोषणा थप गरियो ।  
* Fixed an issue in numeric edit fields such as various effects dialogs
  where nothing or wrong field name was announced.
* नया र अद्यावधिक अनुवादहरू

## १.० मा गरिएका परिवर्तनहरू

* शुरूको संस्करण

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
