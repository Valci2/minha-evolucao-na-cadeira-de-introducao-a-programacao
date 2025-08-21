A Terra está sob ameaça do Império Viltrumita! A Global Defense Agency (GDA), em um protocolo secreto precisa da sua ajuda, aluno ilustre da disciplina de Introdução a Programação, para desenvolver um sistema de gerência de times de heróis e implementação de um protocolo especial quando o Teen Team estiver completo.

Sua missão é defender a terra contra o Império Viltrumita!

Desenvolver um sistema em Python que:

    Gerencie múltiplos times de heróis com no minimo 3 membros no final das mudanças.

    Descodifique os nomes dos heróis por segurança

    Detecte quando os 4 membros do Teen Team ['rex splode', 'duplikate', 'atom eve', 'robot'] estão no mesmo time. Caso isso aconteça: aumente os poderes de todos os heróis do time em 10%, através de uma tecnologia secreta da GDA, mas lembre-se: apenas caso o teen team esteja completo dentro desse time no final das mudanças.

    Escolher o melhor time que deverá defender a terra, baseado no somatório de seus poderes de ataque, onde o melhor time possui o maior somatório de poder.

    Prepare o melhor time para defender a Terra, ao ordenar o time escolhido de forma decrescente de poder, e apenas utilizar os 3 mais fortes desse time para enfrentar o trio viltrumita composto por: [['general kregg',110],['conquista',100], ['anissa', 90]], com cada viltrumita está representado com nome e poder de ataque, respectivamente.

    O Sistema de batalha será no formato 1 contra 1, onde o mais forte herói deverá enfrentar o viltrumita mais forte, o 2º mais forte contra o 2º mais forte, e o 3º contra o 3º, caso um oponente seja vitorioso ele não irá lutar novamente, devendo dar espaço para o próximo combate.

    Vencerá o time que ganhar mais batalhas dentre as 3.

Decodificação

Você deverá montar um sistema que descodifique os nomes dos heróis selecionados da seguinte forma:

Os nomes dos heróis serão recebidos traduzidos de um alfabeto codificado, onde cada letra representa a letra da mesma posição no alfabeto padrão..

Ou seja, se você receber a letra 'k' no input, deve interpretá-la como 'a'.

Este é o alfabeto codificado:

    ['k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c']

Por exemplo o nome ‘cin’, usando a codificação desse alfabeto seria ‘frl’, pois ‘c’ no alfabeto normal tem index 2; ‘i’ tem index 8 e ‘n’ tem index 13 (você recebe 'frl' e traduz para 'cin').

OBS¹: Lembrem q o index começa em 0

OBS²: O caractere espaço ' ' deve ser mantido como está no nome decodificado.

Input

Inicialmente você receberá um input N inteiro representando a quantidade MÁXIMA de times que deverão ser guardados numa matriz no estilo: equipes = [ [equipe1],…,[equipeN] ]:

    N (inteiro)

Obs.: Pode acontecer de não ser formada a quantidade máxima de times. Todavia, lembre que todo time formado tem no mínimo 3 membros.

Após isso, você deverá receber diversas entradas de ação até que seja recebido ‘FIM’,

    acao_1 (string)

    ...

    acao_2

    …

    acao_n

Caso a ação seja ‘adicionar’

    Você irá receber logo em seguida um input com o nome codificado do herói e seu poder de ataque inteiro no formato: nome_heroi_codificado - poder_ataque
    Depois um valor inteiro representado qual time ele será incluído.

OBS¹: Caso o input seja 0(zero), ele representa o primeiro time da matriz. A contagem inicia do 0(zero) e segue normalmente.

Exemplo:

    adicionar

    kbjd xwx - 100

    2

Caso a ação seja ’metamorfo’,:

Significa que um dos heróis escolhidos não passa de uma mera imitação feita pelo metamorfo, logo você deverá substitui-lo do time em que ele está inserido.

    Você irá receber o nome do herói já decodificado e deverá retirar esse herói de seu respectivo time
    Depois você vai receber mais uma linha no mesmo formato da ação ‘adicionar’, sendo um novo herói codificado, que você vai precisar descodificar e inserir no time em que o herói removido estava.
    Em seguida um valor inteiro representado qual time ele terá a troca.

exemplo:

    metamorfo

    atom eve

    uxo yanjmx - 200

    1

A ação ‘FIM’ representa o fim desse processo de manipulação dos times.

Output

Caso a ação seja ‘adicionar’, você deverá printar:

    Quem será o próximo integrante do time?

Caso a ação seja ‘metamorfo’, você deverá printar:

    Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?

Após receber o nome do herói a ser removido você deverá printar:

    Quem você gostaria de colocar no lugar?

Tanto na ação de Adicionar quando na de Metamorfose, caso você receba um dos integrantes do Teen Team, você vai printar algo especial desse herói:

Se o herói for ‘rex splode':

    Eu vou te detonar!

Caso seja ‘atom eve’:

    Eu reescrevo a matéria... incluindo a SUA.

Caso seja ‘duplikate’:

    Quantas de mim você acha que consegue lidar?

Por fim caso seja ‘robot’:

    Minha lógica diz que você vai perder.

Agora após o fim do processo de seleção do time, você deverá verificar entre todos times, se algum deles possui os 4 integrantes do teen team, caso isso aconteça você deverá printar, apenas uma vez:

    O teen team esta completo, Cecil esta muito contente!

Caso as batalhas ocorram você deverá printar o top 3 do time, e caso o time tenha apenas 3 integrantes, printe apenas os 3:

    Aqui está o poderoso time da terra: {heroi1}, {heroi2}, {heroi3}

Para cada rodada, você irá printar cada confronto, iniciando pelos mais fortes, com X representando o numero da rodada, começando com 1.

    {X} Duelo: {heroi} X {viltrumita}

Por fim, se o time da terra vencer mais disputas printe:

    A terra venceu!

Caso os viltrumitas consigam expandir seu império e conquistar a Terra printe:

    Infelizmente o imperio viltrumita conquistou a terra!

Examples

Case: 1

Input

3
adicionar
kbjd xwx - 80
0
adicionar
ujqjb - 75
0
adicionar
rlwrlfrqnx - 90
0
FIM

Output

Quem será o próximo integrante do time?
Eu reescrevo a matéria... incluindo a SUA.
Quem será o próximo integrante do time?
Minha lógica diz que você vai perder.
Quem será o próximo integrante do time?
Aqui está o poderoso time da terra: invincible, atom eve, robot
1 Duelo: invincible X general kregg
2 Duelo: atom eve X conquista
3 Duelo: robot X anissa
Infelizmente o imperio viltrumita conquistou a terra!

Case: 2

Input

2
adicionar
uxo yanjmx - 85
0
metamorfo
rex splode
qgnnxbaujje - 95
0
adicionar
knnxl bzx knrxl - 130
0
adicionar
kbjd xwx - 120
0
FIM

Output

Quem será o próximo integrante do time?
Eu vou te detonar!
Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?
Quem você gostaria de colocar no lugar?
Quem será o próximo integrante do time?
Quem será o próximo integrante do time?
Eu reescrevo a matéria... incluindo a SUA.
Aqui está o poderoso time da terra: allen the alien, atom eve, bulletproof
1 Duelo: allen the alien X general kregg
2 Duelo: atom eve X conquista
3 Duelo: bulletproof X anissa
A terra venceu!