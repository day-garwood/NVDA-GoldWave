# Goldwave #

* Yazarlar: Joseph Lee, NVDA katkıda bulunanlar.
* Download [stable version][1]
* Download [development version][2]

Bu uygulama modülü GoldWave ses editörünün erişilebilirliğini ve kullanımını
geliştirir.

## Kısayollar ##

* NvDA+Shift+C: Düzenlerken komutların seslendirilmesiyle ilgili ayarı açıp
  kapatır.
* Control+Shift+P: Geçerli parçadaki pozisyonu söyler.
* NVDA+Shift+R: Announces remaining time for the currently editing track.
* Control+NVDA+1: Düzenlediğiniz kanalı söyler.
* Control+NVDA+2: Ses dosyasının toplam uzunluğunu söyler.
* Control+NvDA+3: ses seçimiyle ilgili özet bilgi verir.
* Control+NVDA+4: Yakınlaştırma düzeyini söyler.

GoldWave ve klavye komutları hakkında daha fazla bilgi için, GoldWave
kılavuzuna bakın.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. NVDA 2014.1
or later is required to use add-on 2.0.

## Version 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a track.

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
  (NvDA+Shift+R).
* Slight improvements when announcing status information such as channel
  information.

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
* Yeni ve güncel çeviriler.
* Please note that due to recent changes in NVDA, audio selection and other
  status commands may not work as expected in some systems.

## 1.1 için değişiklikler

* Mesaj bildirimi için braille desteği.
* Ses seçimi özeti İngilizce dışındaki dillerde de sunuluyor.
* İşaret noktaları, silme ve kırpma gibi işlemler için daha fazla komut
  bildirimi eklendi
* Fixed an issue in numeric edit fields such as various effects dialogs
  where nothing or wrong field name was announced.
* Yeni ve güncel çeviriler.

## 1.0 için değişiklikler

* İlk sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
