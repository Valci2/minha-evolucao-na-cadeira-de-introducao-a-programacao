# inputs iniciais
jogador_1 = str(input())
jogador_2 = str(input())
num_sets_total = int(input())
nivel = str(input())

# inicio das variaveis
jogador1_escolhido = False
jogador2_escolhido = False

# caso os jogadores sejam um dos escolhidos
if jogador_1 == 'Luis' or jogador_1 == 'Lavoisier' or jogador_1 == 'Joab' or jogador_1 == 'Renan':
    jogador1_escolhido = True
if jogador_2 == 'Luis' or jogador_2 == 'Lavoisier' or jogador_2 == 'Joab' or jogador_2 == 'Renan':
    jogador2_escolhido = True

# inicio do programa
if jogador1_escolhido and jogador2_escolhido:
    print('Essa partida vai ser épica! O jogo vai ser emocionante!')

# condições de dificildade
rebatidas_maximas = 0
if nivel == 'aprendizes':
    rebatidas_maximas = 1
elif nivel == 'básicos':
    rebatidas_maximas = 2
elif nivel == 'amostradinhos':
    rebatidas_maximas = 3


# variaveis para armazernar as pontuações
sets_ganhos_jogador1 = 0
sets_ganhos_jogador2 = 0
num_set_atual = 1


# partidas
while sets_ganhos_jogador1 < (num_sets_total +1) // 2 and sets_ganhos_jogador2 < (num_sets_total + 1) // 2:

    print(f'Iniciando o {num_set_atual}º set')

    pontos_jogador1_set = 0
    pontos_jogador2_set = 0
    # Primeiro saque do set é do jogador 1
    sacador = jogador_1 
    fim_do_set = 0

    while fim_do_set == 0:
        
        print(f'O saque é de {sacador}')
        
        escolha = str(input())
        
        if escolha == 'saque':
            entrada1 = str(input())
            entrada2 = str(input())

            if entrada1 == 'SA' and entrada2 == 'AO':

                print('Um saque PERFEITO!!')
                num_rebatidas = 0
                ponto_concluido = 0
                rebate = False
                while num_rebatidas < rebatidas_maximas and ponto_concluido == 0:
                    
                    acao_rebate = str(input())

                    if acao_rebate == 'rebatida':
                        rebate = True

                    if rebate:
                        if acao_rebate == 'oponente rebateu':
                            num_rebatidas += 1

                        elif acao_rebate == f'{jogador_1} deixou a bola cair':
                            pontos_jogador2_set += 1
                            sacador = jogador_2
                            ponto_concluido = 1

                        elif acao_rebate == f'{jogador_2} deixou a bola cair':
                            pontos_jogador1_set += 1
                            sacador = jogador_1
                            ponto_concluido = 1

                if num_rebatidas == rebatidas_maximas:
                    
                    velocidade1 = int(input())
                    velocidade2 = int(input())

                    if velocidade1 < velocidade2:
                        pontos_jogador1_set += 1
                        sacador = jogador_1
                    else:
                        pontos_jogador2_set += 1
                        sacador = jogador_2


            # caso a bloca bate na propria area duas vezes
            elif entrada1 == 'SA' and entrada2 == 'SA':

                print(f'{sacador}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??')

                if sacador == jogador_1:
                    pontos_jogador2_set += 1
                    sacador = jogador_2
                    
                else:
                    pontos_jogador1_set += 1
                    sacador = jogador_1


            # caso a bola caia na area adversaria duas vezes
            elif entrada1 == 'AO' and entrada2 == 'AO':

                if jogador_1 == sacador:
                    print(f'Boa, {sacador}! Deu ponto de graça pro oponente!! Agora quem saca é {jogador_2}')

                else:
                    print(f'Boa, {sacador}! Deu ponto de graça pro oponente!! Agora quem saca é {jogador_1}')


                if sacador == jogador_1:
                    pontos_jogador2_set += 1
                    sacador = jogador_2

                else:
                    pontos_jogador1_set += 1
                    sacador = jogador_1

            # caso a bola pegue na rede
            elif entrada1 == 'REDE' or entrada2 == 'REDE':

                print('Vish, ainda bateu na rede')

                if sacador == jogador_1:
                    pontos_jogador2_set += 1
                    sacador = jogador_2

                else:
                    pontos_jogador1_set += 1
                    sacador = jogador_1

        # Verifica condição de fim de set
        if (pontos_jogador1_set >= 3) and (pontos_jogador1_set >= pontos_jogador2_set + 2) or (pontos_jogador2_set >= 3) and (pontos_jogador2_set >= pontos_jogador1_set + 2):
            
            if pontos_jogador1_set > pontos_jogador2_set:
                sets_ganhos_jogador1 += 1
                vencedor_set = jogador_1

            else:
                sets_ganhos_jogador2 += 1
                vencedor_set = jogador_2

            num_set_atual += 1
            fim_do_set = 1

# Determina o vencedor da partida
if sets_ganhos_jogador1 > sets_ganhos_jogador2:
    vencedor_partida = jogador_1
    
else:
    vencedor_partida = jogador_2

# printa depois de tudo
print(f'Depois de {num_sets_total} set(s) vibrante(s), o grande vencedor é {vencedor_partida}!!')
print('Fim do jogo!')