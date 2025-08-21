Em um semestre curto e cheio de bugs, prazos e desafios, os monitores de IP tiveram problemas ao avaliar as listas e dar os feedbacks para os alunos. Para resolver o ocorrido, chamaram o único que poderia ajudá-los: Byte, o super mascote de IP! 🐶

Byte agora precisa da sua ajuda para criar um programa que facilite a avaliação dos alunos da cadeira, utilizando como critério a quantidade de questões que o aluno resolveu em cada lista. As orientações são as seguintes:

Serão 6 listas no total, valendo 10 pontos cada. As três primeiras listas possuem 10 questões cada, e as três últimas, 6 questões cada.

O valor de cada questão será o total da pontuação da lista (10) dividido pela quantidade de questões. Ou seja, para as listas de 10 questões, o valor de cada questão será 1 ponto, e para as listas de 6 questões, o valor de cada questão será 10/6 pontos.

A média geral será calculada com uma média simples das notas obtidas em todas as listas.

Input

A entrada será o nome do aluno, seguido pela quantidade de questões corretas de cada uma das listas:

    Nome do aluno (string)

    Acertos lista 1 (int)

    Acertos lista 2 (int)

    …

    Acertos lista 6 (int)

Output

Na saída, Byte inicialmente deve printar a média geral do aluno (com uma casa decimal):

    A média de {nome_do_aluno} é {media_geral}

Byte também deverá ajudar nos feedbacks, retornando uma avaliação baseada em alguns critérios.

Baseada no rendimento:

Caso o aluno mantenha um rendimento constante, ou seja, nunca fez menos pontos em uma lista em relação à lista anterior:

    Progresso constante! Parabéns pelo esforço!

Caso contrário:

    Alerta! Queda no rendimento.

Baseada na quantidade de listas não feitas:

Caso o aluno não tenha feito duas listas ou mais:

    Alerta! Múltiplas listas não respondidas.

Baseada na nota das listas:

Caso o aluno tenha no mínimo nota 8 na média geral das listas:

    Parabéns pelo excelente desempenho! Continue "au" sim.

Caso o aluno tenha média geral maior ou igual a 7 e menor ou igual a 7,9:

    Parabéns pelo bom desempenho!

Caso o aluno tenha média geral abaixo de 7:

    Alerta! Desempenho abaixo do esperado.

Examples

Case: 1

Input

Maria
6
8
8
5
5
5

Output

A média de Maria é 7.8
Progresso constante! Parabéns pelo esforço!
Parabéns pelo bom desempenho!

Case: 2

Input

Pedro
9
5
6
0
3
0

Output

A média de Pedro é 4.2
Alerta! Queda no rendimento.
Alerta! Múltiplas listas não respondidas.
Alerta! Desempenho abaixo do esperado.