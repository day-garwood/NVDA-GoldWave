# Goldwave #

* Forfattere: Joseph Lee, NVDA bidragydere.
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2017.3 to 2019.2

Dette app-modul forbedrer adgangen til og brugen af lydredigeringsprogrammet
Goldwave. Bemærk: GoldWave-programmet har ikke en dansk sprogpakke
tilgængelig. Derfor er tilføjelsen på nuværende tidspunkt ikke oversat.

## Genveje ##

* NVDA+Skift+C: Slår udtale af kommandoer til og fra under lydredigering.
* Ctrl+Skift+P: Annoncerer aktuelle sporposition.
* NVDA+Skift+R: Annoncerer resterende tid for det spor du er i færd med at
  redigere.
* NVDA+Ctrl+1: Annoncerer kanalen du redigere.
* NVDA+Ctrl+2: Annoncerer den fulde længde af lydfilen.
* Ctrl+NVDA+3: Annoncerer en opsummering af markeringen for den del af
  lydfilen, du har valgt.
* NVDA+Ctrl+4: Annoncere det aktuelle niveau for zoom.

For yderligere oplysninger om Goldwave og tastatur kommandoer, læs
brugervejledningen til Goldwave.

Bemærk: GoldWave 6 kræver 64-bit version af Windows 7 eller senere. NVDA
2014.1 eller nyere kræves for at anvende tilføjelse 2.0.

## Version 18.07

* Løst et problem, hvor ledende nul ikke ville blive vist, når man forsøgte
  at opnå resterende tid for et spor.

## Version 17.05

* Tilføjet mulighed for at give fejlfindingsoplysninger, når NVDA kører med
  logføring aktiveret (NVDA 2017.1 eller senere).
* Opdaterede oversættelser.

## Version 16.12

* Versionsordning er nu year.month i stedet for major.minor.

## Ændringer i 4.0

* Depotet til tilføjelsen er flyttet til GitHub (nu placeret på
  https://github.com/josephsl/goldwave).
* Ydelsesforbedringer, når du slår op information som kanalnavn og anden
  statusinformation.

## Ændringer i 3.0

* Tilføjet en kommando til at annoncere resterende tid for det aktuelle spor
  (NvDA+Skift+R).
* Små forbedringer når NVDA annoncerer statusoplysninger såsom
  kanaloplysninger.

## Ændringer i 2.0

* Understøttelse for GoldWave 6, herunder 64-bit version af GoldWave (se
  bemærkning ovenfor).
* Hjælp til tilføjelsen kan nu tilgås ved hjælp fra dialogen "Styring af
  tilføjelsesprogrammer" (NVDA 2014.3 og nyere).
* NVDA annoncerer nu den valgte kanal, hvis du trykker på
  kanalvalgskommandoer som Ctrl+Skift+L for den venstre kanal.
* Forskellige problemer med numeriske redigere felter som censor felt og
  time selector i mix dialog er blevet rettet, herunder valg af tekst,
  opdatering værdier, osv.
* Indstilling til annoncering af kommandoer vil blive husket, når der
  skiftes til andre programmer.

## Ændringer i 1.2

* Rettede et problem, hvor NVDA havde svært ved at annoncere nogle
  editfelter.
* Nye og opdaterede oversættelser.
* Bemærk venligst at på grund af de seneste ændringer i NVDA, vil kommandoer
  til valg af lyd og statuskommandoer ikke nødvendigvis fungerer korrekt på
  nogle systemer.

## Ændringer i 1.1

* Understøtter meddelelser på punkt, når informationer annonceres.
* Opsummeringer af den markerede del af lydfilen vil nu blive præsenteret i
  andre sprog udover engelsk.
* Flere kommandomeddelelser tilføjet, herunder bevægelser af
  startmarkeringer samt beskæring og sletning.
* Rettede et problem i flere redigeringsfelter, såsom forskellige
  effect-dialoger hvor intet eller forkert feltnavn blev annonceret.
* Nye og opdaterede oversættelser.

## Ændringer i 1.0

* Første version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
