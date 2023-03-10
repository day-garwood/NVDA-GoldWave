# GoldWave #

* Yazarlar: Joseph Lee, NVDA'ya katkıda bulunanlar.
* [kararlı sürümü][1] indir
* NVDA compatibility: 2022.4 and later

Bu uygulama modülü GoldWave ses editörünün erişilebilirliğini ve kullanımını
geliştirir.

## Kısayollar ##

* NvDA+Shift+C: Düzenlerken komutların seslendirilmesiyle ilgili ayarı açıp
  kapatır.
* Control+Shift+P: Geçerli parçadaki pozisyonu söyler.
* NVDA+Shift+r: şu anda düzenlenen dosyada kalan süreyi söyler
* Control+NVDA+1: Düzenlediğiniz kanalı söyler.
* Control+NVDA+2: Ses dosyasının toplam uzunluğunu söyler.
* Control+NvDA+3: ses seçimiyle ilgili özet bilgi verir.
* Control+NVDA+4: Yakınlaştırma düzeyini söyler.

GoldWave ve klavye komutları hakkında daha fazla bilgi için, GoldWave
kılavuzuna bakın.

Not: GoldWave 6 veya üstü gerekli.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Sürüm 22.03

* NVDA 2021.3 veya üstü gereklidir.
* Eklentiyi Windows 7, 8 ve 8.1'e yüklemeye çalışırken bir uyarı mesajı
  görüntülenecektir.

## Sürüm 21.10

* NVDA'da yapılan ve bu eklentiyi etkileyen değişiklikler nedeniyle NVDA
  2021.2 veya üstü gereklidir.
* GoldWave 6.57 ve sonraki sürümlerde, NVDA oynat/geri sar/durdur tuşlarına
  basıldığında artık yüklenen dosyanın adını tekrar etmez.

## Sürüm 21.06

* Flake8 ile ek kodlama stili sorunları ve olası hatalar çözüldü.

## Versiyon 20.06

* Flake 8 ile ilgili bir çok kodlama biçimi sorunları ve potansiyel hatalar
  düzeltildi.

## Sürüm 20.04

* Kalan zaman komutu için (NVDA+Shift+R) girdi yardım mesajları eklendi.
* Komut bildirimini açıp kapatma komutu (NVDA+Shift+C) NVDA'nın girdi
  hareketleri iletişim kutusunun "GoldWave" kategorisinde görünecek.

## Versiyon 20.01

* NVDA 2019.3 veya daha üst sürümünü gerektirir.

## Versiyon 19.11

* Windows 7 SP1, GoldWave 6.x ve NVDA 2019.1 veya daha üst sürümü gerekir.
* Ses penceresi için yardım mesajı eklendi (kontrol kullanım asistanı
  eklentisi kuruluysa kullanılabilir).

## Versiyon 18.12

* NVDA, komut bildirimi kapalıyken bazı GoldWave komutları kullanıldığında
  hiçbir şey yapmıyormuş gibi görünmeyecek veya hata sesi çalmayacak (bazı
  durumlarda garip davranışlara sebep olabilir).
* Gelecek NVDA versiyonlarını desteklemek için iç değişiklikler.

## Sürüm 18.07

* Parçanın kalan zamanını söylerken öndeki sıfırların söylenmemesi sorunu
  düzeltildi.

## Versiyon 17.05

* NVDA tamir günlük tutma seviyesinde çalışırken tamir bilgisi verme
  özelliği eklendi (NVDA 2017.1 veya daha üst sürümü).
* Yeni ve güncel çeviriler.

## Versiyon 16.12

* Versiyon düzeni büyük versiyon.küçük versiyon yerine yıl.ay olarak
  ayarlandı.

## 4.0 için değişiklikler

* Eklenti deposu GitHub'a taşındı (https://github.com/josephsl/goldwave
  adresinde bulunabilir).
* Kanal adı ve diğer durum bilgilerini edinme konusunda performans
  geliştirmeleri.

## 3.0 için değişiklikler

* Üzerinde bulunulan parçada kalan zamanı söyleme komutu eklendi
  (NVDA+Shift+R).
* Kanal bilgisi gibi durum bilgilerini söyleme konusunda küçük
  geliştirmeler.

## 2.0 için değişiklikler

* GoldWave'in 64-bit sürümü dahil olmak üzere GoldWave 6 desteği (yukarıdaki
  nota bakın).
* Artık eklenti yardımına eklenti yöneticisinden erişilebilir (NVDA 2014.3
  ve daha üst sürümü).
* Sol kanalı seçmek için Control+Shift+L gibi kanal seçme komutları
  kullanıldığında, NVDA seçilen kanalı söylüyor.
* Sansür alanı ve mixleme iletişim kutusundaki zaman seçimi alanı gibi sayı
  içeren yazı alanlarındaki çeşitli sorunlar giderildi. Giderilen sorunlar
  arasında metin seçimi ve değerlerin güncellenmesi gibi sorunlar var.
* Diğer programlara geçiş yapıldığında komut bildirimi ayarı
  sıfırlanmayacak.

## 1.2 için değişiklikler

* NVDA'nın bazı yazı alanlarını tam olarak bildirememe sorunu düzeltildi.
* Yeni ve güncel çeviriler.
* NVDA'da yapılan bazı değişiklikler nedeniyle, bazı sistemlerde ses seçimi
  ve diğer durum komutlarının beklenen şekilde çalışmayacağını unutmayın.

## 1.1 için değişiklikler

* Mesaj bildirimi için braille desteği.
* Ses seçimi özeti İngilizce dışındaki dillerde de sunuluyor.
* İşaret noktaları, silme ve kırpma gibi işlemler için daha fazla komut
  bildirimi eklendi.
* Çeşitli efekt alanlarındaki değerlerin seslendirilmemesi ya da yanlış
  alanların seslendirilmesi gibi sayısal düzenleme alanlarındaki sorunlar
  giderildi.
* Yeni ve güncel çeviriler.

## 1.0 için değişiklikler

* İlk sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
