Em uma partida de Ping Pong no DA (Diretório Acadêmico) do CIn, Jaob e Luvusier, monitores de IP, estavam competindo de forma intensa.

Após diversas rodadas ainda empatadas, eles decidiram inovar e formular um novo método de pontuação.

gatos tênis de mesa

Agora, o objetivo deles é acertar objetos espalhados pelo DA. Dessa forma, eles chamaram você, aluno de IP, para produzir um programa em Python para registrar cada jogada dessa disputa frenética!

As regras da pontuação para essa competição estão apresentadas da seguinte forma:

Cada um dos objetos abaixo vale uma quantia de pontos:

    Baralho de UNO - valendo 2 pontos

    Armário de Homero e Elena - valendo 3 pontos

    Peça de Dominó - valendo 3 pontos

    Baralho de Coup Desaparecido - valendo 100 pontos e vitória instantânea

Porém, se um dos monitores acertar um dos objetos muito importantes abaixo, há uma perda de pontos para quem atingiu:

    Projetor: perde 2 pontos

    Computador: perde 3 pontos

    Cabeça do Amiguinho: perde 5 pontos

O monitor também pode não acertar nenhum dos alvos citados anteriormente:

    Nada: perde 1 ponto

OBS: Apesar da possibilidade de uma quantidade enorme de erros, ficou definido que a pontuação nunca deve ficar negativa.

Input

Será realizada apenas uma partida. Dessa forma, o seu programa receberá um número inteiro correspondente ao número de rodadas:

    numero_rodadas (int)

Em seguida, antes do início da primeira rodada, deve-se informar o vencedor da tomada (uma rodada de pré-início do jogo, para definir quem começa a partida).

    vencedor_tomada (string)

Em seguida, para cada rodada, as jogadas serão alternadas entre Jaob e Luvusier, começando pelo vencedor da tomada.

ATENÇÃO: Ao fim de uma rodada, na próxima a ser iniciada, quem venceu a rodada anterior irá começar jogando.

Antes de acertar um objeto, eles querem o ângulo perfeito para melhorar a pontaria, então, por uma quantidade indeterminada de vezes, eles podem ficar rebatendo a bola na mesa, informando:

    mesa

OBS.: Quem começa a rodada (faz o saque), nunca pode iniciar tentando acertar um objeto.

Em alguma jogada, o monitor pode arriscar acertar um objeto, informando:

    objeto_acertado (string)

Output

Primeiramente, no início do programa, após a coleta do número de rodadas, deve ser impresso:

    Vamos dar início à disputa!!! TOMADA!!!

Caso o vencedor da tomada seja Jaob:

    Jaob veio de Catende e está pronto para vencer!!!

Caso o vencedor da tomada seja Luvusier:

    Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!

Ao ser iniciada uma nova rodada, deve ser impresso:

    COMEÇA A {numero_rodada}ª RODADA!

Para cada jogada alternada entre os monitores, deve-se printar:

    {nome_monitor} jogou a bolinha no(a) {objeto_acertado}!

Obs.: Lembre-se que o objeto acertado pode ser a mesa, que pode ser utilizada até conseguir o ângulo perfeito!

Caso o objeto acertado aumente a pontuação, imprima:

    {nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pontuacao_atual} pontos.

Caso o objeto acertado diminua a pontuação, imprima:

    {nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pontuacao_atual} pontos.

Caso o objeto acertado seja Baralho de Coup Desaparecido, imprima:

    {nome_monitor} achou o Coup!!! Ele merece a vitória sem dúvidas!

Ao fim de todas as rodadas, deve-se quebrar uma linha e imprimir o resultado da partida:

    TEMOS O RESULTADO DA PARTIDA!

Caso Jaob seja o vencedor da partida:

    Jaob deu orgulho à Catende e ganhou a disputa com {pontuacao} pontos!

Caso Luvusier seja o vencedor da partida:

    A química está em festa, Luvusier ganha a disputa com {pontuacao} pontos!

Se houver empate:

    Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!

Examples

Case: 1

Input

2
Jaob
mesa
Peça de Dominó
mesa
Baralho de UNO

Output

Vamos dar início à disputa!!! TOMADA!!!
Jaob veio de Catende e está pronto para vencer!!!
COMEÇA A 1ª RODADA!
Jaob jogou a bolinha no(a) mesa!
Luvusier jogou a bolinha no(a) Peça de Dominó!
Luvusier teve uma grande pontaria e acertou Peça de Dominó! Agora está com 3 pontos.
COMEÇA A 2ª RODADA!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) Baralho de UNO!
Jaob teve uma grande pontaria e acertou Baralho de UNO! Agora está com 2 pontos.

TEMOS O RESULTADO DA PARTIDA!
A química está em festa, Luvusier ganha a disputa com 3 pontos!

Case: 2

Input

5
Luvusier
mesa
mesa
mesa
Armário de Homero e Elena
mesa
Baralho de UNO
mesa
mesa
mesa
Projetor
mesa
mesa
mesa
mesa
Cabeça do Amiguinho
mesa
mesa
Nada

Output

Vamos dar início à disputa!!! TOMADA!!!
Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!
COMEÇA A 1ª RODADA!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) mesa!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) Armário de Homero e Elena!
Jaob teve uma grande pontaria e acertou Armário de Homero e Elena! Agora está com 3 pontos.
COMEÇA A 2ª RODADA!
Jaob jogou a bolinha no(a) mesa!
Luvusier jogou a bolinha no(a) Baralho de UNO!
Luvusier teve uma grande pontaria e acertou Baralho de UNO! Agora está com 2 pontos.
COMEÇA A 3ª RODADA!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) mesa!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) Projetor!
Jaob teve mãos de alface e acertou o(a) Projetor. Agora está com 1 pontos.
COMEÇA A 4ª RODADA!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) mesa!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) mesa!
Luvusier jogou a bolinha no(a) Cabeça do Amiguinho!
Luvusier teve mãos de alface e acertou o(a) Cabeça do Amiguinho. Agora está com 0 pontos.
COMEÇA A 5ª RODADA!
Jaob jogou a bolinha no(a) mesa!
Luvusier jogou a bolinha no(a) mesa!
Jaob jogou a bolinha no(a) Nada!
Jaob teve mãos de alface e acertou o(a) Nada. Agora está com 0 pontos.

TEMOS O RESULTADO DA PARTIDA!
Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!