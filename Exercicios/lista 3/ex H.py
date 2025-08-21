# listas e variaveis que vou utilizar
teen_team = ['rex splode', 'duplikate', 'atom eve', 'robot']
equipe_dos_viltros = [['general kregg',110],['conquista',100], ['anissa', 90]]
membros_mais_fortes = [['', 0], ['', 0], ['', 0]]
maior_poder = [0]
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
alfabeto_codificado = ['k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c', ' ']
equipes_principais = []
todo_teen_team = False
forca = 0

# quantidade de equipes (sublistas) que vai ter na lista de equipes principais
quantidade_de_listas = int(input())
for quantidade_de_equipes in range(quantidade_de_listas):
    equipes_principais.append([0])

# loop para colocar todos os herois desejados
escolha_do_que_fazer = ''
while escolha_do_que_fazer != 'FIM':

    nome_decodificado = ''
    contador = 0
    parou = False
    
    # input para escolher se quer adicionar um personagem, metamorfosear ou finalizar
    escolha_do_que_fazer = str(input())

    # caso ele queira adicionar um personagem novo
    if escolha_do_que_fazer == 'adicionar':

        print('Quem será o próximo integrante do time?')
        # input para o nome e o poder dos personagens
        nome_poder = str(input()).split(' - ')
        nome_codificado = nome_poder[0] 

        # faz um for no nome para analizar cada caractere
        for letras in nome_codificado:

            # faz a decodificação das caracteres
            index_alfabeto_codificado = alfabeto_codificado.index(letras)
            nome_decodificado += alfabeto[index_alfabeto_codificado]
            
            if len(nome_decodificado) == len(nome_codificado):

                # printa se um dos teen team entrar em alguma equipe
                if nome_decodificado == 'rex splode':
                    print('Eu vou te detonar!') # isso não é do detona ralph?

                elif nome_decodificado == 'atom eve':
                    print('Eu reescrevo a matéria... incluindo a SUA.')
                
                elif nome_decodificado == 'duplikate':
                    print('Quantas de mim você acha que consegue lidar?')

                elif nome_decodificado == 'robot':
                    print('Minha lógica diz que você vai perder.')

                # adicionar as informações dentro de uma lista na lista das equipes
                equipe = int(input())
                equipes_principais[equipe].append(nome_decodificado)
                equipes_principais[equipe].append(int(nome_poder[1]))

                # o poder total de cada equipe é atualizado a cada membro que entra
                equipes_principais[equipe][0] += int(nome_poder[1])

    # caso o metaforfo apareça
    elif escolha_do_que_fazer == 'metamorfo':
        
        # pede os imputs e printa o que tem que printar
        print('Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?')
        nome_para_troca = str(input())

        print('Quem você gostaria de colocar no lugar?')
        nome_e_poder = str(input()).split(' - ')

        nome_codificado = nome_e_poder[0]
        nome_decodificado = ''

        for letras in nome_codificado:

            # faz a decodificação das caracteres
            index_alfabeto_codificado = alfabeto_codificado.index(letras)
            nome_decodificado += alfabeto[index_alfabeto_codificado]

        # printa se tiver um menbro do teen team 
        if nome_decodificado == 'rex splode':
            print('Eu vou te detonar!') 

        elif nome_decodificado == 'atom eve':
            print('Eu reescrevo a matéria... incluindo a SUA.')
        
        elif nome_decodificado == 'duplikate':
            print('Quantas de mim você acha que consegue lidar?')

        elif nome_decodificado == 'robot':
            print('Minha lógica diz que você vai perder.')

        # procura o nome do personagem que desejamos trocar em todas as sublistas
        for procura_de_nome in equipes_principais:
            
            if nome_para_troca in procura_de_nome and not parou:

                # pega os index do nome e poder do personagem
                index_do_nome = procura_de_nome.index(nome_para_troca)
                index_poder = index_do_nome + 1

                # subtrai o poder do heroi removido do poder total da equipe
                subtracao = equipes_principais[contador][index_poder]
                equipes_principais[contador][0] -= subtracao

                # remove o nome e o poder do personagem desejado
                equipes_principais[contador].pop(index_poder)
                equipes_principais[contador].pop(index_do_nome)

                parou = True

            contador += 1
            
        equipe = int(input())
        
        equipes_principais[equipe].append(nome_decodificado)
        equipes_principais[equipe].append(int(nome_poder[1]))
        equipes_principais[equipe][0] += int(nome_poder[1])


