Durante a histórica final da Copa do Mundo de Tênis de Mesa, Hugo Calderano fez história ao derrotar Lin Shidong, o temido número 1 do ranking mundial, por 4 sets a 1. 🏓🥳

Infelizmente, nem todos ficaram satisfeitos com a conquista do nosso atleta brasileiro, e rumores de uma boicotagem se espalhavam pelos arredores.

Enquanto Hugo dava entrevistas e tirava selfies com fãs, algo tenebroso aconteceu: o troféu sumiu misteriosamente da mesa de premiação! 🏆💨

As câmeras de segurança estavam "curiosamente" desligadas, e a única pista concreta é: alguns atletas estavam muito próximos do troféu na hora do desaparecimento, e se tornaram fortes suspeitas do roubo do objeto.

Informações sobre os atletas presentes no local foram coletadas, e você, estudante de Introdução à Programação do CIn, foi contratado pela ITTF (Federação Internacional de Tênis de Mesa) como programador investigativo para ajudar a descobrir o culpado!

🕵️‍♀️ Como funcionam as investigações?

Você deve analisar as características de cada atleta envolvido na cena do crime e calcular uma pontuação de suspeita com base nos seguintes critérios:
🔤 Nome:

    Se a quantidade de vogais for PAR: +10 pontos de suspeita.
    Se a quantidade de vogais for ÍMPAR: +5 pontos de suspeita.

Dica: É interessante você saber como percorrer uma string usando laços de repetição. Caso você não saiba,
CLIQUE AQUI!
🧭 Posição do atleta em relação ao troféu (em graus):

    De 45° a 135° (em frente ao troféu): +10 pontos de suspeita.
    De 225° a 315° (atrás do troféu): +5 pontos de suspeita.
    Fora dessas faixas: +2 pontos de suspeita.

📊 Ranking mundial atual:

    Top 10 (ranking ≤ 10): +10 pontos de suspeita.
    Entre 11 e 50: +5 pontos de suspeita.
    Acima de 50: +2 pontos de suspeita.

💨 Velocidade de ataque:

    Se a velocidade for maior que 140 km/h: +10 pontos de suspeita.
    Se estiver entre 100 e 140 km/h: +5 pontos de suspeita.
    Se for menor que 100 km/h: +2 pontos de suspeita.

Após o cálculo das pontuações, você decidiu montar um ranking dos 3 atletas mais suspeitos, ou seja, que possuem a maior pontuação de suspeita, em ordem decrescente.

Obs.: Em caso de empate entre a pontuação de dois atletas, a ordem no ranking prioriza o atleta cuja entrada veio primeiro.

Boa sorte, detetive do CIn. A honra do esporte nacional depende do seu código!

Input

A primeira entrada será um número inteiro, representando a quantidade de atletas presentes na cena do crime.

    quantidade_atletas (int)

Em seguida, para cada atleta, coletar as seguintes informações:

    nome_atleta (string)

    posicao (int)

    ranking (int)

    velocidade (float)

Output
CASOS ESPECIAIS:

Caso apenas 2 atletas estiveram presentes no momento do roubo, você deve printar:

    Caso encerrado: {atleta_1} e {atleta_2} roubaram o troféu!

Caso apenas 1 atleta esteja presente próximo ao troféu, você deve printar:

    Não há dúvidas... {atleta} é o culpado!

OUTROS CASOS:

Quando não houver casos especiais, no início do programa, para cada nova rodada de investigação de um novo suspeito, você deve printar:

    COMEÇANDO A {num_rodada}ª RODADA DE INVESTIGAÇÃO

Durante o cálculo das pontuações, baseado nas características de cada atleta:

Caso o atleta esteja à frente do trófeu (entre 45º e 135º), printe:

    {atleta} estava em posição estratégica para pegar o troféu... muito suspeito!

Caso o atleta esteja no top10 mundial, printe:

    {atleta} é um dos melhores do mundo... e também um dos principais suspeitos!

