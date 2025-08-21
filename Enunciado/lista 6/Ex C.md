O novo presidente da CBF, Samir Xaud, ao ver o grande sucesso da nova Copa do Mundo de Clubes, decide tentar reformular o brasileirão e voltar ao seu antigo formato de torneio misto, com fase de grupos seguida por um mata-mata entre os melhores colocados.

Acelera CBF!!!

Entretanto, Samir já está mostrando sua falta de experiência: ele esqueceu de organizar o sorteio do cruzamento dos grupos da primeira fase!! Por isso, ele precisa que você desenvolva um programa capaz de:

    Receber os grupos do torneio, com os nomes dos times e suas respectivas pontuações;
    Processar a classificação de cada time dentro do grupo, conforme sua pontuação;
    E, posteriormente, exibir os confrontos definidos por Samir ao realizar o cruzamento dos grupos.

Em cada grupo, os dois melhores colocados avançam para a próxima fase e o último colocado é rebaixado.

O programa deve informar os confrontos definidos a partir do cruzamento dos grupos e também indicar os times rebaixados, ou seja, aqueles que ficaram em último lugar em seus grupos.

Exemplo de cruzamento, considerando um mata-mata entre grupo A e o grupo B:

    1º (primeiro) colocado do grupo A x 2º (segundo) colocado do grupo B

    2º (segundo) colocado do grupo A x 1º (primeiro) colocado do grupo B

ATENÇÃO:

Você precisa obrigatoriamente criar um dicionário para administrar os grupos. Ou seja, criar um dicionário que contenha as informações de todos os grupos e, consequentemente, de todos os times.

Input

O programa inicia com um inteiro que define a quantidade de grupos

    qtd_grupos (int)

Para cada grupo, serão fornecidos os dados de 4 times, conforme o seguinte formato:

    nome_time1 - pontuação_time1

    nome_time2 - pontuação_time2

    nome_time3 - pontuação_time3

    nome_time4 - pontuação_time4

Obs. 1: Não haverá times com pontuações iguais dentro de um mesmo grupo.

Obs. 2: Sempre será informado informações do grupo 1, depois do grupo 2, e assim sucessivamente, até a quantidade de grupos.

Após os grupos estarem definidos, o programa receberá por entrada uma string indicando quais grupos devem ser cruzados, no seguinte formato:

    N1 x N2

(onde N1 e N2 indicam os grupos a serem cruzados, respeitando a ordem de entrada dos dados)

Output

Caso a quantidade de grupos recebida seja menor que 2 ou um número ímpar, não haverá cruzamento entre os grupos e você deverá encerrar o programa após receber as entradas e imprimir:

    Mas como que vamos fazer um torneio com {qtd_grupos} grupos Samir!?

Caso a quantidade de grupos seja válida (número maior ou igual a 2 e par), imprima:

    Roda os dados Samir!

Ao receber os cruzamentos dos grupos, o programa deve imprimir:

    (quebra de linha)

    Confrontos chave {N}:

    {prim_colocado_grupoA} x {seg_colocado_grupoB}

    {seg_colocado_grupoA} x {prim_colocado_grupoB}

Obs.: N indica a ordem de cruzamentos entre grupos. Por exemplo: se 10 grupos forem cruzados, haverá 5 cruzamentos e o programa imprimirá “confrontos chave 1” até “confrontos chave 5”, conforme a ordem de entrada dos cruzamentos.

Por fim, imprima os times rebaixados no seguinte formato:

    (quebra de linha)

    O time {time_rebaixado} ficou em último lugar em seu grupo e foi rebaixado!

Examples

Case: 1

Input

4
Cruzeiro - 9
Coritiba - 6
Grêmio - 4
Flamengo - 0
Vasco da Gama - 8
São Paulo - 5
Sport Recife - 3
Palmeiras - 10
Athletico Paranaense - 5
Atlético Mineiro - 4
Corinthians - 3
Santos - 0
Fluminense - 4
Internacional - 3
Bahia - 2
Botafogo - 1
1 x 3
2 x 4

Output

Roda os dados Samir!

Confrontos chave 1:
Cruzeiro x Atlético Mineiro
Coritiba x Athletico Paranaense

Confrontos chave 2:
Palmeiras x Internacional
Vasco da Gama x Fluminense

O time Flamengo ficou em último lugar em seu grupo e foi rebaixado!
O time Sport Recife ficou em último lugar em seu grupo e foi rebaixado!
O time Santos ficou em último lugar em seu grupo e foi rebaixado!
O time Botafogo ficou em último lugar em seu grupo e foi rebaixado!