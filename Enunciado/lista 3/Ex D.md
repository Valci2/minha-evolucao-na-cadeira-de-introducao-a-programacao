A vilã Rita Repulsa atacou novamente! Dessa vez, ela lançou um Raio de Confusão nos Power Rangers, fazendo com que todos esquecessem qual zord devem usar para formar o lendário Megazord. 😱

Felizmente, os CInners não foram afetados e agora sua missão é elaborar um programa em Python que ajude a distribuir corretamente os zords entre os rangers, com base no poder de cada zord. Para que, assim, eles formem o megazord e derrotem Rita!

power rangers fazendo posezinha

Há muito tempo, antes mesmo da primeira linha de código ser escrita, existia um zord lendário conhecido como robocin, o zord mais poderoso de todos.
Distribuição dos zords 🤖

Existem 3 tipos de zords a serem distribuídos entre os rangers.

    Zords do tipo 3 são aqueles com nível de poder de até nível 10.
    Zords do tipo 2 são aqueles com nível de poder acima de 10 e até nível 30.
    Zords do tipo 1 são aqueles com o nível de poder acima do nível 30.

    O ranger Vermelho deve receber o zord do tipo 1 com maior nível de poder.

    O ranger Verde deve receber o zord do tipo 1 com o segundo maior nível de poder.

    A ranger Rosa deve receber o zord do tipo 2 com maior nível de poder.

    O ranger Preto deve receber o zord do tipo 2 com o segundo maior nível de poder.

    O ranger Azul deve receber o zord do tipo 3 com maior nível de poder.

    A ranger Amarela deve receber o zord do tipo 3 com o segundo maior nível de poder.

    Cada ranger deve receber no máximo 1 zord
    Caso algum dos rangers não receba um zord, a equipe não será capaz de formar o Megazord, e sem o Megazord não serão capazes de derrotar Rita.
    Caso você receba o zord lendário robocin entre os outros zords, os rangers não precisarão mais montar o megazord pois o robocin tem poder suficiente para derrotar Rita sozinho. (Você não precisará distribuir os zords nesse caso).
    Considere que pode haver zords com nomes iguais e que nunca haverá empate nos níveis - ou seja, nunca haverá dois ou mais zords com pontuações iguais.
    Vale lembrar que: os rangers só podem receber zords do tipo especificado acima, não é possível dar um zord de um tipo maior que "sobrou" para o ranger, ele apenas suporta os zords do seu tipo determinado.

Proibições:

O uso de sorted() , .sort() e max() é PROIBIDO nessa questão.

Input

Você receberá uma única linha de entrada contendo uma sequência de N pares, onde cada par é composto pelo nome do zord e seu respectivo nível de poder, separados por um "-” (hífen).

    zord-nivel-zord-nivel...

Output

Antes de tudo, sempre deve ser ser impresso a seguinte frase:

    Go! Go! Power Rangers!

Caso o zord lendário robocin seja encontrado em meio aos outros zords, imprima:

    Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!

Caso o contrário:

Você deve imprimir um relatório com os zords de cada ranger, seguindo esta ordem: Vermelho, Verde, Rosa, Preto, Azul, Amarela.

    Para cada ranger que tiver um zord atribuído, imprima uma linha no formato:

    Zord do Ranger {cor}: {nome_do_zord}

ou

    Zord da Ranger {cor}: {nome_do_zord} (use “da” para a ranger rosa e a amarela)

    Caso o ranger não tenha recebido um zord, imprima:

    Ranger {cor} ficou sem zord!

Após imprimir o relatório de zords de cada ranger, imprima também um relatório com os zords agrupados por tipo (com os zords em ordem decrescente de nível de poder, do mais forte para o mais fraco), nesta ordem: tipo 1, tipo 2 e tipo 3.

    Para cada tipo que possuir zords, imprima, por exemplo:

    Zords do tipo {n}: {zord1}, {zord2}, {zord3}

    Caso não haja nenhum zord de um determinado tipo, imprima:

    Não temos nenhum zord do tipo {n} :(

    Caso todos os rangers tenham um zord e, consequentemente, consigam construir o megazord:

    Os Rangers estão prontos para montar o Megazord e derrotar Rita!

    Caso contrário:

    Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!

Examples

Case: 1

Input

cabra-320-robocina-100-falcao-20-berardozord-7000-tigre-1-discretozord-932

Output

Go! Go! Power Rangers!
Zord do Ranger Vermelho: berardozord
Zord do Ranger Verde: discretozord
Zord da Ranger Rosa: falcao
Ranger Preto ficou sem zord!
Zord do Ranger Azul: tigre
Ranger Amarela ficou sem zord!
Zords do tipo 1: berardozord, discretozord, cabra, robocina
Zords do tipo 2: falcao
Zords do tipo 3: tigre
Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!

Case: 2

Input

dragao-40-robocin-100-falcao-20

Output

Go! Go! Power Rangers!
Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!