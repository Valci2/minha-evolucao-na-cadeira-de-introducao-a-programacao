O Centro de Informática (CIn) da UFPE decidiu que está na hora de eleger um novo mascote oficial — um cão carismático, talentoso e cheio de energia, à altura da comunidade CInzeira. Para isso, foi lançada uma competição entre três candidatos caninos, e o vencedor será anunciado com festa por todo o campus.

Entre os participantes, há rumores de que Byte, o lendário cãozinho do CIn, resolveu entrar na disputa. E, sejamos sinceros... se Byte participar, a competição acaba na hora — afinal, ele já conquistou o coração de todos!
Como funciona a disputa?

Cada cão será testado em três provas clássicas:

    O salto sobre a pilha de monitores antigos
    A travessia do labirinto de cabos
    O desafio do latido melódico na sala de aula

Cada prova vale de 0 a 10 pontos, e a pontuação total de cada cão definirá quem leva o título de mascote.

Regras da disputa:

    Se Byte estiver entre os competidores, ele vence imediatamente, sem discussão. O CIn já sabe quem manda!
    Caso nenhum cão se chame Byte:
        Se algum fizer exatamente 30 pontos, ele é declarado vencedor imediatamente, por ter sido perfeito!
        Se algum fizer menos de 15 pontos, está automaticamente fora da disputa (ninguém quer um mascote dorminhoco!).
        Não há empates: apenas um cão pode vencer.
        Sempre haverá um vencedor.

Sua missão

Você foi convocado como voluntário para ajudar na contagem de pontos dos candidatos. Escreva um programa que receba os dados dos três cães e determine quem será o novo mascote do CIn!

Input

Para cada cão participante:

    nome_cao (string)
    pontuação_prova_1 (inteiro)
    pontuação_prova_2 (inteiro)
    pontuação_prova_3 (inteiro)

    Se o nome for Byte, ele vence imediatamente e a competição se encerra!

    Se alguém fizer 30 pontos, também vence automaticamente!

    O programa sempre recebe o nome do cão e suas três pontuações. Somente após estas entradas serem fornecidas é que o programa avalia se foi "Byte" ou foi 30 pontos e encerra o resto da competição imediatamente.

Output

    Se o nome for “Byte”:

“Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!”. Declarando Byte como vencedor, a disputa acaba imediatamente, de forma que seu programa não deve receber novas entradas.

    Se alguém fizer exatamente 30 pontos:

“Com uma pontuação perfeita, {nome_cao} conquista o título de mascote do CIn!”. Declarado o vencedor com pontuação máxima, a disputa acaba imediatamente, de forma que seu programa não deve receber novas entradas.

O programa recebe o do cão e suas três pontuações. Somente após esses três entradas serem fornecidos, é que o programa avalia se o nome é "Byte" ou se o cão obteve 30 pontos. E, a partir daí, não recebe mais entradas.

Caso nenhuma dessas situações ocorra, todas as entradas são recebidas e as pontuações devem ser analisadas e impressas conforme os seguintes critérios:

    Se um cão fizer menos de 15 pontos:

“Infelizmente {nome_cao} está fora da disputa”

    Realizado o cálculo, declarar o vencedor, conforme a maior pontuação obtida:

“Após uma disputa acirrada, o novo mascote do CIn é {nome_cao}!”

Examples

Case: 1

Input

Byte
10
8
6

Output

Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!

Case: 2

Input

Bolt
4
4
5
Meg
3
5
6
Max
8
9
8

Output

Infelizmente Bolt está fora da disputa
Infelizmente Meg está fora da disputa
Após uma disputa acirrada, o novo mascote do CIn é Max!