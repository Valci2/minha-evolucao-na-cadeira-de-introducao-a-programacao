Vegeta, o orgulhoso e implacável Príncipe dos Saiyajins, finalmente chegou ao nosso planeta! Seu objetivo é um só: derrotar os guerreiros mais poderosos da Terra para provar sua superioridade e dominar tudo e todos.

O planeta precisa da sua ajuda! Sua missão, jovem programador, é desenvolver o simulador de batalhas que irá prever o resultado dessa ameaça.

Você criará um programa que controla os combates turno a turno, aplicando as regras de poder e motivação para decidir se a Terra será subjugada ou se a coragem de seus defensores prevalecerá!

Vegeta em batalha
Ordem dos Combates

A jornada de Vegeta seguirá uma ordem predefinida de oponentes. Ele só avança para o próximo se vencer o atual. A ordem é:
1. Piccolo
2. Gohan
3. Goku

A simulação ocorrerá em uma série de batalhas. Para CADA batalha, o programa entrará em um ciclo de combates.

Fique atento à ordem das informações que seu programa deve receber:

Cada combatente, incluindo o Vegeta, inicia com 100 de vida (HP). Todavia, a luta final contra Goku é mais difícil! Ele começa com o dobro da vida padrão (200 HP).

Obs 1: A vida de Vegeta é totalmente restaurada (100 HP) no início de cada nova batalha. Ou seja, se ele vencer Piccolo, enfrentará Gohan com 100 HP novamente — e o mesmo vale para o últmo confronto.

Obs 2: Reforçando, na batalha final, apenas Goku inicia com vida cheia (200 HP). Caso Vegeta avance até essa luta, ele começará com seus habituais 100 HP.
ATENÇÃO!!!

O seu código precisa ter NO MÍNIMO duas funções:

    Uma função para calcular o dano;
    Uma função para simular uma batalha por turnos entre Vegeta e um oponente.

Input
Motivação Inicial de Vegeta:

Logo no início, você receberá um único número decimal que representa a confiança inicial de Vegeta para toda a sua jornada de conquista.

    motivacao_inicial_vegeta (float)

Motivação dos Oponentes:

Para CADA novo oponente, você receberá a motivação do Guerreiro Z para aquela luta específica:

    motivacao_guerreiroZ (float)

Bônus de Vitória (Fórmula):

Após uma vitória, a NOVA motivação de Vegeta é calculada com a fórmula:

    motivacao = motivacao * (1 + (vida_restante_vegeta / vida_inicial_oponente))

Obs.: Note que a fórmula 1 + (vida_restante_vegeta / vida_inicial_oponente) é multiplicada pela motivação anterior.
Atenção!!!

A motivação de cada personagem deve multiplicar o valor do dano aplicado por ele, durante todas as batalhas.
Durante os Turnos do Combate:

A luta acontece em turnos, e a CADA turno seu programa precisa receber a ação de cada lutador. Vegeta sempre ataca primeiro.

Assim, você receberá uma string indicando o tipo de golpe escolhido,

    tipo_de_golpe (string)

que pode ser:

    Normal -> 20 pontos de dano.
    Potente -> 40 pontos de dano.

Isso se repete até que um dos lutadores seja derrotado.

Output

Inicialmente, seu programa deve exibir:

    A saga de Vegeta começa!

Após isso, pule uma linha.

Para cada nova batalha, antes de começar, imprima:

    --- Iniciando o combate contra {oponente} ---

Após isso, pule uma linha.

No início de cada turno, imprima o contador do turno:

    --- Turno {numero_do_turno} ---

Durante a luta, após CADA golpe, imprima a frase:

    {lutador} usou Golpe {tipo_de_golpe} e causou {qtd_dano} de dano!

Obs.: Lembre-se que, em um turno, ambos atacam (a não ser que o primeiro seja nocauteado).

Ao final de um turno completo (ambos atacaram) ou quando um lutador é nocauteado, imprima o status da vida no seguinte formato:

    |Vegeta: {vida_vegeta} HP vs {nome_oponente}: {vida_oponente} HP|

Obs.: A vida NUNCA deve ser exibida como negativa, mostrando 0 em seu lugar, se for o caso.

Após isso, pule uma linha.

Se Vegeta vencer uma batalha:

    Vitória de Vegeta!

    Vegeta venceu a batalha contra {nome_oponente} com {vida_restante} HP restantes!

Se Vegeta perder uma batalha:

    Vegeta foi derrotado! A Terra está a salvo graças a {nome_oponente}!

Se Vegeta vencer TODAS as batalhas, seu programa deve exibir a mensagem final de conquista:

    Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!

Se o Vegeta usar o Golpe Potente duas vezes seguidas, ele é derrotado instantaneamente! Seguido da mensagem:

    Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!

Obs.: Caso um combate acabe, a contagem dos Golpes Potentes é reiniciada para o próximo combate.

Examples

Case: 1

Input

1.5
1.0
Potente
Normal
Normal
Normal
Normal
1.2
Potente
Normal
Normal
1.3
Potente
Normal
Normal

Output

A saga de Vegeta começa!

--- Iniciando o combate contra Piccolo ---

--- Turno 1 ---
Vegeta usou Golpe Potente e causou 60 de dano!
Piccolo usou Golpe Normal e causou 20 de dano!
|Vegeta: 80 HP vs Piccolo: 40 HP|

--- Turno 2 ---
Vegeta usou Golpe Normal e causou 30 de dano!
Piccolo usou Golpe Normal e causou 20 de dano!
|Vegeta: 60 HP vs Piccolo: 10 HP|

--- Turno 3 ---
Vegeta usou Golpe Normal e causou 30 de dano!
|Vegeta: 60 HP vs Piccolo: 0 HP|

Vitória de Vegeta!
Vegeta venceu a batalha contra Piccolo com 60 HP restantes!

--- Iniciando o combate contra Gohan ---

--- Turno 1 ---
Vegeta usou Golpe Potente e causou 96 de dano!
Gohan usou Golpe Normal e causou 24 de dano!
|Vegeta: 76 HP vs Gohan: 4 HP|

--- Turno 2 ---
Vegeta usou Golpe Normal e causou 48 de dano!
|Vegeta: 76 HP vs Gohan: 0 HP|

Vitória de Vegeta!
Vegeta venceu a batalha contra Gohan com 76 HP restantes!

--- Iniciando o combate contra Goku ---

--- Turno 1 ---
Vegeta usou Golpe Potente e causou 168 de dano!
Goku usou Golpe Normal e causou 26 de dano!
|Vegeta: 74 HP vs Goku: 32 HP|

--- Turno 2 ---
Vegeta usou Golpe Normal e causou 84 de dano!
|Vegeta: 74 HP vs Goku: 0 HP|

Vitória de Vegeta!
Vegeta venceu a batalha contra Goku com 74 HP restantes!

Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!