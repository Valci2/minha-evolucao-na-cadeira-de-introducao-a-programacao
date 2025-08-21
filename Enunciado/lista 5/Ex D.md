Nas Terras Intermédias, um bravo Maculado está prestes a enfrentar um dos poderosos chefes que assolam o reino de Elden Ring. A vitória, no entanto, não depende apenas de coragem, mas de uma preparação meticulosa. Sua jornada de preparação envolve aprimorar seu arsenal e, se a sorte permitir, ativar o poder de uma Grande Runa para ganhar uma vantagem crucial na batalha iminente.

aprimoramento

O jogador guiará o Maculado neste processo. A preparação se divide em duas partes principais: aprimoramento de armas e ativação de grandes runas.
1. Aprimoramento de Armas:

O Maculado pode carregar diversas armas consigo. Cada uma delas é recebida na entrada com um nome, um valor de dano e um tipo (básica/especial). O desafio consiste em verificar as condições para aprimorar essas armas e, quando possível, fortalecê-las — tornando seus danos mais potentes. Após receber uma arma, o programa recebe uma série de números que representam tentativas de aprimoramento. De forma que cada número recebido será analisado conforme o tipo da arma para decidir se ela será aprimorada ou não.

    Para armas básicas, o aprimoramento só acontece se o número recebido pertencer à sequência de Tribonacci (
    clique aqui para ver sobre como funciona a sequência de Tribonacci
    ). A cada número válido, a arma sobe 1 nível, aumentando seu dano em 10%. No entanto, armas básicas só podem alcançar no máximo o nível 20, ou seja, até 20 aprimoramentos válidos.
    Para armas especiais, o número precisa ser um fatorial válido (
    clique aqui para ver sobre como funciona a sequência dos fatoriais
    ). Cada número correto também eleva a arma em 1 nível, mas com um ganho de 20% de dano por nível. Com um limite de 10 aprimoramentos, ou seja, o limite para armas especiais, é de 10 níveis por arma.

Obs.: Os níveis são cumulativos: se uma arma for aprimorada com sucesso três vezes, ela estará no nível 3, e o aumento total de dano será calculado conforme o bônus percentual acumulado. Vale lembrar que, como os aumentos são percentuais, os valores de dano durante o processo podem se tornar números com casas decimais. Porém, após todos os aprimoramentos, o dano final de cada arma é convertido para um número inteiro, descartando qualquer parte decimal.
2. Ativação de Grandes Runas

Caso o Maculado escolha ativar uma Grande Runa em vez de aprimorar uma arma, seu programa deverá entrar no modo de reconhecimento de padrões. A cada tentativa de ativação, o sistema recebe exatamente 10 números. O objetivo é identificar se, dentre esses 10 números, existe ao menos uma sequência de 3 números consecutivos (em termos de posição) que:

    Pertencem à sequência dos Números de Catalan,
    Aparecem na mesma ordem em que ocorrem na sequência original de Catalan.

Ou seja, é necessário procurar por três valores consecutivos i, i+1 e i+2 na entrada, tal que: entrada[i], entrada[i+1] e entrada[i+2] são todos números de Catalan, e eles respeitam a ordem original da sequência de Catalan(
clique aqui para ver sobre como funciona a sequência de catalan e diversas formas de implementá-la de forma recursiva
).

    Exemplo válido: [4, 5, 1, 1, 2, 5, 10, 15, 20, 25] A sequência 1, 2, 5 (nas posições 3 a 5) está em ordem e faz parte dos Números de Catalan
    Exemplo inválido: [14, 2, 1, 42, 5, 1, 2, 9, 5, 13] Apesar de conter números de Catalan, não há três consecutivos em ordem crescente da sequência

Se for encontrada essa sequência, a Grande Runa é ativada com sucesso, concedendo efeitos especiais que impactarão a batalha, conforme o nome da Grande Runa ativada:

    Grande Runa de Radahn: Dá um bônus de 15% na vida máxima.
    Grande Runa de Morgott: Dá um bônus de 25% da vida máxima.
    Grande Runade Godrick: Dá um bônus de 10% no dano de todas as armas após o aprimoramento e concede mais 10% de vida máxima.
    Grande Runa de Malenia: Durante a batalha, cada ataque do maculado recupera 5% da vida máxima (a vida do maculado não pode ultrapassar a vida máxima) e essa vida recuperada após ser calculada é transformada para inteiro também.

