# GoldWave #

* Autores: Joseph Lee, colaboradores de NVDA.

Este módulo de aplicación mejora el acceso y el uso del editor  de audio
Goldwave.

## Atajos de teclado ##

Todas las órdenes soportan el modo de voz a petición.

* Control+Shift+P: Anuncia la posición de la pista actual.
* NVDA+Shift+R: Anuncia el tiempo restante para la pista actualmente en
  edición.
* Control+NVDA+1: Anuncia el canal que estás editando.
* Control+NVDA+2: Anuncia la longitud total del archivo de audio.
* Control+NVDA+3: anuncia un resumen de la información de selección de
  audio.
* Control+NVDA+4: Anuncia el nivel de zoom.

Para obtener más información acerca de Goldwave y de las órdenes de teclado,
remítete al manual de Goldwave.

Nota: se requiere GoldWave 6 o posterior y Windows 10 o posterior.

## Versión 25.07

* Se ha hecho el código del complemento más robusto con la ayuda de Pyright
  (un comprobador de tipado estático en Python).
* Se han mejorado los anuncios de selección de audio, nivel de zoom y
  posición en la pista en Goldwave 7.

## Versión 25.04

* Se ha eliminado el modo de anuncio de órdenes, sustituido por el modo de
  voz a petición. En el modo de voz a petición, las órdenes específicas de
  GoldWave, como situar el marcador de inicio, permanecerán en silencio,
  mientras que las órdenes informativas, como posición de audio, se
  verbalizarán.

## Versión 25.02

* Se requiere NVDA 2024.1 o posterior.
* Se restaura un soporte limitado para Windows 8.1.

## Versión 25.01

* Soporte para GoldWave 7 (requiere Windows 10 de 64 bits o posterior).
* Ya no se incluyen enlaces de descarga de versiones del complemento en su
  documentación. Puedes descargar el complemento desde la tienda de
  complementos de NVDA.
* Se cambia la herramienta de calidad del código de Flake8 a Ruff y se
  reformatean los módulos del complemento para alinearse mejor con los
  estándares de codificación de NVDA.
* Se elimina el soporte de actualizaciones automáticas del complemento
  Add-on Updater.

## Versión 23.02

* Se requiere NVDA 2022.4 o posterior.
* Se requiere Windows 10 21H2 (actualización de noviembre de 2021 /
  compilación 19044) o posterior.

## Versión 23.01

* Se requiere NVDA 2022.3 o posterior.
* Se requiere Windows 10 o posterior, ya que Microsoft no soporta Windows 7,
  8 y 8.1 a partir de enero de 2023.

## Versión 22.03

* Se requiere NVDA 2021.3 o posterior.
* Se mostrará un mensaje de aviso al intentar instalar el complemento en
  Windows 7, 8 y 8.1.

## Versión 21.10

* Se requiere NVDA 2021.2 o posterior a causa de cambios en NVDA que afectan
  a este complemento.
* En GoldWave 6.57 y posterior, NVDA ya no repetirá el nombre del archivo
  cargado al pulsar las teclas de reproducir/pausar/rebobinar.

## Versión 21.06

* Se han resuelto problemas adicionales de estilo del código y fallos
  potenciales con Flake8.

## Versión 20.06

* Se han resuelto muchos problemas de estilo del código y fallos potenciales
  con Flake8.

## Versión 20.04

* Se han añadido mensajes de ayuda de entrada para la orden de tiempo
  restante (NVDA+shift+r).
* La orden para conmutar la verbalización de órdenes (NVDA+shift+c) ahora se
  mostrará bajo la categoría "GoldWave" en el diálogo Gestos de entrada de
  NVDA.

## Versión 20.01

* Se requiere NVDA 2019.3 o posterior.

## Versión 19.11

* Son necesarios Windows 7 SP1, GoldWave 6.x, y NVDA 2019.1 o posterior.
* Se ha añadido un mensaje de ayuda para la ventana de sonido (accesible si
  está instalado Control Usage Assistant).

## Versión 18.12

* NVDA ya no parecerá no hacer nada o reproducirá tonos de error al realizar
  ciertas órdenes de GoldWave con el anuncio de órdenes desactivado (podría
  causar un comportamiento defectuoso en ciertos casos).
* Cambios internos para dar soporte a versiones futuras de NVDA.

## Versión 18.07

* Solucionado un error por el que los ceros a la izquierda no se mostraban
  al intentar obtener el tiempo restante para una pista.

## Versión 17.05

* Añadida la capacidad de proporcionar información de depuración cuando NVDA
  está en ejecución con el registro de depuración habilitado (NVDA 2017.1 o
  posterior).
* Traducciones actualizadas.

## Versión 16.12

* El esquema de la versión ahora es año.mes en lugar de mayor.menor.

## Cambios para 4.0

* El repositorio del complemento se ha movido a GitHub (ahora localizado en
  https://github.com/josephsl/goldwave).
* Mejoras de rendimiento al buscar información tal como nombre de canal y
  otra información de estado.

## Cambios para 3.0

* Añadida una orden para anunciar el tiempo restante para la pista actual
  (NVDA+Shift+R).
* Ligeras mejoras al anunciar información de estado tal como la información
  de canal.

## Cambios para  2.0

* Soporte para GoldWave 6, incluyendo la versión de 64 bits de GoldWave
  (mira la nota arriba).
* Ahora se puede acceder a la ayuda del complemento desde el Administrador
  de complementos (NVDA 2014.3 y posterior).
* NVDA ahora anuncia canal seleccionado si pulsas órdenes de selección de
  canal, tales como Control + Shift + L para el canal izquierdo .
* Se han solucionado varios problemas con campos de edición numéricos como
  el campo censor y el selector de tiempo en el diálogo de mezcla,
  incluyendo la selección de texto , los valores de la actualización y así
  sucesivamente .
* La opción de la orden de anunciado se recordará al cambiar a otros
  programas.

## Cambios para 1.2

* Se ha solucionado un problema por el que NVDA tenía dificultades
  anunciando algunos campos de edición.
* Traducciones nuevas y actualizadas.
* Por favor ten en cuenta que debido a cambios recientes en NVDA, la
  selección de audio y otras órdenes de estado podrían no funcionar como se
  esperaba en algunos sistemas.

## Cambios para 1.1

* Soporte para anunciado de mensajes en braille.
* El resumen de la selección del audio se  presenta en más idiomas que el
  inglés.
* Añadido más anunciado de órdenes incluyendo posición del movimiento del
  indicador y operaciones de borrado/recorte.
* Solucionado un problema en los campos de edición numéricos tales como
  diversos cuadros de diálogo de efectos , donde no se anunciaba nada o
  nombres de campo equivocados.
* Traducciones nuevas y actualizadas.

## Cambios para 1.0

* Versión inicial.

[1]: https://www.nvaccess.org/addonStore/legacy?file=goldwave
