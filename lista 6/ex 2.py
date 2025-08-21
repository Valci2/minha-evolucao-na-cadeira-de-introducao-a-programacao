# irei armazenar os dicioinarios aqui 
lista_com_os_jogadores = []
nome_do_jogador = '' # para começar o loop

# loop para colocar todos os jogadores
while nome_do_jogador != 'FIM':
    
    # dicionario com os dados dos jogadores
    dados_do_jogador = {}
    nome_do_jogador = input() # input de dono dos jogodores
    dados_do_jogador['nome_do_jogador'] = nome_do_jogador
    
    # caso o input jogador seja fim ele não inicia o programa
    if nome_do_jogador != 'FIM':
        dados_do_jogador['disposicao'] = int(input()) # adiciona a dispoção do jogador dentro de uma chave no dicionario
        dados_do_jogador['posicao'] = input() # adiciona a posição
        
        # caso a disposição seja maior que 85
        if dados_do_jogador['disposicao'] >= 85:
        
            # caso o jogador seja atacante
            if dados_do_jogador['posicao'] == 'atacante':
                dados_do_jogador['chutes_para_gol'] = int(input()) # para colocar a quantidade de gol
                if dados_do_jogador['chutes_para_gol'] > 10:
                    print(f'{nome_do_jogador} está com um bom desempenho ofensivo.')
                else:
                    print(f'{nome_do_jogador} pode melhorar, Ancelotti pode usá-lo no segundo tempo.')
            
            # caso o jogador seja de qualquer outra posição que não atacante
            else:
                dados_do_jogador['chutes_ou_passes'] = int(input())
                if dados_do_jogador['chutes_ou_passes'] >= 20:
                    print(f'{nome_do_jogador} está com um bom desempenho de passes.')
                else:
                    print(f'{nome_do_jogador} pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.')
        
        # caso a disposição seja entre 50 e 84
        elif 50 <= dados_do_jogador['disposicao'] <= 84:
            dados_do_jogador['desepenho_do_ultimo_jogo'] = int(input())
            if dados_do_jogador['desepenho_do_ultimo_jogo'] > 80:
                print(f'O jogador {nome_do_jogador} pode ser escalado para a próxima partida.')
            else:
                print(f'Ancelotti precisa analisar o desempenho do {nome_do_jogador} na partida.')
        
        # caso seja abaixo de 50
        else:
            dados_do_jogador['desepenho_do_ultimo_treino'] = int(input())
            if dados_do_jogador['desepenho_do_ultimo_treino'] > 70:
                print(f'Ancelotti deve colocar {nome_do_jogador} para treinar mais.')
            else:
                print(f'{nome_do_jogador} não deveria estar na próxima convocação.')
        
        # adiciona todos os dados dos jogadores dentro de uma lista
        lista_com_os_jogadores.append(dados_do_jogador)


atacantes_prontos = 0 # contador para atacantes
defesores_prontos = 0 # contador para defesa

# loop para verificar as condicionais
for c in lista_com_os_jogadores:

    # para posição de atacante
    if c['posicao'] == 'atacante':
        if (c['disposicao'] >= 85 and c['chutes_para_gol'] > 10) or \
            (50 <= c['disposicao'] <= 84 and c['desepenho_do_ultimo_jogo'] > 80):
            atacantes_prontos += 1
    # caso seja outra posição
    else:
        if (c['disposicao'] >= 85 and c['chutes_ou_passes'] >= 20) or \
            (50 <= c['disposicao'] <= 84 and c['desepenho_do_ultimo_jogo'] > 80):
            defesores_prontos += 1
    
# prints finais
print('\nRelatório dos jogadores:')
print(f'Total de jogadores analisados: {len(lista_com_os_jogadores)}')
print(f'Atacantes prontos para começar: {atacantes_prontos}')
print(f'Meio-campistas e Defensores prontos para começar: {defesores_prontos}')