O valor inicial de pontos de vida do Maculado recebido na entrada representa sua vida máxima, ou seja, o maior valor de vida que ele pode atingir durante toda a disputa. Esse valor é definido antes do combate iniciar, e é sobre ele que incidem os bônus das Grandes Runas.

    À medida que o combate avança, o Maculado vai perdendo vida conforme sofre os contra-ataques do inimigo. Ele nunca poderá ultrapassar sua vida máxima, mesmo que receba curas durante a luta, como ocorre com a Grande Runa de Malenia, que restaura 5% da vida máxima a cada ataque bem-sucedido.
    Sempre que a vida for restaurada, o valor curado é calculado com base na vida máxima e, em seguida, convertido para número inteiro, descartando casas decimais.

batalha

Concluída a fase de preparação, o Maculado enfrentará o chefe em um combate por turnos, utilizando uma arma por vez, seguindo exatamente a ordem em que as armas foram registradas na entrada. A batalha se encerra quando o inimigo for derrotado, o Maculado morrer ou todas as suas armas forem utilizadas.

Cada turno é composto por uma sequência fixa de ações até que alguma das condições de término da batalha seja atingida, as ações são realizadas na seguinte ordem: Maculado → Inimigo, considerando que o inimigo só realizará uma ação se ainda estiver vivo após o ataque do Maculado.
1. Ataque do Maculado:

O Maculado sempre ataca primeiro. Ele usa a primeira arma disponível em seu arsenal, causando o dano correspondente na vida do inimigo. A arma utilizada no ataque não pode ser reutilizada, devendo ser removida do arsenal.

O programa deve verificar a Grande Runa de Malenia foi ativada, nesse caso, o Maculado tem até 5% da vida máxima acrescentado em seus pontos de vida atuais.
2. Ataque do Inimigo:

Após o ataque, o programa deve verificar a vida do inimigo. Se a vida for menor ou igual a zero, a batalha deve ser encerrada e declarada a vitória do Maculado. No entanto, se o inimigo sobreviver ao ataque, ele irá contra-atacar. O dano causado pelo inimigo é um valor fixo, recebido na entrada, e que permanece inalterado até o fim do combate.
3. Fim do Turno:

Se ambos os combatentes permanecerem vivos após o contra-ataque, o turno se encerra, e um novo turno se inicia, repetindo a mesma sequência de ações com a próxima arma disponível no arsenal do Maculado.
Obs.: É obrigatório o uso de funções recursivas para verificar se um número pertence a alguma das sequências (Tribonacci, Fatoriais, Catalan). Cada verificação deve ser implementada com sua própria função recursiva, e essas funções serão avaliadas como parte da lógica do programa.

Input

A ordem de recebimento é muito importante para que a lógica do programa funcione corretamente. Inicialmente, ocorrerá o recebimento das informações do Maculado:

    Formato: Nome - Vida (str)

    Exemplo: Let Me Solo Her - 500

A entrada seguinte indicará a quantidade total de ações que Maculado tomará em sua jornada de preparação, antes de enfrentar o inimigo. Essa quantidade corresponde à soma das ações de aprimoramento de armas com as tentativas de ativação de Grandes Runas, ou seja: total de ações = quantidade de armas que deseja aprimorar + número de tentativas de ativar runas

    qtd_total_acoes (int)

Após informar a quantidade total de ações (total de aprimoramentos de armas e tentativas de ativação de runas), o programa receberá uma entrada para cada ação.

Cada linha de entrada pode representar:

    Uma arma a ser aprimorada, ou
    A tentativa de ativação de uma Grande Runa

A forma como a linha está formatada permite identificar a qual tipo de ação a entrada corresponde:
Tipo de Entrada 1: Arma

Se a linha de entrada contiver o separador ‘ - ‘, a entrada é uma arma. E a string recebida será do seguinte formato:

    Nome - Dano - Tipo (str)

    O Nome é uma string qualquer (ex: Espada Longa, Lâmina Negra);
    O Dano é um valor numérico inteiro
    O Tipo deve ser "basica" ou "especial".

Exemplo - caso seja uma arma do tipo básica:

    Espada Longa - 120 - basica

Exemplo - caso seja um arma do tipo especial:

    Lâmina Negra - 200 - especial

Após o recebimento da arma, o programa aguardará entradas numéricas, um número por linha, representando tentativas de aprimoramento. Essas entradas continuam até que a palavra “fim” seja recebida. Exemplo de entradas para aprimoramento:

    1

    3

    24

    fim

Tipo de Entrada 2: Runa

