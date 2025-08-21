O renomado técnico Carlo Ancelotti assumiu o comando da Seleção Brasileira e ele precisa de uma ferramenta inteligente para analisar o desempenho individual dos jogadores. Para cada atleta sob sua observação, Ancelotti deseja ter um registro detalhado que auxilie a comissão técnica a tomar decisões estratégicas sobre escalação, treinamentos específicos e até mesmo futuras convocações.

Carleto

Sua missão é desenvolver um sistema que colete e organize essas informações cruciais dos jogadores. O diferencial é que você deverá utilizar dicionários de forma central para armazenar e gerenciar os dados de todos os atletas, e, com base nesses registros, gerar relatórios de desempenho personalizados para o técnico.

Input

Você receberá informações de múltiplos jogadores, uma de cada vez. O processo de leitura dos dados de um jogador será iniciado com seu nome, sua disposição percentual no treino mais recente e sua posição. A entrada de jogadores será encerrada quando o nome_jogador for a palavra "FIM".

Para cada jogador, o fluxo de entrada será inicialmente:

    nome_jogador (str)

    disposicao_percentual (int)

    posicao (str) - podem ser: "atacante", "meio-campo", "zagueiro", "goleiro"

Após ler essas três informações, dependendo da disposição percentual do jogador, você receberá dados adicionais específicos:

Se a disposição percentual for maior ou igual a 85%:

Será informada a quantidade de ações ofensivas (chutes a gol) ou de passes dados por ele (esse input vem após a posição).

    chutes_ou_passes (int)

OBS: Se a posição do jogador for "Atacante", o valor de chutes_ou_passes representará chutes a gol. Se for de qualquer outra posição, o valor representará passes realizados.

Por outro lado, se a disposição percentual estiver no intervalo 50% e 84% (50% e 84% entram nessa condição):

Você receberá como entrada o desempenho do jogador no último jogo oficial.

    desempenho_ultimo_jogo (int) - Este é um valor numérico que representa a nota de desempenho (entre 0 e 100).

Por fim, se a disposição percentual for menor do que 50%:

Você receberá como entrada o desempenho do último treino realizado pelo jogador (anterior ao treino atual).

    desempenho_ultimo_treino (int) - Este também é um valor numérico que representa a nota de desempenho (entre 0 e 100).

Output

Após a leitura de todos os jogadores (ou seja, quando "FIM" for digitado como nome de jogador), seu programa deverá gerar um relatório detalhado de desempenho para cada jogador analisado, seguido por um resumo geral da análise da comissão técnica.
1. Relatório Individual de Desempenho

Para cada jogador presente no seu dicionário principal, imprima uma mensagem de avaliação específica, baseada nas suas estatísticas e na faixa de disposição. Os jogadores devem ser processados e suas mensagens impressas na MESMA ORDEM em que foram inseridos no input original.
Se a análise for sobre chutes a gol/passes (disposição percentual maior ou igual a 85%):

Se o jogador for "Atacante" e tiver mais que 10 chutes a gol, imprima:

    (nome_jogador) está com um bom desempenho ofensivo.

Se o jogador for "Atacante" e tiver 10 ou menos chutes a gol, imprima:

    (nome_jogador) pode melhorar, Ancelotti pode usá-lo no segundo tempo.

Se o jogador tiver qualquer outra posição e tiver no mínimo 20 passes, imprima:

    (nome_jogador) está com um bom desempenho de passes.

Se o jogador tiver qualquer outra posição e tiver menos do que 20 passes, imprima:

    (nome_jogador) pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.

Se a análise for sobre o desempenho no último jogo (disposição percentual entre 50% e 84%):

Se o desempenho_ultimo_jogo estiver acima de 80%, imprima:

    O jogador (nome_jogador) pode ser escalado para a próxima partida.

Se não, imprima:

    Ancelotti precisa analisar o desempenho do (nome_jogador) na partida.

Por último, se a análise for sobre o desempenho do último treino anterior (disposição percentual menor que 50%):

Se o desempenho_ultimo_treino estiver acima de 70%, imprima:

    Ancelotti deve colocar (nome_jogador) para treinar mais.

Se não, imprima:

    (nome_jogador) não deveria estar na próxima convocação.

2. Resumo da Análise da Comissão Técnica

Após todos os relatórios individuais, imprima, após uma linha vazia (usem um print vazio) um resumo geral do time que ajude Ancelotti a ter uma visão panorâmica:

    Relatório dos jogadores:

    Total de jogadores analisados: qnt_jogadores

    Atacantes prontos para começar: qnt_atletas_prontos

    Meio-campistas e Defensores prontos para começar: qnt_mei_def_prontos

Observação para o Resumo:

Atacantes prontos para começar: Contabilize os atacantes que se encaixam em UMA destas condições:

        Disposição percentual >= 85% E mais de 10 chutes a gol
        OU Disposição percentual entre 50% e 84% E desempenho_ultimo_jogo > 80%

Meio-campistas e Defensores prontos para começar: Contabilize os jogadores de outras posições que se encaixam em UMA destas condições:

        Disposição percentual >= 85% E no mínimo 20 passes
        OU Disposição percentual entre 50% e 84% E desempenho_ultimo_jogo > 80%

💡 Observações Importantes:

    Utilize um dicionário para armazenar os dados de cada jogador.
    Nem sempre as entradas irão conter os 4 tipos de jogadores (atacantes, meio-campistas, defensores (zagueiros e goleiros)), logo, o seu código deve lidar com isso.

Examples

Case: 1

Input

Vinicius Jr
90
atacante
15
Casemiro
88
meio-campo
25
Richarlison
92
atacante
8
Militão
85
zagueiro
18
Alisson
91
goleiro
20
FIM

Output

Vinicius Jr está com um bom desempenho ofensivo.
Casemiro está com um bom desempenho de passes.
Richarlison pode melhorar, Ancelotti pode usá-lo no segundo tempo.
Militão pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.
Alisson está com um bom desempenho de passes.

Relatório dos jogadores:
Total de jogadores analisados: 5
Atacantes prontos para começar: 1
Meio-campistas e Defensores prontos para começar: 2