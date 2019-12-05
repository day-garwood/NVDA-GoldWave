# Goldwave #

* Autores: Joseph Lee, colaboradores do NVDA.
* Descarga [versión estable][1]
* Descarga [versión de desenvolvemento][2]
* Compatibilidade con NVDA: da 2019.1 á 2019.2

Este módulo de aplicación mellora o acceso e o uso do editor de audio
GoldWave.

## Atallos de teclado ##

* NVDA+Shift+C: Cambia a fala das ordes durante a edición do audio.
* Control+Shift+P: Anuncia a posición da pista actual.
* NVDA+Shift+R: Anuncia o tempo restante para a pista actualmente en
  edición.
* Control+NVDA+1: Anuncia a canle que estás a editar.
* Control+NVDA+2: Anuncia a lonxitude total do ficheiro de audio.
* Control+NVDA+3: anuncia un resumo da información da selección do audio.
* Control+NVDA+4: Anuncia o nivel do zoom.

Para obter máis información acerca do GoldWave e das ordes do teclado,
consulta o Manual do GoldWave.

Nota: GoldWave 6 require da versión de 64 bits de Windows 7 ou
posterior. Requírese do NVDA 2019.1 ou posterior para utilizar o
complemento.

## Versión 19.11

* Requírese Windows 7 SP1, GoldWave 6.x, e NVDA 2019.1, ou posteriores.
* Engadida mensaxe de axuda para a ventá de son (accesible se o complemento
  Control Usage Assistant está instalado).

## Versión 18.12

* NVDA xa non parecerá non facer nada ni reproducirá tons de erro ao
  executar certas ordes de GoldWave co anunciado de ordes establecido en
  desactivado (isto podería resultar en comportamentos aleatorios en certos
  casos).
* Trocos internos para soportar versións futuras de NVDA.

## Versión 18.07

* Arranxado un erro polo que os ceros á esquerda non se amosaban ó obter o
  tempo restante para unha pista.

## Versión 17.05

* Engadida a capacidade de proporcionar información de depuración cando o
  NVDA está en execución co rexistro de depuración habilitado (NVDA 2017.1
  ou posterior).
* Traduccións actualizadas.

## Versión 16.12

* O esquema da versión agora é ano.mes en lugar de maior.menor.

## Cambios para 4.0

* O repositorio do complemento moviuse a GitHub (localizado agora en
  https://github.com/josephsl/goldwave).
* Melloras de rendemento ao buscar información coma nome do canal e outra
  información de estado.

## Cambios para 3.0

* Engadida unha orden para anunciar o tempo restante para a pista actual
  (NVDA+Shift+R).
* Lixeiras melloras ó anunciar información de estado como a información da
  canle.

## Cambios para 2.0

* Soporte para GoldWave 6, incluíndo versión de 64 bits do GoldWave (mira a
  nota arriba).
* A axuda do complemento agora pode acesarse dende o Administrador de
  Complementos (NVDA 2014.3 e superiores).
* NVDA agora anuncia canle seleccionado se premes ordes de selección de
  canle, como Control+Shift+L para a canle esquerdo.
* Correxíronse varios problemas con campos de edición numéricos, como o
  campo de censor e o selector de tempo no diálogo de mezcla, incluíndo a
  selección de texto , actualización de valores e así por diante.
* A opción da orden de anunciado lembrarase cando se cambie a outros
  programas .

## Cambios para 1.2

* Solucionouse un problema polo que o NVDA tiña dificultades anunciando
  algúns campos de edición.
* Traduccións novas e actualizadas.
* Por favor ten en conta que debido a cambios recentes no NVDA, a selección
  de audio e outras ordes de estado poderían non funcionar  como se esperaba
  nalgúns sistemas.

## Cambios para 1.1

* Soporte para o anunciado de mesaxes en braille.
* O resumo da selección de audio preséntase en máis linguas que no inglés.
* Engádense máis ordes incluindo o anunciado do movemento da posición do
  sinal e operacións de borrado/recorte.
* Correxido un problema en campos de edición numéricos, como varios diálogos
  de efectos nos que non se anunciaba nada ou o nome dos campos incorrectos.
* Traduccións novas e actualizadas.

## Cambios para 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
