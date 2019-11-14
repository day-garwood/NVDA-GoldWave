# Goldwave #

* Autores: Joseph Lee, colaboradores do NVDA.
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* NVDA compatibility: 2019.1 to 2019.2

This app module enhances access and usage of GoldWave audio editor.

## Atalhos: ##

* NVDA+Shift+C: Alterna a fala de comandos durante a edição de áudio.
* Control+Shift+P: Anuncia a posição na faixa atual.
* NVDA+Shift+R: Anuncia o tempo restante da faixa atualmente em edição.
* Control+NVDA+1: Anuncia o canal que se está editando.
* Control+NVDA+2: Anuncia o comprimento total do arquivo de áudio.
* Control+NVDA+3: Anuncia um resumo com informações da seleção de áudio.
* Control+NVDA+4: Anuncia o nível de zum.

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

## Versão 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Versão 17.05

* Adicionada capacidade de fornecer informações de depuração quando o NVDA
  está sendo executado com o log de depuração ativado (NVDA 2017.1 ou
  posterior).
* Traduções atualizadas.

## Versão 16.12

* O esquema de versão agora é ano.mês ao invés de maior.menor.

## Mudanças na 4.0

* Movido o repositório do complemento para o GitHub (agora localizado em
  https://github.com/josephsl/goldwave).
* Melhorias de desempenho ao verificar informações como nome do canal e
  outras informações de status.

## Mudanças na 3.0

* Adicionado comando para anunciar o tempo restante da faixa atual
  (NVDA+Shift+R).
* Ligeira melhoria ao anunciar informações de status, tais como informações
  de canal.

## Mudanças na 2.0

* Suporte ao GoldWave 6, incluindo a versão 64-bit do GoldWave (ver nota
  acima).
* A ajuda do complemento pode ser agora acessada do gestor de complementos
  (NVDA 2014.3 e posterior).
* O NVDA agora anuncia o canal selecionado se você pressiona comandos de
  seleção de canais, como Control+Shift+L para o canal esquerdo.
* Foram corrigidos vários problemas com campos numéricos de edição, como o
  campo de censor e o seletor de tempo no diálogo de mixagem, incluindo
  selecionar texto, atualizar valores e outros.
* As definições de anúncio de comando serão lembradas ao trocar para outros
  programas

## Mudanças na 1.2

* Corrigido um problema com o qual o NVDA encontrava dificuldades ao
  anunciar alguns campos de edição.
* Novas e atualizadas traduções.
* Por favor note que, devido a mudanças recentes no NVDA, a seleção de
  áudioi e outros comandos de status podem não funcionar como esperado em
  alguns sistemas.

## Mudanças na 1.1

* Suporte a anúncios de mensagens em braille.
* O resumo da seleção de áudio é apresentado noutros idiomas além de Inglês.
* Adicionados novos anúncios de comandos incluindo movimentos na posição da
  divisão e operações de apagamento/exclusão.
* Corrigido um problema em campos numéricos de edição, como em vários
  diálogos de efeitos, nos quais nada era anunciado ou então um nome de
  campo errado.
* Novas e atualizadas traduções.

## Mudanças na 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