Se a linha não contiver o separador ' - ‘, o sistema irá interpretar que se trata da tentativa de ativar uma Grande Runa.

    nome_grande_Runa (str)

Exemplo:

    Grande Runa de Godrick

Logo após o nome da runa, o programa deve receber exatamente 10 números inteiros, um por linha. Esses números serão utilizados para verificar se há uma sequência de 3 valores consecutivos que pertençam à sequência de Catalan, condição de ativação da runa. Exemplo de entradas para ativação:

    1

    2

    5

    14

    42

    132

    429

    1430

    4862

    1000

Obs.: O Maculado apenas irá tentar ativar uma runa.

Mesmo se a tentativa falhar, o Maculado não tentará ativar a runa novamente. Lembrando que o programa indentificará o tipo de ação (arma/runa) através do formato das entradas, conforme foi especificado acima.

Por último, o programa receberá uma string que corresponde às informações do inimigo, seguindo a estrutura:

    Nome - Vida - Dano (str)

Exemplo:

    Malenia, Blade of Miquella - 2500 - 150

Output
Fase de Preparação
1. Aprimoramento de Armas:

Para cada arma recebida, imprima:

    Vou levar a/o {nome_arma} ela/e vai ser de grande ajuda.

Ao iniciar o aprimoramento de uma arma:

    Hora de Aprimorar!!!

A cada aprimoramento bem-sucedido:

    Pronto, consegui mais um nível agora a/o {nome_arma} está no nível {novo_nivel}!

Se a arma foi aprimorada pelo menos uma vez, imprima:

    Agora sim! Acho que a/o {nome_arma} está forte o suficiente, consegui colocar ele/a para o nível {nivel_final}

Se a arma não foi aprimorada:

    Droga não consegui aumentar o nível da/o {nome_arma}

2. Ativação de Runa:

Se Maculado decidir tentar ativar alguma runa, imprima:

    A batalha vai ser difícil melhor tentar ativar uma runa!

    Me decidi vou tentar ativar a {nome_runa}, {frase_efeito}

As frases de efeitos de cada Grande Runas são:

Grande Runa de Godrick:

    acho que um pouco de tudo não é nada mal.

Grande Runa de Radahn:

    mais vida vai ajudar muito.

Grande Runa de Morgott:

    quanto mais vida melhor.

Grande Runa de Malenia:

    ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez.

Se a ativação da runa for bem-sucedida:

    Isso consegui ativar a Grande Runa.

Em seguida, imprimir os 3 primeiros números de Catalan presentes na sequencia numérica recebida:

    Acabei precisando apenas dos números: {N1} - {N2} - {N3}.

Se a ativação da runa falhar:

    Caramba não consegui ativar a Grande Runa, infelizmente vou ter que me contentar com as armas que vou levar.

A cada arma e grande runa processada, uma linha em branco é impressa no final para melhor visualização das saídas.

    quebra de linha

~
Fase de Batalha

A batalha ocorre em turnos. A cada turno, a seguinte sequência de mensagens é exibida:

    {num_turno}° TURNO

Começando no primeiro turno:

    1º TURNO

Status dos combatentes (Maculado):

    Melhor conferir meus status antes de lutar -> vida: ({vida_atual}/{vida_maxima})

Status dos combatentes (Inimigo):

    E o {nome_inimigo} ainda está com {vida_inimigo} pontos de vida

Ataque do Jogador:

    Atacando com {nome_arma_utilizada}.

    Consegui causar {dano_causado} de dano no/a {nome_inimigo}!!!"

    Acabei consumindo a/o {nome_arma_utilizada}, hora de pegar outra arma do arsenal.

Se a Grande Runa de Malenia estiver ativada, o inimigo ainda estiver vivo após o ataque do Maculado, e a vida atual do Maculado for menor que sua vida máxima, o programa deve aplicar o efeito de cura e imprimir a seguinte mensagem:

    Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {valor_de_cura}

Obs.: O valor base da cura é 5% da vida máxima. No entanto, como a vida do Maculado não pode ultrapassar a vida máxima, o valor de cura deve ser ajustado:

    Exemplo: se o Maculado está com 99/100 (vida_atual/vida_maxima) de vida e a cura calculada for 5, ele recupera apenas 1 ponto de vida, e esse valor (1) corresponde ao valor de cura e é o que deve ser exibido.

Se, após o ataque do Maculado, o inimigo sobreviver, ele executará um contra-ataque, causando dano ao Maculado. Nesse caso, imprima:

    Droga {nome_inimigo} ainda não morreu, acabei recebendo {dano_recebido} de dano.

