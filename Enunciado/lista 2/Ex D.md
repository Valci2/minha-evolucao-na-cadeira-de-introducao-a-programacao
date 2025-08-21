Após a última Copa do Mundo de Tênis de Mesa, os engenheiros do RoboCIn decidiram levar a robótica esportiva a um novo patamar. Eles desenvolveram o Hugo 4.0, um braço robótico avançado inspirado no lendário mesatenista Hugo Calderano. Seu objetivo? Treinar, desafiar e até mesmo superar jogadores humanos em uma simulação realista de partidas profissionais.

Agora, os estudantes precisam testar esse robô em uma batalha técnico-esportiva, onde um jogador real enfrenta o Hugo 4.0 em uma sequência de rebatidas. O robô aumentará sua força a cada segundo, mas atenção: se o robô ultrapassar o limite de força permitido, ele pode esgotar sua energia ou fazer a bola sair da mesa, de forma que o confronto deverá ser encerrado!

No tênis de mesa de alto rendimento, controlar o ritmo e a intensidade das rebatidas é essencial para manter a bola em jogo e forçar o erro do oponente. O Hugo 4.0 foi programado para simular esse comportamento com a seguinte equação de força aplicada:

    F_rebatida = força_inicial + (tempo × incremento)

Onde:

    F_rebatida: força aplicada pelo robô na rebatida atual
    forca_inicial: valor da primeira força aplicada pelo robô
    tempo: tempo da partida (em segundos), que pode ser calculada a partir da quantidade de rebatidas até o momento, pois o robô realiza uma rebatida por segundo
    incremento: valor fixo de aumento da força a cada segundo (o incremento será fixo para cada nível de dificuldade - informado mais abaixo na questão)

Regras da Partida

A simulação é finalizada assim que a força acumulada das rebatidas ultrapassar o limite máximo (F_max), definido na entrada do programa.

    Com o tempo iniciado em zero, a partida ocorre com o robô realizando uma rebatida por segundo, sendo aplicada uma força correspondente à calculada na equação acima;
    A força de uma rebatida não é válida se ultrapassar 150. Quando isso ocorrer, considera-se que a bola saiu da mesa e a partida deve ser encerrada imediatamente;
    Além da força de cada rebatida, que é calculada pela equação, o programa também deve contabilizar uma força acumulada, que representa a soma de todas as forças de rebatidas válidas até o momento (se a força de uma rebatida for maior que 150, ela não deve ser somada à força acumulada do robô);
    Se a força acumulada ultrapassar a F_max fornecida na entrada, a energia do robô é esgotada e o duelo termina.
    Seu programa também deve calcular a força média das rebatidas do robô, que será comparada com a força média do jogador (também fornecida na entrada do programa). A média do robô é uma equação simples:

    Força_media_robo = forca_acumulada / tempo_partida

Obs: A força média do robô deve ser calculada utilizando divisão inteira, desconsiderando qualquer parte decimal. Isso significa que o valor da média deve ser sempre um número inteiro. Por exemplo, se a força acumulada for 29 e o tempo for 2, então a média será 29 // 2 = 14, e não 14.5.

Comparando com a força média do jogador adversário, temos:

    Se a média do robô for maior: vitória do robô.
    Se for menor: vitória do jogador.
    Se forem iguais: empate técnico.

Input

Você receberá, na ordem:

    F_max

Um número inteiro F_max, representando a força acumulada máxima permitida.

    forca_inicial

Um número inteiro forca_inicial, que representa a força a ser usada na primeira rebatida.

    nivel

Uma string nivel, representando o nível de dificuldade do robô (facil, medio ou dificil).

    forca_media_jogador

Um número inteiro, representando a força média das rebatidas do jogador humano (que será comparada com a força média do robô para decidir o vencedor).

Output

Quando o programa iniciar, a seguinte mensagem deve ser mostrada:

    Robô Hugo 4.0 foi inicializado…

