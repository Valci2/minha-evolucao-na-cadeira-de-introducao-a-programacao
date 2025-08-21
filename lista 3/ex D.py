# listas iniciais
primeiro_tipo_de_zord = []
segundo_tipo_de_zord = []
terceiro_tipo_de_zord = []

# variveis iniciais
robocin = False
cont = 0
passou = False

print('Go! Go! Power Rangers!')

zords = str(input()).split('-')

# se o robocin tiver no time o programa nem roda
if 'robocin' in zords:
    print('Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!')
    robocin = True

else:

    # vai passa por cada zord do split, para adicionar cada um em seu devido tipo
    for nome_e_poder in zords:

        if cont % 2 == 0:
            nome = nome_e_poder # pega o nome do zord

        elif cont % 2 == 1:
            poder = int(nome_e_poder) # pega o poder do zord
            passou = True

        cont += 1 # contador para pegar primeiro o nome e depois o poder

        if passou:
            passou = False
            
            # adicionar zord por zord na lista
            if poder > 30:    
                primeiro_tipo_de_zord.append([nome, poder])
            elif 10 < poder <= 30:
                segundo_tipo_de_zord.append([nome, poder])
            else:
                terceiro_tipo_de_zord.append([nome, poder])       

    # Ordena o tipo 1
    n = 0
    while n < len(primeiro_tipo_de_zord):
        j = 0
        while j < len(primeiro_tipo_de_zord) - n - 1:
            if primeiro_tipo_de_zord[j][1] < primeiro_tipo_de_zord[j+1][1]:
                temp = primeiro_tipo_de_zord[j]
                primeiro_tipo_de_zord[j] = primeiro_tipo_de_zord[j+1]
                primeiro_tipo_de_zord[j+1] = temp
            j += 1
        n += 1

    # Ordena o tipo 2
    n = 0
    while n < len(segundo_tipo_de_zord):
        j = 0
        while j < len(segundo_tipo_de_zord) - n - 1:
            if segundo_tipo_de_zord[j][1] < segundo_tipo_de_zord[j+1][1]:
                temp = segundo_tipo_de_zord[j]
                segundo_tipo_de_zord[j] = segundo_tipo_de_zord[j+1]
                segundo_tipo_de_zord[j+1] = temp
            j += 1
        n += 1

    # Ordena o tipo 3
    n = 0
    while n < len(terceiro_tipo_de_zord):
        j = 0
        while j < len(terceiro_tipo_de_zord) - n - 1:
            if terceiro_tipo_de_zord[j][1] < terceiro_tipo_de_zord[j+1][1]:
                temp = terceiro_tipo_de_zord[j]
                terceiro_tipo_de_zord[j] = terceiro_tipo_de_zord[j+1]
                terceiro_tipo_de_zord[j+1] = temp
            j += 1
        n += 1

# caso o robocin não esteja no split
if not robocin:

    # strings já prontas para se caso um ranger ficar sem zord
    ranger_vermelho = 'Ranger Vermelho ficou sem zord!'
    ranger_verde =  'Ranger Verde ficou sem zord!'
    ranger_rosa = 'Ranger Rosa ficou sem zord!'
    ranger_preto = 'Ranger Preto ficou sem zord!'
    ranger_azul = 'Ranger Azul ficou sem zord!'
    ranger_amarela = 'Ranger Amarela ficou sem zord!'

    # se por um acaso só tiver 1 zord, ele fica para o primeiro
    # caso contrario, o primeiro zord (o mais forte) fica com o primeiro ranger
    # o segundo mais forte de cada categoria fica com o segundo renger
    if len(primeiro_tipo_de_zord) >= 1:
        ranger_vermelho = 'Zord do Ranger Vermelho: ' + primeiro_tipo_de_zord[0][0]

    if len(primeiro_tipo_de_zord) >= 2:
        ranger_verde = 'Zord do Ranger Verde: ' + primeiro_tipo_de_zord[1][0]

    if len(segundo_tipo_de_zord) >= 1:
        ranger_rosa = 'Zord da Ranger Rosa: ' + segundo_tipo_de_zord[0][0]

    if len(segundo_tipo_de_zord) >= 2:
        ranger_preto = 'Zord do Ranger Preto: ' + segundo_tipo_de_zord[1][0]

    if len(terceiro_tipo_de_zord) >= 1:
        ranger_azul = 'Zord do Ranger Azul: ' + terceiro_tipo_de_zord[0][0]

    if len(terceiro_tipo_de_zord) >= 2:
        ranger_amarela = 'Zord da Ranger Amarela: ' + terceiro_tipo_de_zord[1][0]

    print(ranger_vermelho)
    print(ranger_verde)
    print(ranger_rosa)
    print(ranger_preto)
    print(ranger_azul)
    print(ranger_amarela)

    # printa todos os zords de cada tipo, caso não tenha printa outra coisa
    if len(primeiro_tipo_de_zord) > 0:
        print(f"Zords do tipo 1: {', '.join([zord[0] for zord in primeiro_tipo_de_zord])}")
    else:
        print('Não temos nenhum zord do tipo 1 :(')

    if len(segundo_tipo_de_zord) > 0:
        print(f"Zords do tipo 2: {', '.join([zord[0] for zord in segundo_tipo_de_zord])}")
    else:
        print('Não temos nenhum zord do tipo 2 :(')

    if len(terceiro_tipo_de_zord) > 0:
        print(f"Zords do tipo 3: {', '.join([zord[0] for zord in terceiro_tipo_de_zord])}")
    else:
        print('Não temos nenhum zord do tipo 3 :(')

    # se todos os ranger tiverem um zord ele printa
    if ranger_vermelho[0] == 'Z' and \
        ranger_verde[0] == 'Z' and \
        ranger_rosa[0] == 'Z' and \
        ranger_preto[0] == 'Z' and \
        ranger_azul[0] == 'Z' and \
        ranger_amarela[0] == 'Z':
        print('Os Rangers estão prontos para montar o Megazord e derrotar Rita!')

    # caso não, ele printa isso
    else:
        print('Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!')