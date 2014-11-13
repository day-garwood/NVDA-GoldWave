# 골드웨이브 #

* 개발자: 이성원 (Joseph Lee) 외 NVDA 공헌자들.
* Download [stable version][1]
* Download [development version][2]

본 앱마주얼을 설치하여 골드웨이브를 더 손쉽게 사용하실 수 있습니다.

## 단추키 ##

* ㄹontrol+Shift+P: 현 트랙 위치를 알려줍니다.
* Control+NvDA+3: 선택된 오디오에 대한 정보를 알려줍니다.
* Control+NVDA+2: 오디오 파일의 전체 재생 시간을 알려줍니다.
* Control+NVDA+1: 현재 편집중인 오디오 체널을 알려줍니다.
* NvDA+Shift+C: 오디오 편집중 단추키 관련 출력 유무를 설정합니다.
* Control+NVDA+4: 오디오 줌 레벨을 알려줍니다.

골드웨이브에 대한 정보 및 단추키 목록에 대해서는 골드웨이브 사용설명서를 참고하세요.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. NVDA 2014.1
or later is required to use add-on 2.0.

## Changes for 2.0

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

## Changes for 1.2

* Fixed an issue where NVDA had difficulty announcing some edit fields.
* New and updated translations.
* Please note that due to recent changes in NVDA, audio selection and other
  status commands may not work as expected in some systems.

## Changes for 1.1 ##

* Support for message announcements in braille.
* Audio selection summary is presented in languages other than English.
* More command announcements added including cue position movement and
  delete/trim operations.
* Fixed an issue in numeric edit fields such as various effects dialogs
  where nothing or wrong field name was announced.
* New and updated translations.

## 1.0 ##

* 첫 버전.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=gwv

[2]: http://addons.nvda-project.org/files/get.php?file=gwv-dev
