lista_dos_grupos = [] # lista para armazenas os dicinarios dos times
quantidade_de_grupos = int(input()) # input para a quantidade de grupos de 4 times

for grupos in range(quantidade_de_grupos): # faz um for para cada grupo
    lista = [] # lista para adicionar cada time individualmente
    for _ in range(4): # adiciona os cada times em uma dicionario, quanto passar os 4 times coloca os 4 times uma lista unica
        grupo = {}
        nome_pontuacao = input().split(' - ')
        grupo['time'] = nome_pontuacao[0]
        grupo['pontuacao'] = int(nome_pontuacao[1])
        lista.append(grupo)
    lista_dos_grupos.append(lista) # lista com todo o time para formar o grupo

# Fim da primeira parte
# ==========================================================================================================

# se a quantidade de grupos for impar
if quantidade_de_grupos % 2 == 1:
    print(f'Mas como que vamos fazer um torneio com {quantidade_de_grupos} grupos Samir!?')

# caso seja par
else:
    print('Roda os dados Samir!\n')
    
    # loop para saber os times que vão se enfrentar
    for confrontos in range(quantidade_de_grupos // 2):
        
        disputas = input().split(' x ')

        primeiro_time_que_vai_desputar = int(disputas[0])
        segundo_time_que_vai_desputar = int(disputas[1])

        # variaveis para armazenas as maiores pontuações de cada time
        time_com_maior_pontuacao_grupo_1 = 0
        time_com_segunda_maior_pontuacao_grupo_1 = 0
        nome_do_time_com_maior_pontuacao_grupo_1 = ''
        nome_do_time_com_segunda_maior_pontuacao_grupo_1 = ''

        # pega o primeiro grupo escolhido
        primeiro_grupo = lista_dos_grupos[primeiro_time_que_vai_desputar - 1]

        # loop para armazenar o time com maiores pontuações do grupo
        for times in primeiro_grupo:
            pontuacao = times['pontuacao']

            # armazena o mais forte
            if pontuacao > time_com_maior_pontuacao_grupo_1:

                # caso o primeiro time receba alguém com maior pontuação, o primeiro que era o mais forte vai passar a ser o segundo mais forte 
                time_com_segunda_maior_pontuacao_grupo_1 = time_com_maior_pontuacao_grupo_1
                nome_do_time_com_segunda_maior_pontuacao_grupo_1 = nome_do_time_com_maior_pontuacao_grupo_1

                nome_do_time_com_maior_pontuacao_grupo_1 = times['time']
                time_com_maior_pontuacao_grupo_1 = pontuacao

            # armazena o segundo mais forte
            elif pontuacao > time_com_segunda_maior_pontuacao_grupo_1:
                nome_do_time_com_segunda_maior_pontuacao_grupo_1 = times['time']
                time_com_segunda_maior_pontuacao_grupo_1 = pontuacao

        # ----------------------------- Mesma logica que do primeiro ----------------------------- #
        segundo_grupo = lista_dos_grupos[segundo_time_que_vai_desputar - 1]
        time_com_maior_pontuacao_grupo_2 = 0
        time_com_segunda_maior_pontuacao_grupo_2 = 0
        nome_do_time_com_maior_pontuacao_grupo_2 = ''
        nome_do_time_com_segunda_maior_pontuacao_grupo_2 = ''

        for times in segundo_grupo:
            pontuacao = times['pontuacao']

            if pontuacao > time_com_maior_pontuacao_grupo_2:
            
                time_com_segunda_maior_pontuacao_grupo_2 = time_com_maior_pontuacao_grupo_2
                nome_do_time_com_segunda_maior_pontuacao_grupo_2 = nome_do_time_com_maior_pontuacao_grupo_2
            
                nome_do_time_com_maior_pontuacao_grupo_2 = times['time']
                time_com_maior_pontuacao_grupo_2 = pontuacao
            
            elif pontuacao > time_com_segunda_maior_pontuacao_grupo_2:
                nome_do_time_com_segunda_maior_pontuacao_grupo_2 = times['time']
                time_com_segunda_maior_pontuacao_grupo_2 = pontuacao
     
        # printa os confrontos de cada grupo
        print(f'Confrontos chave {confrontos + 1}:')
        print(f'{nome_do_time_com_maior_pontuacao_grupo_1} x {nome_do_time_com_segunda_maior_pontuacao_grupo_2}')
        print(f'{nome_do_time_com_segunda_maior_pontuacao_grupo_1} x {nome_do_time_com_maior_pontuacao_grupo_2}\n')

    # Fim da segunda parte
    # ==========================================================================================================

    lista_de_rebaxamento = [] # lista com os times de menor pontuação

    # loop para armazenar os nomes dos times dentro da lista 'lista_de_rebaxamento'
    for _ in lista_dos_grupos: # for para cada grupo
        
        pontuacao = float('inf') # reseta a cada loop

        for times in _: # for para cada time
            if times['pontuacao'] < pontuacao:
                nome_do_time = times['time'] # armazena o nome
                pontuacao = times['pontuacao'] # aemazena a pontuação a cada time analizado

        # adiciona o nome do time após a verificação de pontuação
        lista_de_rebaxamento.append(nome_do_time)

    # print dos os nomes da lista de rebaixamento
    for nome_do_time_rebaixado in lista_de_rebaxamento:
        print(f'O time {nome_do_time_rebaixado} ficou em último lugar em seu grupo e foi rebaixado!')