# testa equipe por equipe (sublista) uma variavel para guardar a equipe com o maior poder
for poder in equipes_principais:

    if len(poder) > 0:

        # faz a verificação para saber se todos os personagens do teen team estão em uma equipe
        if 'rex splode' in poder and 'atom eve' in poder and 'duplikate' in poder and 'robot' in poder:

            # pega o index de cada um dos teem time
            index_rex = poder.index('rex splode') + 1
            index_eve = poder.index('atom eve') + 1
            index_duplikate = poder.index('duplikate') + 1
            index_robot = poder.index('robot') + 1

            # aqui ele acrescenta 10% a todo mundo
            poder[0] += (10 / 100) * poder[index_rex]
            poder[index_rex] += (10 / 100) * poder[index_rex]

            poder[0] += (10 / 100) * poder[index_eve]
            poder[index_eve] += (10 / 100) * poder[index_eve]

            poder[0] += (10 / 100) * poder[index_duplikate]
            poder[index_duplikate] += (10 / 100) * poder[index_duplikate]

            poder[0] += (10 / 100) * poder[index_robot]
            poder[index_robot] += (10 / 100) * poder[index_robot]
            todo_teen_team = True

        # faz a verificação do poder total de cada equipe
        if poder[0] > maior_poder[0]:
            maior_poder[0] = poder[0]
            equipe_com_maior_poder = poder

# deleta poder total de cada time (final não precisaremos mais)
equipe_com_maior_poder.pop(0)

# caso o teen team esteja completo ele printa isso
if todo_teen_team:
    print('O teen team esta completo, Cecil esta muito contente!')

# contador para na hora do for só coletar o nome na hora que for para coletar o nome e o poder na hora do poder
contador = 0
for membros in equipe_com_maior_poder:
    if contador % 2 == 0: # se o contador for par ele pega o nome
        nome = membros
    else:
        if membros > membros_mais_fortes[0][1]: # caso seja impar ele verifica se o poder do primeiro membro (agora nada) é maior 
            membros_mais_fortes[0][0] = nome
            membros_mais_fortes[0][1] = membros
    
    contador += 1

# fiz a mesma coisa porque o prazo ta curto
contador = 0
for membros in equipe_com_maior_poder:
    if contador % 2 == 0:
        nome = membros
    else:
        if membros > membros_mais_fortes[1][1] and nome not in membros_mais_fortes[0][0]:
            membros_mais_fortes[1][0] = nome
            membros_mais_fortes[1][1] = membros

    contador += 1

# pro terceiro também
contador = 0
for membros in equipe_com_maior_poder:
    if contador % 2 == 0:
        nome = membros
    else:
        if membros > membros_mais_fortes[2][1] and nome not in membros_mais_fortes[0][0] and nome not in membros_mais_fortes[1][0]:
                membros_mais_fortes[2][0] = nome
                membros_mais_fortes[2][1] = membros
    
    contador += 1

# print dos herois mais poderosos
print(f'Aqui está o poderoso time da terra: {membros_mais_fortes[0][0]}, {membros_mais_fortes[1][0]}, {membros_mais_fortes[2][0]}')

# variaveis para saber a equipe vencedora
vitorias_herois = 0
vitorias_viltro = 0

# printa os três duelos
print(f'1 Duelo: {membros_mais_fortes[0][0]} X {equipe_dos_viltros[0][0]}')
print(f'2 Duelo: {membros_mais_fortes[1][0]} X {equipe_dos_viltros[1][0]}')
print(f'3 Duelo: {membros_mais_fortes[2][0]} X {equipe_dos_viltros[2][0]}')

# verifica qual equipe venceu
if membros_mais_fortes[0][1] > equipe_dos_viltros[0][1]:
    vitorias_herois += 1
else:
    vitorias_viltro += 1
if membros_mais_fortes[1][1] > equipe_dos_viltros[1][1]:
    vitorias_herois += 1
else:
    vitorias_viltro += 1

if membros_mais_fortes[2][1] > equipe_dos_viltros[2][1]:
    vitorias_herois += 1
else:
    vitorias_viltro += 1

# printa a equipe vencedora
if vitorias_herois > vitorias_viltro:
    print('A terra venceu!')
elif vitorias_viltro > vitorias_herois:
    print('Infelizmente o imperio viltrumita conquistou a terra!')

