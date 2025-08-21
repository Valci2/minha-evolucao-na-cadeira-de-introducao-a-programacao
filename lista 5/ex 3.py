def sublista(lista_de_armas, afinidade, lista_do_up, indici=0):
    
    if indici < len(lista_do_up):

        nome = lista_de_armas[0]
        eh_normal_ou_especial = lista_de_armas[1]
        dano = int(lista_de_armas[2])
        atributo = lista_de_armas[3]

        if indici == 0:

            if atributo == 'físico':
                atributo = 'mágico'
            elif atributo == 'mágico':
                atributo = 'fogo'
            elif atributo == 'fogo':
                atributo = 'dourado'
            elif atributo == 'dourado':
                atributo = 'oculto'
            elif atributo == 'oculto':
                atributo = 'físico'

        atributo_que_vai_upar = lista_do_up[indici]

        if atributo_que_vai_upar == 'D':
            if 'destreza' in afinidade:
                dano += 1
            if atributo == 'físico':
                dano += 1
        
        if atributo_que_vai_upar == 'S':
            if 'força' in afinidade:
                dano += 1
            if atributo == 'fogo':
                dano += 1

        if atributo_que_vai_upar == 'I':
            if 'inteligência' in afinidade:
                dano += 1
            if atributo == 'mágico':
                dano += 1
        
        if atributo_que_vai_upar == 'F':
            if 'fé' in afinidade:
                dano += 1
            if atributo == 'dourado':
                dano += 1
        
        if atributo_que_vai_upar == 'A':
            if 'arcano' in afinidade:
                dano += 1
            if atributo == 'oculto':
                dano += 1

        if eh_normal_ou_especial == 'especial' and atributo_que_vai_upar == '-':
                dano += 5

        elif eh_normal_ou_especial == 'normal' and atributo_que_vai_upar == '+':
                dano += 3

        if isinstance(lista_do_up[indici], list):
            nova_lista, retorno_encontrado = sublista(lista_de_armas, afinidade, atributo_que_vai_upar)


            if not retorno_encontrado:
                return sublista(nova_lista, afinidade, atributo_que_vai_upar, indici + 1)
            
            else:
                print('Hmm, não acho que isso vai funcionar...')
                print(f'{nome}: {lista_de_armas[2]} -> {dano}')
                print(f'Afinidade revertida para {atributo}')

        if atributo_que_vai_upar == 'R':
            nova_lista = [nome, eh_normal_ou_especial, dano, atributo, afinidade]
            return nova_lista , True
        
        nova_lista = [nome, eh_normal_ou_especial, dano, atributo, afinidade]
        
        return sublista(nova_lista, afinidade, lista_do_up, indici + 1)
    
    else:

        return lista_de_armas, False

def atribuição(lista_das_armas, afinidade, lista_do_up, indici=0):
    
    if indici != len(lista_do_up):

        nome = lista_das_armas[0]
        normal_especial = lista_das_armas[1]
        dano = int(lista_das_armas[2])
        atributos = lista_das_armas[3]    

        atributo_que_vai_upar = lista_do_up[indici]

        if atributo_que_vai_upar == 'D':
            if 'destreza' in afinidade:
                dano += 1
            if atributos == 'físico':
                dano += 1
        
        if atributo_que_vai_upar == 'S':
            if 'força' in afinidade:
                dano += 1
            if atributos == 'fogo':
                dano += 1

        if atributo_que_vai_upar == 'I':
            if 'inteligência' in afinidade:
                dano += 1
            if atributos == 'mágico':
                dano += 1
        
        if atributo_que_vai_upar == 'F':
            if 'fé' in afinidade:
                dano += 1
            if atributos == 'dourado':
                dano += 1
        
        if atributo_que_vai_upar == 'A':
            if 'arcano' in afinidade:
                dano += 1
            if atributos == 'oculto':
                dano += 1

        if normal_especial == 'especial':
            if atributo_que_vai_upar == '-':
                dano += 5

        elif normal_especial == 'normal':
            if atributo_que_vai_upar == '+':
                dano += 3
        
        if isinstance(lista_do_up[indici], list):
            
            arma_com_sublista, retorno_encontrado = sublista(lista_das_armas, afinidade, atributo_que_vai_upar)
            
            if not retorno_encontrado:
                return atribuição(arma_com_sublista, afinidade, lista_do_up, indici + 1)
            
            else:
                print('Hmm, não acho que isso vai funcionar...')
                print(f'{nome}: {arma_com_sublista[2]} -> {dano}')
                print(f'Afinidade revertida para {atributos}')


        nova_lista = [nome, normal_especial, dano, atributos, afinidade]
    
        return atribuição(nova_lista, afinidade, lista_do_up, indici + 1)
    
    else:

        return lista_das_armas

def aprimorar(lista_de_armas, lista_dos_aprimoramentos, novas_armas = []):

    if len(lista_de_armas) > 0:
        lista_com_o_upgrade_da_nova_arma = atribuição(lista_de_armas[0], lista_de_armas[0][4:], lista_dos_aprimoramentos[0])
        novas_armas.append((lista_com_o_upgrade_da_nova_arma))
        print(f'{lista_de_armas[0][0]} aprimorado!')
        lista_de_armas.pop(0)
        lista_dos_aprimoramentos.pop(0)
        return aprimorar(lista_de_armas, lista_dos_aprimoramentos, novas_armas)

    if len(lista_de_armas) == 0:
        fogo = 0
        dourado = 0
        print('Inventário:')
        for c in novas_armas:
            print(f'- {c[0]}: {c[2]}')
            print(f'- afinidade: {c[3]}')
            if c[3] == 'fogo':
                print('Fogo... é uma das fraquezas da Malenia!!!')
                fogo += 1
            elif c[3] == 'dourado':
                print('É, não acho que uma arma de fé vá me ajudar muito...')
                dourado += 1
        print()
        return fogo, dourado


print('Não aguento mais morrer para a Malenia, Blade of Miquella...')
print('Vou refazer minha build!\n')

armas = []
aprimoramento = []
arma = ''
while 'finalizar' not in arma:
    arma = input().split(' - ')
    if 'finalizar' not in arma:
        armas.append(arma)

for _ in range(len(armas)):
    aprimoramento.append(eval(input()))

fogo, dourado = aprimorar(armas, aprimoramento)

if fogo > 0 and fogo > dourado:
    print('Muitas armas de fogo, ela não vai ter chance!')
elif dourado > 0 and dourado > fogo:
    print('Acho que vou ter que refazer meus aprimoramentos...')
else:
    print('Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!')