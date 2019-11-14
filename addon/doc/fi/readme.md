# Goldwave #

* Tekijät: Joseph Lee, NVDA:n tekijät.
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA compatibility: 2019.1 to 2019.2

This app module enhances access and usage of GoldWave audio editor.

## Pikanäppäimet ##

* NVDA+Vaihto+C: Ottaa käyttöön tai poistaa käytöstä äänenmuokkauskomentojen
  puhumisen.
* Control+Vaihto+P: Ilmoittaa nykyisen kohdan raidalla.
* NVDA+Vaihto+R: Ilmoittaa nykyisen raidan jäljellä olevan ajan.
* Control+NVDA+1: Ilmoittaa muokattavan kanavan.
* Control+NVDA+2: Ilmoittaa äänitiedoston kokonaiskeston.
* Control+NVDA+3: Kertoo ääniraidan valitun kohdan yhteenvedon.
* Control+NVDA+4: Ilmoittaa zoomauksen tason.

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

## Versio 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Versio 17.05

* Lisätty mahdollisuus virheenkorjaustietojen tarjoamiseen, kun NVDA:ta
  ajetaan virheenkorjaus-lokitasolla (NVDA 2017.1 tai uudempi).
* Käännöksiä päivitetty.

## Versio 16.12

* Versionumero on nyt muotoa vuosi.kuukausi aiemman suuri.pieni sijaan.

## Muutokset versiossa 4.0

* Lisäosan koodivarasto on muuttanut GitHubiin (sijaitsee nyt osoitteessa
  https://github.com/josephsl/goldwave).
* Suorituskykyä paranneltu tietoja, kuten kanavan nimeä ja muita
  tilatietoja, haettaessa.

## Muutokset versiossa 3.0

* Lisätty komento nykyisen raidan jäljellä olevan ajan ilmoittamiseen
  (NVDA+Shift+R).
* Pieniä parannuksia tilatietoja, kuten kanavaa ilmoitettaessa.

## Muutokset versiossa 2.0

* Tuki GoldWave 6:lle, 64-bittinen versio mukaan lukien (katso huomautus
  edeltä).
* Ohje on käytettävissä Lisäosien hallinnasta (NVDA 2014.3 ja uudemmat).
* NVDA ilmoittaa nyt valitun kanavan painaessasi kanavanvalitsemiskomentoa,
  kuten Control+Shift+L, joka valitsee vasemman.
* Erilaisia numeeristen muokkauskenttien, kuten Censor-äänitehosteen ja
  Mix-valintaikkunan ajanvalitsimen, ongelmia on korjattu, mukaan lukien
  tekstin valitseminen, arvojen päivittäminen jne.
* Komentojenpuhumisasetus säilyy muihin ohjelmiin siirryttäessä.

## Muutokset versiossa 1.2

* Korjattu ongelma, jossa NVDA:lla oli vaikeuksia joidenkin muokkauskenttien
  lukemisessa.
* Uusia ja päivitettyjä käännöksiä.
* Huomaa, että äänen valintaan käytettävät sekä muut tilakomennot eivät ehkä
  toimi odotetusti joissakin järjestelmissä NVDA:han äskettäin tehtyjen
  muutosten vuoksi.

## Muutokset versiossa 1.1

* Tuki ilmoitusten näyttämiselle pistenäytöllä.
* Ääniraidan valitun kohdan yhteenvetotiedot luetaan nyt muillakin kielillä
  kuin englanniksi.
* Lisää komentojen ilmoituksia, paikkamerkin sijainnin siirtäminen sekä
  poisto/leikkaus mukaan lukien.
* Korjattu numeeristen muokkauskenttien ongelma (esim. eri
  äänitehostevalintaikkunoissa), joka aiheutti sen, että väärä kentän nimi
  luettiin tai sitä ei luettu ollenkaan.
* Uusia ja päivitettyjä käännöksiä.

## Muutokset versiossa 1.0

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
