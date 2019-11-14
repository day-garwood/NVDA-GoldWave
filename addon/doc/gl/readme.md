# Goldwave #

* Autores: Joseph Lee, colaboradores do NVDA.
* Descarga [versión estable][1]
* Descarga [versión de desenvolvemento][2]
* NVDA compatibility: 2019.1 to 2019.2

This app module enhances access and usage of GoldWave audio editor.

## Atallos de teclado ##

* NVDA+Shift+C: Cambia a fala das ordes durante a edición do audio.
* Control+Shift+P: Anuncia a posición da pista actual.
* NVDA+Shift+R: Anuncia o tempo restante para a pista actualmente en
  edición.
* Control+NVDA+1: Anuncia a canle que estás a editar.
* Control+NVDA+2: Anuncia a lonxitude total do ficheiro de audio.
* Control+NVDA+3: anuncia un resumo da información da selección do audio.
* Control+NVDA+4: Anuncia o nivel do zoom.

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

## Versión 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

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
