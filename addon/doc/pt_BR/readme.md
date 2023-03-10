# GoldWave #

* Autores: Joseph Lee, colaboradores do NVDA.
* Baixe a [versão estável][1]
* NVDA compatibility: 2022.4 and later

Este módulo de aplicativo melhora o acesso e o uso do editor de áudio
GoldWave.

## Atalhos ##

* NVDA+Shift+C: Alterna a fala de comandos durante a edição de áudio.
* Control+Shift+P: Anuncia a posição na faixa atual.
* NVDA+Shift+R: Anuncia o tempo restante da faixa atualmente em edição.
* Control+NVDA+1: Anuncia o canal que se está editando.
* Control+NVDA+2: Anuncia o comprimento total do arquivo de áudio.
* Control+NVDA+3: anuncia um resumo das informações de seleção de áudio.
* Control+NVDA+4: Anuncia o nível de zum.

Para mais informações sobre o GoldWave e os comandos de teclado, consulte o
Manual do GoldWave.

Nota: GoldWave 6 ou posterior é necessário.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.

## Versão 21.10

* O NVDA 2021.2 ou posterior é necessário devido a mudanças no NVDA que
  afetam este complemento.
* No GoldWave 6.57 e posteriores, o NVDA não repetirá mais o nome do arquivo
  carregado ao pressionar as teclas reproduzir/retroceder/parar.

## Versão 21.06

* Resolvidos problemas adicionais de estilo de codificação e possíveis
  falhas com Flake8.

## Versão 20.06

* Foram resolvidos muitos problemas de estilo de codificação e possíveis
  erros com o Flake8.

## Versão 20.04

* Adicionadas mensagens de ajuda de entrada para o comando de tempo restante
  (NVDA+Shift+R).
* O comando de alternância de anúncio de comando (NVDA+Shift+C) será exibido
  na categoria "GoldWave" no diálogo Definir comandos do NVDA.

## Versão 20.01

* Requer NVDA 2019.3 ou posterior.

## Versão 19.11

* É necessário o Windows 7 SP1, GoldWave 6.x, e NVDA 2019.1 ou posterior.
* Adicionada mensagem de ajuda para a janela de som (acessível se o
  complemento Assistente para Uso de Controles estiver instalado).

## Versão 18.12

* O NVDA não parece mais fazer nada ou reproduzir sons de erro ao executar
  determinados comandos GoldWave com o aviso de comando desativado (isso
  pode resultar em comportamentos estranhos em alguns casos).
* Alterações internas para dar suporte a versões futuras do NVDA.

## Versão 18.07

* Corrigido um problema em que os zeros iniciais não eram exibidos ao tentar
  obter o tempo restante para uma faixa.

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

* Adicionado um comando para anunciar o tempo restante da faixa atual
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
  programas.

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

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
