O nosso querido mascote Byte acaba de chegar aos ambientes do Centro de Informática, estamos todos muito felizes com a sua chegada, que deve entrar para a história pois já sabemos que ele é o melhor mascote que já existiu!

byte_disco_img

Byte é um filhote muito brincalhão e cheio de energia, porém, acabou fazendo mais bagunça que o esperado e está dando muito trabalho. Por causa disso, o nosso novo pet está em processo de adaptação e de treinamento. Agora você está responsável por acompanhá-lo durante as suas explorações pelo CIn e por registrar todo o avanço dele ao longo do dia!

cachorro_gif

Input

Você receberá um conjunto de informações que indicarão, respectivamente:

    O humor de Byte;
    A quantidade de vezes que cada comando de treinamento já foi utilizado com o nosso mascote;
    E um comando para que ele execute no momento.

Os inputs sempre serão na seguinte ordem:

    Humor de Byte (string)

    Quantidade de vezes que já foi utilizado o comando Senta (int)

    Quantidade de vezes que já foi utilizado o comando Dá a patinha (int)

    Quantidade de vezes que já foi utilizado o comando Fica (int)

    Quantidade de vezes que já foi utilizado o comando Pega (int)

    Próximo comando (string)

Como o nosso doguinho é muito esperto, na terceira ordem de um mesmo comando ele já vai ter aprendido esse novo truque!. Por exemplo, se já foi dada a ordem de Senta duas vezes e o próximo comando foi também Senta, pode-se considerar que o aprendizado de Senta aconteceu (independente do humor).

Vale ressaltar que o nosso mascote já demonstra muita personalidade e, em alguns momentos, mesmo já tendo aprendido algum truque, ele pode não respeitar alguns comandos dados a ele.

    Se o humor de Byte for Brincalhão, ele não irá respeitar os comandos Senta e Fica.
    Se o humor de Byte for Preguiçoso, ele não irá respeitar o comando Pega.

Output

    Se o comando for Senta e Byte realizá-lo, mostre a seguinte mensagem:

    “Byte é o melhor”

    Caso ele não respeite o comando por causa do humor, mostre a seguinte mensagem:

    “Ele parece estar muito animado para isso!”

    Se o comando for “Dá a patinha” e Byte realizá-lo, mostre a seguinte mensagem:

    “Ele é um bom garoto!”

    Se o comando for “Fica” e Byte realizá-lo, mostre a seguinte mensagem:

    “Ele está aprendendo”

    Caso ele não respeite o comando por causa do humor, mostre a seguinte mensagem:

    “Ele não consegue ficar parado”

    Se o comando for “Pega” e Byte realizá-lo, mostre a seguinte mensagem:

    “Ele é muito ágil!”

    Caso ele não respeite o comando por causa do humor, mostre a seguinte mensagem:

    “Quem não tem seu momento de preguiça?”

    Para todos os casos, se Byte não respeitar o comando por não ter o aprendido ainda, mostre a seguinte mensagem:

    “Parece que ele não aprendeu esse truque ainda”

    Ao final, caso o cachorro saiba ao menos 1 truque, verifique a quantidade atualizada de repetições de cada comando, considerando também o comando do início do programa (ou seja, considere também a entrada "próximo comando"). Se Byte domina pelo menos um truque, mostre todos que ele aprendeu até o momento, da seguinte maneira:

    O nosso novo mascote estava {humor_byte} e aprendeu o(s) seguinte(s) truque(s):

    truque1

    truque2

    truque3

    truque4

    Vale ressaltar que pode ser exibido apenas um, dois, três ou todos os comandos, e que a ordem para verificar os truques é sempre a mesma: Senta, Dá a patinha, Fica, Pega.

Examples

Case: 1

Input

Brincalhão
1
2
4
0
Dá a patinha

Output

Ele é um bom garoto!
O nosso novo mascote estava Brincalhão e aprendeu o(s) seguinte(s) truque(s):
Dá a patinha
Fica

Case: 2

Input

Preguiçoso
3
4
6
2
Pega

Output

Quem não tem seu momento de preguiça?
O nosso novo mascote estava Preguiçoso e aprendeu o(s) seguinte(s) truque(s):
Senta
Dá a patinha
Fica
Pega

Case: 3

Input

Alegre
0
1
2
2
Senta

Output

Parece que ele não aprendeu esse truque ainda