Após isso, você deve mostrar uma das seguintes frases abaixo de acordo com a dificuldade selecionada:

    Se a dificuldade for nível fácil, o incremento a ser usado na equação da força de cada rebatida deve ser igual a 1 e deve ser printado:

    Iniciando no modo iniciante... Ótimo para aquecer os motores!

    Se a dificuldade for média, o incremento deve ser igual a 3 e deve ser printado:

    Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!

    Se a dificuldade for nível difícil, o incremento deve ser igual a 5 e deve ser printado:

    Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!

A cada rebatida válida, o programa deve imprimir as seguintes informações:

    Rebatida {n}: força = {força_aplicada}, força acumulada = {forca_total}

A partida encerra quando:

A força acumulada ultrapassar F_max, visto que o robô esgotou sua energia:

    Energia do robô esgotada! Encerrando o confronto…

Ou quando a força de uma rebatida ultrapassar 150:

    Bola fora! A força da rebatida excedeu os limites da mesa.

Ao fim da partida:

Ao finalizar o programa, imprima o seguinte alerta:

    Partida finalizada! Estas são as estatísticas do embate:

Em seguida, mostre:

    O robô realizou {quantidade} rebatidas em {tempo} segundos, com força total de {forca_total}.

    Força média do robô: {forca_media_robo}

    Força média do jogador: {forca_media_jogador}

Obs.: Mesmo que a rebatida seja inválida, ela será considerada para a quantida de rebatidas e para o tempo.
Declarar vencedor:

    Se forca_media_robo for maior que forca_media_jogador:

    Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!

    Se forca_media_robo for menor que forca_media_jogador:

    Vitória do jogador! O talento humano ainda é imbatível!

    Se forca_media_robo for igual que forca_media_jogador:

    Empate técnico! Um duelo digno de mestres do tênis de mesa.

Examples

Case: 1

Input

300
20
dificil
30

Output

Robô Hugo 4.0 foi inicializado…
Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!
Rebatida 1: força = 25, força acumulada = 25
Rebatida 2: força = 30, força acumulada = 55
Rebatida 3: força = 35, força acumulada = 90
Rebatida 4: força = 40, força acumulada = 130
Rebatida 5: força = 45, força acumulada = 175
Rebatida 6: força = 50, força acumulada = 225
Rebatida 7: força = 55, força acumulada = 280
Rebatida 8: força = 60, força acumulada = 340
Energia do robô esgotada! Encerrando o confronto…
Partida finalizada! Estas são as estatísticas do embate:
O robô realizou 8 rebatidas em 8 segundos, com força total de 340.
Força média do robô: 42
Força média do jogador: 30
Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!

Case: 2

Input

200
10
medio
40

Output

Robô Hugo 4.0 foi inicializado…
Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!
Rebatida 1: força = 13, força acumulada = 13
Rebatida 2: força = 16, força acumulada = 29
Rebatida 3: força = 19, força acumulada = 48
Rebatida 4: força = 22, força acumulada = 70
Rebatida 5: força = 25, força acumulada = 95
Rebatida 6: força = 28, força acumulada = 123
Rebatida 7: força = 31, força acumulada = 154
Rebatida 8: força = 34, força acumulada = 188
Rebatida 9: força = 37, força acumulada = 225
Energia do robô esgotada! Encerrando o confronto…
Partida finalizada! Estas são as estatísticas do embate:
O robô realizou 9 rebatidas em 9 segundos, com força total de 225.
Força média do robô: 25
Força média do jogador: 40
Vitória do jogador! O talento humano ainda é imbatível!

Case: 3

Input

1000
150
facil
50

Output

Robô Hugo 4.0 foi inicializado…
Iniciando no modo iniciante... Ótimo para aquecer os motores!
Bola fora! A força da rebatida excedeu os limites da mesa.
Partida finalizada! Estas são as estatísticas do embate:
O robô realizou 1 rebatidas em 1 segundos, com força total de 0.
Força média do robô: 0
Força média do jogador: 50
Vitória do jogador! O talento humano ainda é imbatível!