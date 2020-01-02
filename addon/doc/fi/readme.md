# Goldwave #

* Tekijät: Joseph Lee, NVDA:n tekijät.
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* Yhteensopivuus: NVDA 2019.3 ja uudemmat
* Lataa [vanhempi versio,][3] joka on yhteensopiva NVDA 2019.2.1:n ja sitä
  vanhempien kanssa

Tämä sovellusmoduuli parantaa GoldWave-äänimuokkaimen saavutettavuutta ja
käytettävyyttä.

## Pikanäppäimet ##

* NVDA+Vaihto+C: Ottaa käyttöön tai poistaa käytöstä äänenmuokkauskomentojen
  puhumisen.
* Control+Vaihto+P: Ilmoittaa nykyisen kohdan raidalla.
* NVDA+Vaihto+R: Ilmoittaa nykyisen raidan jäljellä olevan ajan.
* Control+NVDA+1: Ilmoittaa muokattavan kanavan.
* Control+NVDA+2: Ilmoittaa äänitiedoston kokonaiskeston.
* Control+NVDA+3: Kertoo ääniraidan valitun kohdan yhteenvedon.
* Control+NVDA+4: Ilmoittaa zoomauksen tason.

Lisätietoja GoldWavesta sekä sen näppäinkomennoista on ohjelman
käsikirjassa.

Huom: GoldWave 6 vaatii Windows 7:n 64-bittisen version tai uudemman. Tämän
lisäosan käyttämiseen tarvitaan NVDA 2019.3 tai uudempi.

## Versio 20.01

* Vaatii NVDA 2019.3:n tai uudemman.

## Versio 19.11

* Windows 7 SP1, GoldWave 6.x ja NVDA 2019.1 tai uudempi vaaditaan.
* Lisätty ohjeviesti ääni-ikkunalle (käytettävissä, mikäli Säätimen
  käyttöapu -lisäosa on asennettuna).

## Versio 18.12

* NVDA ei enää näytä olevan tekemättä mitään tai toista virheääniä tiettyjä
  GoldWave-komentoja suoritettaessa, kun komentojen puhuminen on poistettu
  käytöstä (tämä voi johtaa joissakin tapauksissa outoon käyttäytymiseen).
* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

## Versio 18.07

* Korjattu ongelma, jossa etunollia ei näytetty yritettäessä hakea raidan
  jäljellä olevaa aikaa.

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

[3]: https://addons.nvda-project.org/files/get.php?file=gwv-2019
