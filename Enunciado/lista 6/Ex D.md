Falta menos de um ano para o início da Copa do Mundo de 2026 e a Seleção Brasileira está sofrendo com uma crise política desde o afastamento de Ednaldo Rodrigues. . O tempo está correndo e a CBF e seu presidente, Samir Xaud, precisam decidir se Ancelotti continuará no cargo ou irão procurar outro profissional que esteja à altura de treinar a maior seleção do planeta.

ChatGPT Image 22 de abr. de 2025, 16_53_09.png

Por isso, eles contrataram você, um estudante do Cin e futuro gênio da programação, para criar um programa que analise os possíveis treinadores e selecione o mais preparado para assumir o cargo.

A partir das informações coletadas pela competente equipe de scout da CBF, você deverá criar um ranking com os 3 melhores profissionais considerando os seguintes critérios:

    Cada título continental vale 100 pontos;
    Cada título nacional vale 50 pontos;
    Se o técnico for brasileiro, ele ganhará um acréscimo de 10% em cima da pontuação total;
    Se o técnico for alemão, ele perderá 10% de sua pontuação total;
    Caso o técnico NÃO possua títulos continentais, ele perderá 50% da sua pontuação total.

Cálculo da pontuação total:

 pontuação_total = (titulos_continentais + titulos_nacionais) * aproveitamento

Obs.: Não terá caso de empate ao final dos cálculos.

É OBRIGATORIO o uso de dicionário para armazenar as informações dos técnicos observados.

É PROIBIDO nessa questão o uso de listas e tuplas, consequentemente keys(), values(), items(), etc.

Input

A primeira entrada será a quantidade de técnicos que a CBF observa:

    qtd_tecnicos (int)

Obs: sempre haverá ao menos 3 técnicos

Logo após, você receberá uma sequência de inputs com o nome, a nacionalidade, a quantidade de títulos continentais e de títulos nacionais e o percentual de aproveitamento dos treinadores:

    nome (str)

    nacionalidade (str)

    titulos_continentais (int)

    titulos_nacionais (int)

    aproveitamento (float)

Obs: o aproveitamento sempre será um número maior que 0 e menor que 1

Além disso, você receberá um input confirmando se o técnico tem interesse em treinar a Seleção Brasileira.

    interesse (str)

Obs: o input será “sim” ou “não”

Output

    Caso um dos treinadores observados seja o “Ancelotti”, o programa deverá printar:

    Será que Carleto irá continuar no cargo?

    Já se um dos técnicos for o "Jorge Jesus", a seguinte frase deverá ser impressa:

    O mister finalmente retornará ao Brasil?

    Se a nacionalidade do profissional observado for “argentino”, ele será desconsiderado e a seguinte mensagem deverá ser impressa:

    Um hermano comandando a seleção? Sai fora!

Obs.: Por desconsiderado entenda que o programa não receberá as demais entradas referentes ao técnico caso a nacionalidade dele seja “argentino”.

    Se a nacionalidade for “alemão” o programa deverá imprimir o seguinte:

    Iremos mesmo perdoar o 7x1?

O programa deverá printar o ranking dos técnicos analisados da seguinte forma:

    Lista de treinadores - CBF

    1º {nome_1} - {nacionalidade_1} - {pontos_1} pontos

    2º {nome_2} - {nacionalidade_2} - {pontos_2} pontos

    3º {nome_3} - {nacionalidade_3} - {pontos_3} pontos

Obs1: o ranking deverá estar em ordem decrescente de acordo com os pontos

Obs2: os pontos deverão estar com duas casas decimais

    A escolha do técnico será feita percorrendo o ranking final, do 1º ao 3º colocado. O processo funciona da seguinte forma:
        O programa deve verificar o interesse de cada técnico em ordem.
        Para cada técnico verificado que não tiver interesse, a mensagem deverá ser impressa, e a análise continuará para o próximo do ranking.

        O {nome_n} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!

        O primeiro técnico que tiver interesse será o "escolhido", e a busca termina.
        Caso nenhum dos três técnicos do ranking tenha interesse após todos serem verificados, a seguinte mensagem deverá ser impressa no final:

        Nenhum técnico aceitou a maior seleção do mundo!? Que humilhação, Sr. Samir Xaud!!!

    Se o técnico escolhido não for brasileiro:

    {nome_n} será o quarto estrangeiro a treinar o Brasil. Que honra para o {nacionalidade_n}!

    Se “Ancelotti” estiver no ranking e tiver interesse em treinar a seleção os outros técnicos deverão ser desconsiderados, independente de suas posições no ranking:

    Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!

    Se o técnico escolhido for “Jorge Jesus”, o programa deverá imprimir:

    JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?

    Se o técnico escolhido for “Felipão”, o programa deverá imprimir:

    FELIPÃO DE NOVO!? Vem mais um 7x1 por aí?

    Caso o técnico escolhido não for nenhum dos citados anteriormente, o programa deverá imprimir:

    O técnico {nacionalidade_n} {nome_n} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!

Examples

Case: 1

Input

3
Ancelotti
italiano
5
5
0.7
sim
Jorge Jesus
português
3
5
0.8
sim
Joachim Low
alemão
4
2
0.6
não

Output

Será que Carleto irá continuar no cargo?
O mister finalmente retornará ao Brasil?
Iremos mesmo perdoar o 7x1?
Lista de treinadores - CBF
1º Ancelotti - italiano - 525.00 pontos
2º Jorge Jesus - português - 440.00 pontos
3º Joachim Low - alemão - 270.00 pontos
Ancelotti será o quarto estrangeiro a treinar o Brasil. Que honra para o italiano!
Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!

Case: 2

Input

4
Ancelotti
italiano
7
3
0.7
não
Jorge Jesus
português
4
6
0.8
sim
Sampaoli
argentino
Diniz
brasileiro
1
2
0.5
sim

Output

Será que Carleto irá continuar no cargo?
O mister finalmente retornará ao Brasil?
Um hermano comandando a seleção? Sai fora!
Lista de treinadores - CBF
1º Ancelotti - italiano - 595.00 pontos
2º Jorge Jesus - português - 560.00 pontos
3º Diniz - brasileiro - 110.00 pontos
O Ancelotti não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!
Jorge Jesus será o quarto estrangeiro a treinar o Brasil. Que honra para o português!
JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?