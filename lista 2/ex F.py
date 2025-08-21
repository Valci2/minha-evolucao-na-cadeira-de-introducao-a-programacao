quant = int(input()) # vai ser a quantidade de vezes que o loop deve se repetir.
jogador = str(input()) # vai armazenar quem começou.
vezes = pontuacao_jaob = pontuacao_Luvusier = comeca = mesa = fim = partida_perfeita = 0
objeto = ''


# inicio do programa
print('Vamos dar início à disputa!!! TOMADA!!!')

# print diferente para cada jogador
if jogador == 'Jaob':
    print('Jaob veio de Catende e está pronto para vencer!!!')
elif jogador == 'Luvusier':
    print('Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!')


# vai fazer o loop até a quantidade de vezes que o usuario desejar
while vezes < quant:

    # variaveis que resetam
    erro = acerto = pontuacao = 0

    # só printa quanto o uma nova rodada começar
    if comeca == 0 or fim > 0:
        print(f'COMEÇA A {vezes+1}ª RODADA!')
        fim -= 1
        comeca = 1


    # objeto que o jogador vai acertar
    objeto = str(input())

    if objeto == 'mesa':
        print(f'{jogador} jogou a bolinha no(a) mesa!')
        if jogador == 'Jaob':
            mesa = 1
            jogador = 'Luvusier'
        elif jogador == 'Luvusier':
            mesa = 1
            jogador = 'Jaob'

    # para o programa progredir o jogador precisa da mesa quando uma partida começar
    if mesa > 0:

        # define o objeto que ele vai acertar
        if objeto == 'Baralho de UNO':
            print(f'{jogador} jogou a bolinha no(a) {objeto}!')
            pontuacao += 2
            acerto += 1
            vezes += 1
            mesa = 0


        elif objeto == 'Armário de Homero e Elena':
            print(f'{jogador} jogou a bolinha no(a) {objeto}!')
            acerto += 1
            vezes += 1
            pontuacao += 3
            mesa = 0


        elif objeto == 'Peça de Dominó':
            print(f'{jogador} jogou a bolinha no(a) {objeto}!')
            acerto += 1
            vezes += 1
            pontuacao += 3
            mesa = 0


        elif objeto == 'Baralho de Coup Desaparecido':
            print(f'{jogador} achou o Coup!!! Ele merece a vitória sem dúvidas!')
            acerto += 1
            vezes = quant
            pontuacao += 100
            partida_perfeita = 1
            mesa = 0


        elif objeto == 'Projetor':
            print(f'{jogador} jogou a bolinha no(a) {objeto}!')
            vezes += 1
            erro += 1
            pontuacao -= 2
            mesa = 0


        elif objeto == 'Computador':
            print(f'{jogador} jogou a bolinha no(a) {objeto}!')
            vezes += 1
            erro += 1
            pontuacao -= 3
            mesa = 0


        elif objeto == 'Cabeça do Amiguinho':
            print(f'{jogador} jogou a bolinha no(a) {objeto}!')
            vezes += 1
            erro += 1
            pontuacao -= 5
            mesa = 0


        elif objeto == 'Nada':
            print(f'{jogador} jogou a bolinha no(a) {objeto}!')
            vezes += 1
            erro += 1
            pontuacao -= 1
            mesa = 0


    # contabiliza a pontuação dos jogadores
    if jogador == 'Jaob':
        pontuacao_jaob += pontuacao

        # caso o a pontuação seja < 0 a pontuação dos jogadores vai voltar a ser 0
        if pontuacao_jaob < 0:
            pontuacao_jaob = 0

    elif jogador == 'Luvusier':
        pontuacao_Luvusier += pontuacao
        if pontuacao_Luvusier < 0:
            pontuacao_Luvusier = 0


    # printa se o jogador acertar ou errar

    if acerto > 0:

        # aqui diferencei os jogadores por causa das pontuações diferentes de cada um
        if jogador == 'Jaob':
            print(f'{jogador} teve uma grande pontaria e acertou {objeto}! Agora está com {pontuacao_jaob} pontos.')
        else:
            print(f'{jogador} teve uma grande pontaria e acertou {objeto}! Agora está com {pontuacao_Luvusier} pontos.')
        fim = 1


    # caso o jogador 'errar', nesse caso, ele acerta um objeto que faz ele perder ponto
    elif erro > 0:

        if jogador == 'Jaob':
            print(f'{jogador} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontuacao_jaob} pontos.')
        else:
            print(f'{jogador} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontuacao_Luvusier} pontos.')
        fim = 1

        # se ele acertar um objeto que faz ele perder ponto o jogador troca
        if jogador == 'Luvusier':
            jogador = 'Jaob'
        elif jogador == 'Jaob':
            jogador = 'Luvusier'


# quando o programa chegar no final ele printa isso.
print('\nTEMOS O RESULTADO DA PARTIDA!')


# se o jogador consegui acertar o COUP perdido ele. 
if partida_perfeita > 0:
       print(f'{jogador} achou o Coup!!! Ele merece a vitória sem dúvidas!')


# caso ele não encontre o COUP.       
else:
    if pontuacao_jaob > pontuacao_Luvusier:
        print(f'Jaob deu orgulho à Catende e ganhou a disputa com {pontuacao_jaob} pontos!')
    elif pontuacao_Luvusier > pontuacao_jaob:
        print(f'A química está em festa, Luvusier ganha a disputa com {pontuacao_Luvusier} pontos!')
    else:
        print('Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!')