# GoldWave #

* Autores: Joseph Lee e colaboradores do NVDA.
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* Compatibilidade com NVDA: 2017.3 a 2019.2

This app module enhances access and usage of GoldWave audio editor.

## Atalhos ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: anuncia a posição da pista actual.
* NVDA+Shift+R: anuncia o tempo restante para a pista que está a ser
  editada.
* Control+NVDA+1: anuncia o canal que está a editar.
* Control+NVDA+2: Anuncia o tamanho total do ficheiro de áudio.
* Control+NVDA+3: announces a summary on audio selection information.
* Control+NVDA+4: anuncia o nível de zoom.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this
add-on, NVDA 2019.3 or later is required.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 19.11

* Windows 7 SP1, GoldWave 6.x, and NVDA 2019.1 or later is required.
* Added help message for sound window (accessible if Control Usage Assistant
  add-on is installed).

## Version 18.12

* NVDA will no longer appear to do nothing or play error tones when
  performing certain GoldWave commands with command announcement set to off
  (this may result in odd behaviors in some cases).
* Internal changes to support future NVDA releases.

## Versão 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Versão 17.05

* adicionada a possibilidade de fornecer informações de depuração quando o
  NVDA está a ser executado com log de depuração activado (NVDA 2017.1 ou
  posterior).
* Traduções actualizadas.

## Versão 16.12

* O esquema de versão agora é ano.mês em vez de maior.menor.

## Alterações para 4.0

* O repositório do extra foi movido para o GitHub (agora localizado em
  https://github.com/josephsl/goldwave).
* Melhorias de desempenho ao pesquisar informações como o nome do canal e
  outras informações de estados.

## Alterações para 3.0

* Added a command to announce remaining time for the current track
  (NVDA+Shift+R).
* Pequenas melhorias ao anunciar informações de status, como informações do
  canal.

## Mudanças para 2.0

* Introduzido suporte para o GoldWave 6, incluindo a versão de 64 bits do
  GoldWave (veja a nota acima).
* A ajuda do extra agora pode ser acedida pelo gestor de extras (NVDA 2014.3
  e posterior).
* O NVDA agora anuncia o canal seleccionado se pressionar os comandos de
  seleção de canais, como Control + Shift + L para o canal esquerdo.
* Vários problemas com campos de edição numéricos como o campo de censura e
  o seletor de tempo na caixa de diálogo de mistura foram corrigidos,
  inclusive selecionando texto, atualizando valores e assim por diante.
* A configuração do anúncio de comando será lembrada ao mudar para outros
  programas.

## Alterações para 1.2

* Corrigido um problema em que o NVDA tinha dificuldade em anunciar alguns
  campos de edição.
* Traduções novas e actualizadas
* Por favor, note que devido a mudanças recentes no NVDA, a selecção de
  áudio e outros comandos de status podem não funcionar como esperado em
  alguns sistemas.

## Alterações para 1.1

* Suporte para anúncios de mensagens em braille.
* O resumo da selecção de áudio passa a ser apresentado também em idiomas
  diferentes do inglês.
* Mais anúncios de comandos foram adicionados incluindo movimento de posição
  de sinalização e operações de exclusão / corte.
* Corrigido um problema em campos de edição numéricos, como vários diálogos
  de efeitos onde nada ou nome de campo errado era anunciado.
* Traduções novas e actualizadas

## Alterações para 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
