# GoldWave #

* Autores: Joseph Lee e colaboradores do NVDA.
* Baixar [versão estável][1]
* NVDA compatibility: 2022.4 and later

Este módulo de aplicação melhora o acesso e a utilização do editor de áudio
GoldWave.

## Atalhos ##

* NVDA+Shift+C: Alterna a leitura de comandos durante a edição de áudio.
* Control+Shift+P: anuncia a posição da pista actual.
* NVDA+Shift+R: anuncia o tempo restante para a pista que está a ser
  editada.
* Control+NVDA+1: anuncia o canal que está a editar.
* Control+NVDA+2: Anuncia o tamanho total do ficheiro de áudio.
* Control+NVDA+3: anuncia um resumo sobre informação de selecção de áudio.
* Control+NVDA+4: anuncia o nível de zoom.

Para mais informações sobre o GoldWave e seus comandos de teclado, consultar
o Manual do GoldWave.

Nota: O GoldWave 6 ou posterior é necessário.

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

* É necessário o NVDA 2021.2 ou posterior devido a alterações do NVDA que
  afectam este extra.
* No GoldWave 6.57 e posteriores, o NVDA deixará de repetir o nome do
  ficheiro carregado ao pressionar as teclas tocar/retroceder/parar.

## Versão 21.06

* Resolvidas questões adicionais de estilo de codificação e potenciais bugs
  com Flake8.

## Versão 20.06

* Resolvidos vários problemas de estilo de codificação e potenciais bugs com
  Flake8.

## Versão 20.04

* Adicionadas mensagens de ajuda de entrada para o comando de tempo restante
  (NVDA+Shift+R).
* O comando "alternar anúncio de comandos" (NVDA+Shift+C) irá agora aparecer
  na categoria "GoldWave" no diálogo definir comandos do NVDA.

## Versão 20.01

* Requer o NVDA 2019.3 ou posterior.

## Versão 19.11

* São necessários o Windows 7 SP1, o GoldWave 6.x, e o NVDA 2019.1 ou
  posteriores.
* Adicionada mensagem de ajuda para janela de som (acessível se o add-on
  Control Usage Assistant estiver instalado).

## Versão 18.12

* O NVDA deixará de parecer não fazer nada ou de tocar os tons de erro ao
  executar certos comandos do GoldWave com o anúncio de comando activado
  (isto pode resultar em comportamentos estranhos em alguns casos).
* Alterações internas para apoiar futuros lançamentos do NVDA.

## Versão 18.07

* Corrigido um problema em que os zeros iniciais não eram mostrados ao
  tentar obter o tempo restante para uma pista.

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

* Adicionado um comando para anunciar o tempo restante para a pista actual
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

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
