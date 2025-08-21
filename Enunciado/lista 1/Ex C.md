Com a chegada de Byte, uma questão entrou na mente dos monitores responsáveis: Quem vai ter a honra e prazer de fazer o primeiro passeio do nosso querido Cachorro pelo Cin???

Byte, cachorro da monitori de IP, na frente do CIn

Para resolver esse problema, os monitores Arthur, Bruna, César, Daniel e Eduarda decidiram jogar um jogo chamado Zerinho ou Um Americano. Esse jogo consiste em todos os participantes escolherem um número de 0 a 10. Em seguida, somam-se todos os valores escolhidos e inicia-se uma contagem em círculo entre os jogadores. A pessoa onde a contagem parar é a selecionada.

Grupo de pessoas em uma roda jogando

Buscando uma forma mais justa e automatizada, o grupo optou por substituir a contagem presencial por um algoritmo que escolhesse o vencedor de forma imparcial. Nesse novo método, após a soma dos números, o programa calcula o resto da divisão dessa soma por 5. O resultado determina o ganhador, associando os valores da seguinte maneira: Arthur com o resto 0, Bruna com 1, César com 2, Daniel com 3 e Eduarda com 4.

Diante do desafio de desenvolver esse algoritmo, os monitores decidiram pedir a ajuda de alguém de fora da monitoria — e ninguém melhor para essa missão do que os alunos de Introdução à Programação do CIn, conhecidos por sua criatividade e habilidade com código!

Input

    Como input o programa vai solicitar 5 números, um para cada monitor.

    Numero (inteiro)

OBS: Os números usados pelos monitores são de 0 a 10, número de dedos que eles conseguem levantar!

Output

    Como output o programa deverá imprimir o vencedor do Jogo junto com a seguinte mensagem:

    “{Monitor} vai ter a honra de passear com Byte hoje!”

OBS: Tente usar operador
**modulo
!**

Examples

Case: 1

Input

10
10
0
1
5

Output

Bruna vai ter a honra de passear com Byte hoje!

Case: 2

Input

2
2
4
4
6

Output

Daniel vai ter a honra de passear com Byte hoje!