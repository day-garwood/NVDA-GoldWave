# GoldWave #

* Tekijät: Joseph Lee, NVDA:n tekijät.
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä sovellusmoduuli parantaa GoldWave-äänimuokkaimen saavutettavuutta ja
käytettävyyttä.

## Pikanäppäimet ##

* NVDA+Shift+C: Ottaa käyttöön tai poistaa käytöstä äänenmuokkauskomentojen
  puhumisen.
* Control+Shift+P: Ilmoittaa nykyisen kohdan ääniraidalla.
* NVDA+Shift+R: Ilmoittaa nykyisen raidan jäljellä olevan ajan.
* Control+NVDA+1: Ilmoittaa muokattavan kanavan.
* Control+NVDA+2: Ilmoittaa äänitiedoston kokonaiskeston.
* Control+NVDA+3: Kertoo ääniraidan valitun kohdan yhteenvedon.
* Control+NVDA+4: Ilmoittaa zoomauksen tason.

Katso GoldWaven käsikirjasta lisätietoja ohjelmasta sekä sen
näppäinkomennoista.

Huomaa, että GoldWave 6 tarvitsee Windows 7:n 64-bittisen version tai
uudemman. Lisäosan 2.0-version käyttämiseen tarvitaan NVDA 2014.1 tai
uudempi.

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
