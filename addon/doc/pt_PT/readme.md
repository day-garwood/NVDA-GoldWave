# Goldwave #

* Autores: Joseph Lee e colaboradores do NVDA.
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]

Este módulo do aplicativo melhora o acesso e o uso do editor de áudio
Goldwave.

## Atalhos ##

* NvDA+Shift+C: Alterna a fala de comandos durante a edição de áudio.
* Control+Shift+P: anuncia a posição da pista actual.
* NVDA+Shift+R: anuncia o tempo restante para a pista que está a ser
  editada.
* Control+NVDA+1: anuncia o canal que está a editar.
* Control+NVDA+2: Anuncia o tamanho total do ficheiro de áudio.
* Control+NVDA+3: anuncia um resumo das informações da selecção de áudio.
* Control+NVDA+4: anuncia o nível de zoom.

Para obter mais informações sobre o Goldwave e os comandos do teclado,
consulte o Manual do Goldwave.

Nota: O GoldWave 6 requer uma versão de 64 bits do Windows 7 ou posterior. O
NVDA 2014.1 ou posterior é necessário para usar o add-on 2.0.

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

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev
