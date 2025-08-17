# GoldWave #

* Autores: Joseph Lee, colaboradores da NVDA.

Observação: Eu (Joseph Lee) estou procurando pessoas que farão a manutenção do complemento GoldWave a partir de 1º de abril de 2022.

Este módulo de aplicativo aprimora o acesso e o uso do editor de áudio GoldWave.

## Atalhos ##

Todos os comandos suportam o modo de fala sob demanda.

* Control+Shift+P: Anuncia a posição atual da trilha.
* NVDA+Shift+R: Anuncia o tempo restante da trilha em edição no momento.
* Controle+NVDA+1: Anuncia o canal que está sendo editado.
* Control+NVDA+2: Anuncia a duração total do arquivo de áudio.
* Control+NVDA+3: anuncia um resumo das informações de seleção de áudio.
* Control+NVDA+4: Anuncia o nível de zoom.

Para obter mais informações sobre o GoldWave e os comandos de teclado, consulte o Manual do GoldWave.

Observação: é necessário o GoldWave 6 ou posterior e o Windows 10 ou posterior.

## Versão 25.07

* Tornou o código do complemento mais robusto com a ajuda do Pyright (um verificador de tipos estáticos do Python).
* Anúncios aprimorados de seleção de áudio, nível de zoom e posição da trilha no GoldWave 7.

## Versão 25.04

* Removido o modo de anúncio de comando, substituído pelo modo de fala sob demanda. No modo de fala sob demanda, os comandos específicos do GoldWave, como a definição do marcador de início, permanecerão em silêncio, enquanto os comandos informativos, como a posição do áudio, serão falados.

## Versão 25.02

* É necessário o NVDA 2024.1 ou posterior.
* Suporte limitado restaurado para o Windows 8.1.

## Versão 25.01

* Suporte para GoldWave 7 (requer Windows 10 de 64 bits ou posterior).
* Os links de download para versões de complemento não estão mais incluídos na documentação do complemento. Você pode fazer o download do complemento na loja de complementos do NV Access.
* Mudança da ferramenta de linting do Flake8 para o Ruff e reformatação dos módulos complementares para melhor alinhamento com os padrões de codificação do NVDA.
* Removido o suporte ao recurso de atualizações automáticas de complementos do complemento Add-on Updater.

## Versão 23.02

* É necessário o NVDA 2022.4 ou posterior.
* É necessário o Windows 10 21H2 (atualização/compilação 19044 de novembro de 2021) ou posterior.

## Versão 23.01

* É necessário o NVDA 2022.3 ou posterior.
* É necessário ter o Windows 10 ou posterior, pois o Windows 7, 8 e 8.1 não serão mais suportados pela Microsoft a partir de janeiro de 2023.

## Versão 22.03

* É necessário o NVDA 2021.3 ou posterior.
* Uma mensagem de aviso será exibida ao tentar instalar o complemento no Windows 7, 8 e 8.1.

## Versão 21.10

* O NVDA 2021.2 ou posterior é necessário devido a alterações no NVDA que afetam esse complemento.
* No GoldWave 6.57 e posterior, o NVDA não repetirá mais o nome do arquivo carregado ao pressionar as teclas de reprodução/retrocesso/parada.

## Versão 21.06

* Resolvidos outros problemas de estilo de codificação e possíveis bugs com o Flake8.

## Versão 20.06

* Resolvidos vários problemas de estilo de codificação e possíveis bugs com o Flake8.

## Versão 20.04

* Adição de mensagens de ajuda de entrada para o comando remainig time (NVDA+Shift+R).
* O comando de anúncio de comando de alternância (NVDA+Shift+C) agora aparecerá na categoria "GoldWave" na caixa de diálogo de gestos de entrada do NVDA.

## Versão 20.01

* Requer NVDA 2019.3 ou superiores.

## Versão 19.11

* É necessário o Windows 7 SP1, o GoldWave 6.x e o NVDA 2019.1 ou posterior.
* Adicionada mensagem de ajuda para a janela de som (acessível se o complemento Control Usage Assistant estiver instalado).

## Versão 18.12

* O NVDA não parecerá mais não fazer nada ou reproduzir tons de erro ao executar determinados comandos do GoldWave com o anúncio de comando definido como desativado (isso pode resultar em comportamentos estranhos em alguns casos).
* Alterações internas para dar suporte a futuras versões do NVDA.

## Versão 18.07

* Foi corrigido um problema em que os zeros à esquerda não eram exibidos quando se tentava obter o tempo restante de um trakc.

## Versão 17.05

* Foi adicionada a capacidade de fornecer informações de depuração quando o NVDA estiver em execução com o registro de depuração ativado (NVDA 2017.1 ou posterior).
* Traduções atualizadas.

## Versão 16.12

* O esquema de versão agora é ano.mês em vez de maior.menor.

## Alterações para a versão 4.0

* O repositório de complementos foi transferido para o GitHub (agora localizado em https://github.com/josephsl/goldwave).
* Melhorias no desempenho ao procurar informações como o nome do canal e outras informações de status.

## Alterações para a versão 3.0

* Foi adicionado um comando para anunciar o tempo restante da faixa atual (NVDA+Shift+R).
* Pequenas melhorias ao anunciar informações de status, como informações de canal.

## Alterações para a versão 2.0

* Suporte ao GoldWave 6, incluindo a versão de 64 bits do GoldWave (consulte a nota acima).
* A ajuda do complemento agora pode ser acessada no gerenciador de complementos (NVDA 2014.3 e posterior).
* O NVDA agora anuncia o canal selecionado se você pressionar comandos de seleção de canal, como Control+Shift+L para o canal esquerdo.
* Vários problemas com campos de edição numérica, como o campo de censura e o seletor de tempo na caixa de diálogo de mixagem, foram corrigidos, incluindo a seleção de texto, a atualização de valores e assim por diante.
* A configuração do anúncio de comando será lembrada ao alternar para outros programas.

## Alterações para a versão 1.2

* Foi corrigido um problema em que o NVDA tinha dificuldade para anunciar alguns campos de edição.
* Traduções novas e atualizadas.
* Observe que, devido a alterações recentes no NVDA, a seleção de áudio e outros comandos de status podem não funcionar como esperado em alguns sistemas.

## Alterações para a versão 1.1

* Suporte para anúncios de mensagens em braile.
* O resumo da seleção de áudio é apresentado em outros idiomas além do inglês.
* Foram adicionados mais anúncios de comando, incluindo o movimento da posição da deixa e operações de exclusão/aparagem.
* Foi corrigido um problema em campos de edição numérica, como várias caixas de diálogo de efeitos, em que nada ou um nome de campo errado era anunciado.
* Traduções novas e atualizadas.

## Mudanças para a versão 1.0

* Versão inicial.

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
