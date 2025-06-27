# GoldWave #

* Autores: Joseph Lee, colaboradores do NVDA.

Este módulo de aplicativo melhora o acesso e o uso do editor de áudio
GoldWave.

## Atalhos ##

All commands support speech on demand mode.

* Control+Shift+P: Anuncia a posição na faixa atual.
* NVDA+Shift+R: Anuncia o tempo restante da faixa atualmente em edição.
* Control+NVDA+1: Anuncia o canal que se está editando.
* Control+NVDA+2: Anuncia o comprimento total do arquivo de áudio.
* Control+NVDA+3: anuncia um resumo das informações de seleção de áudio.
* Control+NVDA+4: Anuncia o nível de zum.

Para mais informações sobre o GoldWave e os comandos de teclado, consulte o
Manual do GoldWave.

Note: GoldWave 6 or later and Windows 10 or later is required.

## Version 25.07

* Made the add-on code more robust with help from Pyright (a Python static
  type checker).
* Improved audio selection, zoom level, and track position announcements in
  GoldWave 7.

## Version 25.04

* Removed command announcement mode, replaced with speech on demand mode. In
  speech on demand mode, GoldWave specific commands such as setting start
  marker will stay silent while informational commands such as audio
  position will be spoken.

## Version 25.02

* NVDA 2024.1 or later is required.
* Restored limited support for Windows 8.1.

## Versão 25.01

* Suporte para GoldWave 7 (requer Windows 10 de 64 bits ou posterior).
* Os links de download para versões de complemento não estão mais incluídos
  na documentação do complemento. Você pode fazer o download do complemento
  na loja de complementos da NV Access.
* Mudança da ferramenta de linting do Flake8 para o Ruff e reformatação dos
  módulos complementares para melhor alinhamento com os padrões de
  codificação do NVDA.
* Removido o suporte ao recurso de atualizações automáticas de complementos
  do complemento Add-on Updater.

## Versão 23.02

* É necessário o NVDA 2022.4 ou posterior.
* É necessário o Windows 10 21H2 (atualização/compilação 19044 de novembro
  de 2021) ou posterior.É necessário o Windows 7 SP1, GoldWave 6.x, e NVDA
  2019.1 ou posterior.

## Versão 23.01

* É necessário o NVDA 2022.3 ou posterior.
* É necessário ter o Windows 10 ou posterior, pois o Windows 7, 8 e 8.1 não
  serão mais suportados pela Microsoft a partir de janeiro de 2023.

## Versão 22.03

* É necessário o NVDA 2021.3 ou posterior.
* Uma mensagem de aviso será exibida ao tentar instalar o complemento no
  Windows 7, 8 e 8.1.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=goldwave
