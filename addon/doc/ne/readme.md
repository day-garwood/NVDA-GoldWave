# गोल्डवेभ #

* लेखकहरू: जोसेफ ली, नेत्रवाणी योगदान कर्ताहरू
* Download [stable version][1]
* Download [development version][2]

यो उपकरणले गोल्डवेभ नामक ध्वनी सम्पादकको पहुँच र प्रयोगमा सहजता सिर्जना
गर्ने छ । .

## द्रुतमार्ग ##

* नेत्रवाणी+Shift+C: ध्वनी सम्पादन गर्दा आदेश वाचनको  साटोफेरो गर्छ ।
* Control+Shift+P: हालको ट्याकको स्थान बताउने छ ।
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+नेत्रवाणी+1: तपाइले सम्पादन गर्दै गरेको च्यानेल बताउने छ ।
* Control+नेत्रवाणी+2: ध्वनी फाइलको कूल लम्वाई बताउने छ ।
* Control+नेत्रवाणी+3: ध्वनि चयनको शारांश बताउने छ ।
* Control+नेत्रवाणी+4: अभिवर्धनको स्तर बताउने छ ।

गोल्डवेभ र कुञ्जीपाटी आदेश बारे थप जानकारि लिन   गोल्डवेभ सम्बन्धित
कागजातहरू हेर्नु होला । 

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. NVDA 2014.1
or later is required to use add-on 2.0.

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