A cada fim de turno, imprima um espaço vazio no para melhor visualização das saídas.

    quebra de linha

Fim da Batalha

A batalha pode terminar de duas maneiras principais: com a vitória ou a derrota de Maculado.
Cenário de Vitória (Inimigo Derrotado)

    Great Enemy Felled

Mensagem de resumo (dependendo do arsenal restante):

Se a vitória ocorreu, mas consumiu a última arma:

    Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o {nome_inimigo}.

Se a vitória ocorreu e ainda restam armas:

    Finalmente depois de tanto me preparar consegui derrotar a/o {Nome do Inimigo}.

Imprimir o número de armas restantes e cada uma delas, separadas por vírgula e espaço:

    Acho que me preparei bem eu ainda tenho {num_armas_restantes} arma/as sobrando são ela/as: {arma1}, {arma2}..., {armaN}."

Cenários de Derrota

Se a vida do inimigo ainda estiver acima de zero quando a batalha terminar, o Maculado foi derrotado.

Se a derrota foi causada apenas pela falta de armas:

    Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o {nome_inimigo} ainda tem {vida_inimigo} pontos de vida, vou ter que me preparar mais da próxima vez.

Se a derrota foi causada pela morte de Maculado, imprima:

    You Died

Seguido por:

    Droga acabei morrendo para a/o {nome_inimigo} e ele ainda tem {vida_inimigo} pontos de vida, vou ter que trazer armas mais fortes da próxima vez.

Obs.: Caso o maculado morra e suas armas também tenham acabado, a mensagem de morte tem prioridade e será a única mensagem de derrota exibida.

Examples

Case: 1

Input

Andarilho das Cinzas - 1600
5
Grande Runa de Malenia
1323
13
423
1
0
1
1
2
5
14
Lâmina de Escamas - 140 - basica
1
2
4
8
fim
Espada Larga de Cavaleiro - 155 - basica
13
24
44
fim
Uchigatana - 120 - basica
1
2
4
fim
Espada Magna de Starscourage - 250 - especial
6
24
fim
Sentinela da Árvore Dracônico - 900 - 550

Output

A batalha vai ser difícil melhor tentar ativar uma runa!
Me decidi vou tentar ativar a Grande Runa de Malenia, ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez.
Isso consegui ativar a Grande Runa.
Acabei precisando apenas dos números: 1 - 1 - 2.

Vou levar a/o Lâmina de Escamas ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Lâmina de Escamas está no nível 1!
Pronto, consegui mais um nível agora a/o Lâmina de Escamas está no nível 2!
Pronto, consegui mais um nível agora a/o Lâmina de Escamas está no nível 3!
Agora sim! Acho que a/o Lâmina de Escamas está forte o suficiente, consegui colocar ele/a para o nível 3

Vou levar a/o Espada Larga de Cavaleiro ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Espada Larga de Cavaleiro está no nível 1!
Pronto, consegui mais um nível agora a/o Espada Larga de Cavaleiro está no nível 2!
Pronto, consegui mais um nível agora a/o Espada Larga de Cavaleiro está no nível 3!
Agora sim! Acho que a/o Espada Larga de Cavaleiro está forte o suficiente, consegui colocar ele/a para o nível 3

Vou levar a/o Uchigatana ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Uchigatana está no nível 1!
Pronto, consegui mais um nível agora a/o Uchigatana está no nível 2!
Pronto, consegui mais um nível agora a/o Uchigatana está no nível 3!
Agora sim! Acho que a/o Uchigatana está forte o suficiente, consegui colocar ele/a para o nível 3

Vou levar a/o Espada Magna de Starscourage ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Espada Magna de Starscourage está no nível 1!
Pronto, consegui mais um nível agora a/o Espada Magna de Starscourage está no nível 2!
Agora sim! Acho que a/o Espada Magna de Starscourage está forte o suficiente, consegui colocar ele/a para o nível 2

1° TURNO
Melhor conferir meus status antes de lutar -> vida: (1600/1600)
E o Sentinela da Árvore Dracônico ainda está com 900 pontos de vida
Atacando com Lâmina de Escamas.
Consegui causar 186 de dano no/a Sentinela da Árvore Dracônico!!!
Acabei consumindo a/o Lâmina de Escamas, hora de pegar outra arma do arsenal.
Droga Sentinela da Árvore Dracônico ainda não morreu, acabei recebendo 550 de dano.

