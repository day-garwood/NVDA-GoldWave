# GoldWave #

* Tekijät: Joseph Lee, NVDA-yhteisö

Tiedoksi: GoldWave-lisäosa tarvitsee uusia ylläpitäjiä 1.4.2022 alkaen – otathan yhteyttä, jos olet kiinnostunut.

Tämä sovellusmoduuli parantaa GoldWave-äänimuokkaimen saavutettavuutta ja käytettävyyttä.

## Pikanäppäimet ##

Kaikki komennot tukevat "pyydettäessä"-puhetilaa.

* Ctrl+Vaihto+P: Ilmoittaa nykyisen kohdan raidalla.
* NVDA+Vaihto+R: Ilmoittaa nykyisen raidan jäljellä olevan ajan.
* Ctrl+NVDA+1: Ilmoittaa muokattavan kanavan.
* Ctrl+NVDA+2: Ilmoittaa äänitiedoston kokonaiskeston.
* Ctrl+NVDA+3: Antaa yhteenvedon raidan valitun kohdan tiedoista.
* Ctrl+NVDA+4: Ilmoittaa zoomauksen tason.

Lisätietoja GoldWavesta ja sen näppäinkomennoista on sovelluksen käyttöohjeessa.

Huom: Tämä lisäosa edellyttää GoldWave 6:ta tai uudempaa sekä Windows 10:tä tai uudempaa.

## Versio 25.07

* Lisäosan koodin vakautta ja virheensietoa parannettu Pyrightin (Pythonin staattisen tyypintarkistustyökalun) avulla.
* Paranneltu äänen valinnan, zoomaustason ja raidan nykyisen kohdan ilmoituksia GoldWave 7:ssä.

## Versio 25.04

* Komentojen ilmoitustila on korvattu "pyydettäessä"-puhetilalla. Tässä tilassa GoldWaven komennoista, kuten aloitusmerkin määrittämisestä, ei anneta puhepalautetta, mutta tietoa antavat komennot, kuten toistokohdan sijainti, puhutaan.

## Versio 25.02

* Edellyttää NVDA 2024.1:tä tai uudempaa.
* Palautettu rajoitettu tuki Windows 8.1:lle.

## Versio 25.01

* Tuki GoldWave 7:lle (edellyttää 64-bittistä Windows 10:tä tai uudempaa).
* Latauslinkkiä ei enää sisällytetä lisäosan dokumentaatioon. Voit ladata lisäosan NV Accessin lisäosakaupasta.
* Virheidentarkistustyökalu vaihdettu Flake8:sta Ruff:iin ja lisäosamoduulit muotoiltu uudelleen paremmin NVDA:n koodauskäytäntöjä vastaaviksi.
* Poistettu tämän lisäosan automaattisen päivityksen tuki Lisäosien päivittäjä -lisäosasta.

## Versio 23.02

* Edellyttää NVDA 2022.4:ää tai uudempaa.
* Edellyttää Windows 10 21H2:ta (marraskuun 2021 päivitys/koontiversio 19044) tai uudempaa.

## Versio 23.01

* Edellyttää NVDA 2022.3:ea tai uudempaa.
* Edellyttää Windows 10:tä tai uudempaa, koska Microsoft ei enää tue Windows 7:ää, 8:aa tai 8.1:tä tammikuusta 2023 alkaen.

## Versio 22.03

* Edellyttää NVDA 2021.3:ea tai uudempaa.
* Lisäosa näyttää varoituksen yritettäessä asentaa sitä Windows 7:ssä, 8:ssa tai 8.1:ssä.

## Versio 21.10

* Edellyttää NVDA 2021.2:ta tai uudempaa tähän lisäosaan vaikuttavien NVDA-muutosten takia.
* NVDA ei enää toista GoldWave 6.57:ssä ja uudemmissa avatun tiedoston nimeä toista-, kelaa taaksepäin- tai pysäytä-näppäimiä painettaessa.

## Versio 21.06

* Ratkaistu lisää koodaustyylin ongelmia sekä mahdollisia Flake8:aan liittyviä virheitä.

## Versio 20.06

* Ratkaistu useita koodaustyylin ongelmia sekä mahdollisia Flake8:aan liittyviä virheitä.

