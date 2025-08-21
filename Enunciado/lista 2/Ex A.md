Está chegando o torneio de Tênis de Mesa do InterCIn, o campeonato mais aguardado do ano! Você, um excelente mesatenista do CIn, se inscreveu para participar. Com o desejo de chegar preparado para enfrentar qualquer adversário, você decidiu iniciar uma intensa rotina de treinos antes do grande evento.

Imagem InterCin

Para isso, foi necessário chamar um amigo de confiança para te ajudar nos treinos. Durante as sessões, vocês criaram um sistema de acompanhamento para medir a sua evolução. A ideia é simples: a cada bola lançada por seu amigo, ela será classificada como um atributo de Ataque ou de Defesa. Se a bola foi rebatida com sucesso, será ganho x pontos no respectivo atributo.

Para garantir um acompanhamento justo, vocês decidiram que, no início do treino, tanto o atributo de Ataque quanto o de Defesa começarão em 0 pontos.

Ao final da sessão, vocês querem saber quantos pontos foram acumulados em cada um dos atributos.

Input

Inicialmente, você receberá uma quantidade N de bolas que deverão ser rebatidas:

    N (int)

Após isso, para cada bola lançada, serão informados o seu tipo e o golpe executado:

    tipo_bola_lançada (str)

    golpe_executado (str)

Cada bola que for lançada poderá ser do tipo Ataque ou Defesa. Para o caso da bola ser de Defesa, os possíveis golpes são Chop e Push, já se for de Ataque, os possíveis golpes são Topspin e Smash, sendo:

    Push: +5 pontos no atributo de defesa;
    Chop: +10 pontos no atributo de defesa;
    Topspin: +5 pontos no atributo de ataque;
    Smash: +10 pontos no atributo de ataque;

Porém, ainda existe a possibilidade de você errar o golpe. Nesse caso, a entrada recebida para o golpe executado será Errou, e funciona da seguinte maneira:

    Se a bola lançada for de Ataque: -10 pontos no atributo de ataque;
    Se a bola lançada for de Defesa: -10 pontos no atributo de defesa;

    OBS 1: Não existem casos que o golpe executado não seja correspondente com o tipo de bola lançada.

    OBS 2: Ao final do programa, antes de comparar os valores de ataque e defesa, verifique se algum deles é negativo - se for, defina-os como 0, pois nunca haverá ataque ou defesa negativa.

Output

Logo no início do código, você deverá printar a seguinte frase:

    ------- Início do Treino -------

Para cada bola rebatida, caso você acerte o golpe, deverá ser printada a frase:

    Você conseguiu rebater uma bola de {bola_lançada}! Golpe executado: {golpe_executado}.

Porém, caso você erre o golpe, seu programa deverá printar:

    Você errou! Levanta a cabeça que ainda tem mais.

Ao final do código, deverá ser expresso:

Caso seu atributo de ataque seja maior que o de defesa, printe:

    Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!

Já para o caso do seu atributo de defesa ser maior que o de ataque, printe:

    Defesa ganha campeonatos! Agora sim estou preparado.

Por fim, se ambos forem iguais, printe:

    Foi um treino equilibrado.

Após isso, caso você erre pelo menos uma bola durante o treino, printe:

    Infelizmente não foi um treino perfeito, mas pude melhorar muito.

Por fim, deverão ser printados os seus atributos finais da seguinte forma:

    ------- Atributos -------

    Ataque: {atributo_ataque} (int)

    Defesa: {atributo_defesa} (int)

Examples

Case: 1

Input

3
Ataque
Smash
Ataque
Smash
Defesa
Chop

Output

------- Início do Treino -------
Você conseguiu rebater uma bola de Ataque! Golpe executado: Smash.
Você conseguiu rebater uma bola de Ataque! Golpe executado: Smash.
Você conseguiu rebater uma bola de Defesa! Golpe executado: Chop.
Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!
------- Atributos -------
Ataque: 20
Defesa: 10

Case: 2

Input

4
Defesa
Chop
Defesa
Chop
Defesa
Errou
Defesa
Errou

Output

------- Início do Treino -------
Você conseguiu rebater uma bola de Defesa! Golpe executado: Chop.
Você conseguiu rebater uma bola de Defesa! Golpe executado: Chop.
Você errou! Levanta a cabeça que ainda tem mais.
Você errou! Levanta a cabeça que ainda tem mais.
Foi um treino equilibrado.
Infelizmente não foi um treino perfeito, mas pude melhorar muito.
------- Atributos -------
Ataque: 0
Defesa: 0