2° TURNO
Melhor conferir meus status antes de lutar -> vida: (1050/1600)
E o Sentinela da Árvore Dracônico ainda está com 714 pontos de vida
Atacando com Espada Larga de Cavaleiro.
Consegui causar 206 de dano no/a Sentinela da Árvore Dracônico!!!
Acabei consumindo a/o Espada Larga de Cavaleiro, hora de pegar outra arma do arsenal.
Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar 80
Droga Sentinela da Árvore Dracônico ainda não morreu, acabei recebendo 550 de dano.

3° TURNO
Melhor conferir meus status antes de lutar -> vida: (580/1600)
E o Sentinela da Árvore Dracônico ainda está com 508 pontos de vida
Atacando com Uchigatana.
Consegui causar 159 de dano no/a Sentinela da Árvore Dracônico!!!
Acabei consumindo a/o Uchigatana, hora de pegar outra arma do arsenal.
Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar 80
Droga Sentinela da Árvore Dracônico ainda não morreu, acabei recebendo 550 de dano.

4° TURNO
Melhor conferir meus status antes de lutar -> vida: (110/1600)
E o Sentinela da Árvore Dracônico ainda está com 349 pontos de vida
Atacando com Espada Magna de Starscourage.
Consegui causar 360 de dano no/a Sentinela da Árvore Dracônico!!!
Acabei consumindo a/o Espada Magna de Starscourage, hora de pegar outra arma do arsenal.

Great Enemy Felled
Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o Sentinela da Árvore Dracônico.

Case: 2

Input

Guerreiro Exausto - 2000
4
Martelo de Guerra - 160 - basica
1
2
4
8
13
24
44
fim
Claymore - 150 - basica
1
2
4
8
13
24
fim
Lança de Justa - 140 - basica
1
2
4
8
13
fim
Faca de Arremesso - 80 - basica
1
2
4
8
fim
Golem dos Guardiões - 1350 - 300

Output

Vou levar a/o Martelo de Guerra ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Martelo de Guerra está no nível 1!
Pronto, consegui mais um nível agora a/o Martelo de Guerra está no nível 2!
Pronto, consegui mais um nível agora a/o Martelo de Guerra está no nível 3!
Pronto, consegui mais um nível agora a/o Martelo de Guerra está no nível 4!
Pronto, consegui mais um nível agora a/o Martelo de Guerra está no nível 5!
Pronto, consegui mais um nível agora a/o Martelo de Guerra está no nível 6!
Agora sim! Acho que a/o Martelo de Guerra está forte o suficiente, consegui colocar ele/a para o nível 6

Vou levar a/o Claymore ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Claymore está no nível 1!
Pronto, consegui mais um nível agora a/o Claymore está no nível 2!
Pronto, consegui mais um nível agora a/o Claymore está no nível 3!
Pronto, consegui mais um nível agora a/o Claymore está no nível 4!
Pronto, consegui mais um nível agora a/o Claymore está no nível 5!
Agora sim! Acho que a/o Claymore está forte o suficiente, consegui colocar ele/a para o nível 5

Vou levar a/o Lança de Justa ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Lança de Justa está no nível 1!
Pronto, consegui mais um nível agora a/o Lança de Justa está no nível 2!
Pronto, consegui mais um nível agora a/o Lança de Justa está no nível 3!
Pronto, consegui mais um nível agora a/o Lança de Justa está no nível 4!
Agora sim! Acho que a/o Lança de Justa está forte o suficiente, consegui colocar ele/a para o nível 4

Vou levar a/o Faca de Arremesso ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Faca de Arremesso está no nível 1!
Pronto, consegui mais um nível agora a/o Faca de Arremesso está no nível 2!
Pronto, consegui mais um nível agora a/o Faca de Arremesso está no nível 3!
Agora sim! Acho que a/o Faca de Arremesso está forte o suficiente, consegui colocar ele/a para o nível 3

1° TURNO
Melhor conferir meus status antes de lutar -> vida: (2000/2000)
E o Golem dos Guardiões ainda está com 1350 pontos de vida
Atacando com Martelo de Guerra.
Consegui causar 283 de dano no/a Golem dos Guardiões!!!
Acabei consumindo a/o Martelo de Guerra, hora de pegar outra arma do arsenal.
Droga Golem dos Guardiões ainda não morreu, acabei recebendo 300 de dano.