Caso o atleta ultrapasse a velocidade de 140km/h, printe:

    Alta velocidade detectada! {atleta} pode ter fugido rapidamente com o troféu!

Caso o atleta não tenha atendido nenhuma das condições anteriores, printe:

    Hum, esse {atleta} sei não viu... Deve tá escondendo alguma coisa.

ATENÇÃO: As mensagens anteriores devem ser impressas na MESMA ORDEM em que estão dispostas no enunciado, para cada condição obedecida, seguindo também a ordem de entrada de cada atleta.

Após a investigação, o programa deve printar o ranking e o culpado:

    (pule uma linha)

    RESULTADOS DAS INVESTIGAÇÕES:

    (pule uma linha)

    Os 3 principais suspeitos são:

    1. {atleta_1} - {pontuacao_1} pontos

    2. {atleta_2} - {pontuacao_2} pontos

    3. {atleta_3} - {pontuacao_3} pontos

    (pule uma linha)

Sabe-se que, no máximo, duas pessoas roubaram o prêmio. Então, em caso de empate no top 3, o 1º e 2º lugar serão culpados, devendo printar a seguinte frase:

    Que absurdo... {atleta_1} e {atleta_2} roubaram o troféu juntos!

Se não houver empate, deve-se exibir o nome do principal suspeito:

    Mistério resolvido: O culpado é {atleta}! Ele roubou o troféu de Calderano.

Examples

Case: 1

Input

4
Lin Shidong
90
1
141.6
Wei Wuxian
315
24
101.1
Wang Chuqin
180
2
139.0
Lan Wangji
316
55
93.4

Output

COMEÇANDO A 1ª RODADA DE INVESTIGAÇÃO
Lin Shidong estava em posição estratégica para pegar o troféu... muito suspeito!
Lin Shidong é um dos melhores do mundo... e também um dos principais suspeitos!
Alta velocidade detectada! Lin Shidong pode ter fugido rapidamente com o troféu!
COMEÇANDO A 2ª RODADA DE INVESTIGAÇÃO
Hum, esse Wei Wuxian sei não viu... Deve tá escondendo alguma coisa.
COMEÇANDO A 3ª RODADA DE INVESTIGAÇÃO
Wang Chuqin é um dos melhores do mundo... e também um dos principais suspeitos!
COMEÇANDO A 4ª RODADA DE INVESTIGAÇÃO
Hum, esse Lan Wangji sei não viu... Deve tá escondendo alguma coisa.

RESULTADOS DAS INVESTIGAÇÕES:

Os 3 principais suspeitos são:
1. Lin Shidong - 35 pontos
2. Wang Chuqin - 22 pontos
3. Wei Wuxian - 20 pontos

Mistério resolvido: O culpado é Lin Shidong! Ele roubou o troféu de Calderano.

Case: 2

Input

2
Dimitrij Ovtcharov
270
20
137.0
Tomokazu Harimoto
180
4
91.2

Output

Caso encerrado: Dimitrij Ovtcharov e Tomokazu Harimoto roubaram o troféu!

Case: 3

Input

3
Lin Yun-Ju
45
12
139.9
Xiang Peng
224
9
137.0
Savi Matoso
45
13
127.7

Output

COMEÇANDO A 1ª RODADA DE INVESTIGAÇÃO
Lin Yun-Ju estava em posição estratégica para pegar o troféu... muito suspeito!
COMEÇANDO A 2ª RODADA DE INVESTIGAÇÃO
Xiang Peng é um dos melhores do mundo... e também um dos principais suspeitos!
COMEÇANDO A 3ª RODADA DE INVESTIGAÇÃO
Savi Matoso estava em posição estratégica para pegar o troféu... muito suspeito!

RESULTADOS DAS INVESTIGAÇÕES:

Os 3 principais suspeitos são:
1. Lin Yun-Ju - 25 pontos
2. Savi Matoso - 25 pontos
3. Xiang Peng - 22 pontos

Que absurdo... Lin Yun-Ju e Savi Matoso roubaram o troféu juntos!