Zen’oh e Zen’oh do futuro planejam organizar o torneio do poder (um torneio de proporções imensas, entre 8 universos diferentes!), mas por conta da complexidade (e preguiça…), não queriam ter que organizar e catalogar todas as informações relacionadas às lutas. Por isso, você, brilhante estudante de Introdução à Programação do Centro de Informática, foi requisitado como organizador do registro do torneio do poder! Sua tarefa é identificar os lutadores, calcular suas forças e, com base nisso, registrar os vencedores e perdedores. Para calcular a força entre dois lutadores, você deve analisar as técnicas que ambos utilizaram. Para calcular a pontuação de uma técnica, basta encontrar o resto da divisão do tamanho do nome da técnica (incluindo espaços em branco) por 8.

Ex.:

    Técnica = kaio-ken x100

    Pontuação = 13 mod 8 = 5

Obs.: Nesse exemplo, mod é o mesmo que 13 % 8 = 5 em Python.

Porém, é preciso ter atenção para quais lutas estão sendo travadas. Se a luta for entre lutadores específicos, um lutador adicional poderá se juntar a batalha como aliado de algum dos dois lutadores iniciais, e sua pontuação de técnica será adicionada à pontuação de técnica de seu aliado. A ordem dos lutadores é irrelevante, importa apenas se a luta é travada entre lutadores específicos. A seguir, as combinações de confrontos que possibilitam a entrada de um terceiro lutador e seu aliado na batalha:

    Se Goku e Jiren se enfrentarem, um novo lutador entrará na batalha aliando-se ao Goku.

    Se Frieza e Jiren se enfrentarem, um novo lutador entrará na batalha aliando-se ao Frieza.

    Se Gohan e Namekuseijins se enfrentarem, um novo lutador entrará na batalha aliando-se ao Gohan.

    Se Androide 17 e Ribrianne se enfrentarem, um novo lutador entrará na batalha aliando-se ao Androide 17.

OBS. 1: É obrigatório o uso de função para calcular a força de cada lutador e para a verificação do recebimento de um possível 3° lutador.

OBS. 2: É proibido o uso da palavra-chave global na resolução da questão.

Input

Você receberá os seguintes inputs:

    Um input inicial (sempre maior que zero) indicando a quantidade de batalhas que serão travadas no torneio.

    qtd_batalhas (int)

    Para cada batalha, você receberá dois inputs contendo, em uma linha, um lutador e sua respectiva técnica utilizada, separados por um hífen.

    lutador1 - técnica1 (str)

    lutador2 - técnica2 (str)

    Se a batalha possibilitar um terceiro lutador, um input extra com o nome do lutador e sua técnica deverá ser recebido logo após os dois lutadores iniciais dessa batalha.

    lutador3 - técnica3 (str)

Output

    Primeiramente, deve ser impresso, antes das batalhas:

    O torneio do poder irá começar com {qtd_batalhas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!

    Se houver um terceiro lutador entrando na batalha, deverá ser impresso:

    A intensidade dos dois lutadores motivou {lutador3} a entrar na batalha também!

    A cada batalha finalizada entre dois lutadores, deverá ser impresso:

    Incrível! {vencedor} mostrou sua força e defenderá seu universo até o final!

    A cada batalha finalizada entre três lutadores, deverá ser impresso:

    Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {tecnica1}, {tecnica2} e {tecnica3}! A batalha acaba com {vencedor} no topo!

ATENÇÃO:

    Em batalhas de 3 lutadores, se a dupla vencer, ela deverá ser impressa da seguinte forma: seus nomes devem estar separados por “e“, sendo o primeiro nome o lutador inicial e o segundo nome o 3° lutador. Exemplo: “Goku e Frieza”.
    NUNCA haverá empate entre os lutadores.

Examples

Case: 1

Input

1
Goku - Kamehameha
Vegeta - Final Flash

Output

O torneio do poder irá começar com 1 batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!
Incrível! Vegeta mostrou sua força e defenderá seu universo até o final!

Case: 2

Input

2
Jiren - Heatwave Magnetron
Piccolo - Special Beam Cannon
Androide 17 - Endgame
Ribrianne - Pretty Cannon
Goku - Genki Dama

Output

O torneio do poder irá começar com 2 batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!
Incrível! Piccolo mostrou sua força e defenderá seu universo até o final!
A intensidade dos dois lutadores motivou Goku a entrar na batalha também!
Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de Endgame, Pretty Cannon e Genki Dama! A batalha acaba com Androide 17 e Goku no topo!