2° TURNO
Melhor conferir meus status antes de lutar -> vida: (1700/2000)
E o Golem dos Guardiões ainda está com 1067 pontos de vida
Atacando com Claymore.
Consegui causar 241 de dano no/a Golem dos Guardiões!!!
Acabei consumindo a/o Claymore, hora de pegar outra arma do arsenal.
Droga Golem dos Guardiões ainda não morreu, acabei recebendo 300 de dano.

3° TURNO
Melhor conferir meus status antes de lutar -> vida: (1400/2000)
E o Golem dos Guardiões ainda está com 826 pontos de vida
Atacando com Lança de Justa.
Consegui causar 204 de dano no/a Golem dos Guardiões!!!
Acabei consumindo a/o Lança de Justa, hora de pegar outra arma do arsenal.
Droga Golem dos Guardiões ainda não morreu, acabei recebendo 300 de dano.

4° TURNO
Melhor conferir meus status antes de lutar -> vida: (1100/2000)
E o Golem dos Guardiões ainda está com 622 pontos de vida
Atacando com Faca de Arremesso.
Consegui causar 106 de dano no/a Golem dos Guardiões!!!
Acabei consumindo a/o Faca de Arremesso, hora de pegar outra arma do arsenal.
Droga Golem dos Guardiões ainda não morreu, acabei recebendo 300 de dano.

Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o Golem dos Guardiões ainda tem 516 pontos de vida, vou ter que me preparar mais da próxima vez.

Case: 3

Input

Viajante Cinzento - 1450
4
Lâmina Negra - 170 - especial
18
22
10
45
99
1
33
78
56
2
12
fim
Grande Espada do Lorde - 200 - especial
40
16
8
32
50
99
11
67
81
25
19
fim
Uchigatana - 150 - basica
11
15
9
21
34
55
89
5
13
20
41
7
fim
Cajado de Meteorito - 180 - especial
6
18
5
25
60
77
8
42
31
19
90
fim
Cavaleiro do Crisol - 600 - 210

Output

Vou levar a/o Lâmina Negra ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Lâmina Negra está no nível 1!
Pronto, consegui mais um nível agora a/o Lâmina Negra está no nível 2!
Agora sim! Acho que a/o Lâmina Negra está forte o suficiente, consegui colocar ele/a para o nível 2

Vou levar a/o Grande Espada do Lorde ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Droga não consegui aumentar o nível da/o Grande Espada do Lorde

Vou levar a/o Uchigatana ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Uchigatana está no nível 1!
Pronto, consegui mais um nível agora a/o Uchigatana está no nível 2!
Agora sim! Acho que a/o Uchigatana está forte o suficiente, consegui colocar ele/a para o nível 2

Vou levar a/o Cajado de Meteorito ela/e vai ser de grande ajuda.
Hora de Aprimorar!!!
Pronto, consegui mais um nível agora a/o Cajado de Meteorito está no nível 1!
Agora sim! Acho que a/o Cajado de Meteorito está forte o suficiente, consegui colocar ele/a para o nível 1

1° TURNO
Melhor conferir meus status antes de lutar -> vida: (1450/1450)
E o Cavaleiro do Crisol ainda está com 600 pontos de vida
Atacando com Lâmina Negra.
Consegui causar 244 de dano no/a Cavaleiro do Crisol!!!
Acabei consumindo a/o Lâmina Negra, hora de pegar outra arma do arsenal.
Droga Cavaleiro do Crisol ainda não morreu, acabei recebendo 210 de dano.

2° TURNO
Melhor conferir meus status antes de lutar -> vida: (1240/1450)
E o Cavaleiro do Crisol ainda está com 356 pontos de vida
Atacando com Grande Espada do Lorde.
Consegui causar 200 de dano no/a Cavaleiro do Crisol!!!
Acabei consumindo a/o Grande Espada do Lorde, hora de pegar outra arma do arsenal.
Droga Cavaleiro do Crisol ainda não morreu, acabei recebendo 210 de dano.

3° TURNO
Melhor conferir meus status antes de lutar -> vida: (1030/1450)
E o Cavaleiro do Crisol ainda está com 156 pontos de vida
Atacando com Uchigatana.
Consegui causar 181 de dano no/a Cavaleiro do Crisol!!!
Acabei consumindo a/o Uchigatana, hora de pegar outra arma do arsenal.

Great Enemy Felled
Finalmente depois de tanto me preparar consegui derrotar a/o Cavaleiro do Crisol.
Acho que me preparei bem eu ainda tenho 1 arma/as sobrando são ela/as: Cajado de Meteorito.