## Versio 20.04

* Lisätty näppäinohjeviestit jäljellä olevan ajan ilmoittavalle komennolle (NVDA+Vaihto+R).
* Komentojen puhumisen käyttöön ottava tai käytöstä poistava komento (NVDA+Vaihto+C) näkyy nyt GoldWave-kategoriassa NVDA:n Näppäinkomennot-valintaikkunassa.

## Versio 20.01

* Edellyttää NVDA 2019.3:ea tai uudempaa.

## Versio 19.11

* Edellyttää Windows 7 SP1:tä, GoldWave 6.x:ää ja NVDA 2019.1:tä tai uudempaa.
* Lisätty ohjeviesti ääni-ikkunalle (käytettävissä, mikäli Säätimen käyttöapu -lisäosa on asennettuna).

## Versio 18.12

* NVDA ei enää näytä olevan tekemättä mitään tai toista virheääniä tiettyjä GoldWave-komentoja suoritettaessa, kun komentojen puhuminen on poistettu käytöstä (tämä voi johtaa joissakin tapauksissa outoon käyttäytymiseen).
* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

## Versio 18.07

* Korjattu ongelma, jonka takia etunollia ei näytetty yritettäessä hakea raidan jäljellä olevaa aikaa.

## Versio 17.05

* Lisätty mahdollisuus virheenkorjaustietojen tarjoamiseen, kun NVDA:ta käytetään virheenkorjaus-lokitasolla (NVDA 2017.1 tai uudempi).
* Käännöksiä päivitetty.

## Versio 16.12

* Versionumero on nyt muotoa vuosi.kuukausi aiemman suuri.pieni sijaan.

## Muutokset versiossa 4.0

* Lisäosan koodivarasto on muuttanut GitHubiin (sijaitsee nyt osoitteessa https://github.com/josephsl/goldwave).
* Suorituskykyä paranneltu tietoja, kuten kanavan nimeä ja muita tilatietoja, haettaessa.

## Muutokset versiossa 3.0

* Lisätty nykyisen raidan jäljellä olevan ajan ilmoittava komento (NVDA+Vaihto+R).
* Pieniä parannuksia tilatietoja, kuten kanavaa, ilmoitettaessa.

## Muutokset versiossa 2.0

* Tuki GoldWave 6:lle, 64-bittinen versio mukaan lukien (katso huomautus edeltä).
* Ohje on käytettävissä Lisäosien hallinnasta (NVDA 2014.3 ja uudemmat).
* NVDA ilmoittaa nyt valitun kanavan painettaessa kanavan valitsemiskomentoa, kuten Control+Shift+L, joka valitsee vasemman.
* Useita numeeristen muokkauskenttien, kuten Censor-äänitehosteen ja Mix-valintaikkunan ajanvalitsimen, ongelmia on korjattu, mukaan lukien tekstin valitseminen, arvojen päivittäminen jne.
* Komentojen puhumisasetus säilyy muihin sovelluksiin siirryttäessä.

## Muutokset versiossa 1.2

* Korjattu ongelma, jonka takia NVDA:lla oli vaikeuksia joidenkin muokkauskenttien lukemisessa.
* Uusia ja päivitettyjä käännöksiä.
* Huomaa, että NVDA:han äskettäin tehtyjen muutosten vuoksi äänen valintaan käytettävät sekä muut tilakomennot eivät välttämättä toimi normaalisti kaikissa järjestelmissä.

## Muutokset versiossa 1.1

* Tuki ilmoitusten näyttämiselle pistenäytöllä.
* Raidan valitun kohdan yhteenvetotiedot luetaan nyt muillakin kielillä kuin englanniksi.
* Lisää komentojen ilmoituksia, paikkamerkin sijainnin siirtäminen sekä poisto/leikkaus mukaan lukien.
* Korjattu numeeristen muokkauskenttien ongelma (esim. eri äänitehostevalintaikkunoissa), joka aiheutti sen, että väärä kentän nimi luettiin tai sitä ei luettu ollenkaan.
* Uusia ja päivitettyjä käännöksiä.

## Muutokset versiossa 1.0

* Ensimmäinen versio.

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
