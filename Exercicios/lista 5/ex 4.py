def tribonacci(n):
    '''Faz o calculo de Tribonacci
    
    Argumentos:
        n (int): numero a qual seja o indici

    retorna:
        faz o calculo de tribonacci  
    '''
    if n <= 1:
        return 0
    elif n <= 3:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci (n- 3)

def fatorial(n):
    '''Faz a fatorial de um número usando recursiva
    
    argumentos:
        n (int): numero a qual será feito o fatorial

    retorna:
        retorna o resultado do cálculo do fatorial em n
    '''
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)

def sequencia_de_catalan(n):
    '''Faz a sequencia de catalan indici de n
    
    argumentos:
        n (int): numero a qual seja o indici

    retorna:
        retorna o resultado do cálculo da sequencia de catalan
    '''
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 5
    else:
        return int(fatorial(2 * n) / (fatorial(n+1) * fatorial(n)))

def verificar_tribonacci(n, num=0, termo_tribunacci=0):
    '''verifica se o número desejado está dentro da sequencia de tribonacci
    
    argumentos:
        n (int): numero que deseja saber se faz ou nao parte da sequencia
        num (int): assume todos os numeros da sequencia ate o numero da sequencia ultrapassar n
        sequencia (lista): uma lista que adiciona todos os numeros da sequencia, para fazer a verificação se o numero esta ou não

    retorna:
        false se na tiver dentro da sequencia
        true se estiver dentro da sequencia
    '''

    if termo_tribunacci == n:
        return True
    elif termo_tribunacci > n:
        return False
    else:
        tribonacci_de_um_termo = tribonacci(num)
        return verificar_tribonacci(n, num + 1, tribonacci_de_um_termo)

def verificar_fatorial(n, num=0, termo_fatorial=-1):
    '''verifica se o numero desejado está dentro da sequencia de fatorial'''

    if termo_fatorial == n:
        return True
    elif termo_fatorial > n:
        return False
    else:
        fatorial_de_um_termo = fatorial(num)
        return verificar_fatorial(n, num + 1, fatorial_de_um_termo)

def verificar_sequencia_de_catalan(n, num=0, termo_catalan=-1):
    '''verifica se o número desejado está dentro da sequncia de catalan'''

    if termo_catalan == n:
        return True
    elif termo_catalan > n:
        return False
    else:
        termo_catalan = sequencia_de_catalan(num)
        return verificar_sequencia_de_catalan(n, num + 1, termo_catalan)
        
def tres_em_sequencia(lista_de_numeros):
    '''Verifica se há uma sequência de três números de Catalan consecutivos em uma lista.

    A função percorre a lista de números e checa se, em alguma posição,
    existem três números seguidos que fazem parte da sequência de Catalan.

    Args:
        numbers (list): Uma lista de números inteiros.

    Returns:
        bool: Retorna True e uma lista com os três números de catalan se encontrar três números de Catalan consecutivos.
              Retorna False e uma lista vazia caso contrário.
    '''

    # loop para a sequencia de três digitos, para verificar se os três números sequenciais fazem parte da sequencia de catalan
    for i in range(len(lista_de_numeros) - 2):
        primeiro_termo = lista_de_numeros[i]
        segundo_termo = lista_de_numeros[i+1]
        terceiro_termo = lista_de_numeros[i+2]

        # se o primeiro, segundo e terceiro fizerem parte o programa passa para a proxima parte
        if verificar_sequencia_de_catalan(primeiro_termo) and \
        verificar_sequencia_de_catalan(segundo_termo) and \
        verificar_sequencia_de_catalan(terceiro_termo):
            
            # se por um acaso o primeiro termo for < que o segundo termo e o segundo menor que o terceiro ele entra nesse if
            # caso especial, onde o número é [1 1 2] já que essa sequencia faz parte da sequencia de tribunacci
            if primeiro_termo < segundo_termo < terceiro_termo or \
            primeiro_termo == 1 and segundo_termo == 1 and terceiro_termo == 2:
                
                lista_dos_termos = [primeiro_termo ,segundo_termo ,terceiro_termo]
                return True, lista_dos_termos

    # caso nao encontre nenhum caso verdadeiro ele retorna uma false e uma lista vazia
    return False, []

def batalha(hp_do_personagem, vida_maxima, arsenal, nome_do_boss, hp_do_boss, dps_do_boss, vampirismo, turno=1):
    '''Faz a batalha entre o personagem e o boss, até um dos dois perecer ou o personagem ficar sem armas
    
    argumentos:
        hp_do_personagem (int): vida do personagem principal
        vida_maxima (int): vida max que o personagem principal tem
        arsenal (list): armas que estão contidas em seu arsenal
        nome_do_boss (str): nome do boss
        hp_do_boss (int): vida do boss
        dps_do_boss (int): dano do boss
        vampirismo (bool): caso a runa de malenia esteja ativo ele comecã a recuperar vida
        turno (int): quantidade de turno
    '''
    # caso a vida do personagem principal do boss ou armas for maior que 0, o programa continua
    while hp_do_personagem > 0 and hp_do_boss > 0 and len(arsenal) > 0:

        # pega o nome  
        nick_da_arma = arsenal[0][0]
        dps_da_arma = int(arsenal[0][1])

        # prints do inicio do turno
        print(f'{turno}° TURNO')
        print(f'Melhor conferir meus status antes de lutar -> vida: ({hp_do_personagem}/{vida_maxima})')
        print(f'E o {nome_do_boss} ainda está com {hp_do_boss} pontos de vida')
        print(f'Atacando com {nick_da_arma}.')
        print(f'Consegui causar {dps_da_arma} de dano no/a {nome_do_boss}!!!')
        print(f'Acabei consumindo a/o {nick_da_arma}, hora de pegar outra arma do arsenal.')
        arsenal.pop(0) # elimina a primeira arma da lista, para fazer o programa pegar a proxima arma

        # tira o hp do boss, baseado no dano da arma
        hp_do_boss -= dps_da_arma

        # caso a runa de malenia esteja ativo
        if vampirismo and turno > 1 and hp_do_boss > 0:
            hp_curado = 0
            
            if hp_do_personagem < (vida_max * 95/100):
                hp_curado = int(vida_max * 5/100)
                hp_do_personagem += hp_curado
                print(f'Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {hp_curado}')

            else:
                hp_curado = vida_max - hp_do_personagem
                hp_do_personagem += int(hp_curado)
                print(f'Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {hp_curado}')
        
        # caso o boss não tenha morrido
        if hp_do_boss > 0:
            hp_do_personagem -= dps_do_boss # ele ataca o personagem
            print(f'Droga {nome_do_boss} ainda não morreu, acabei recebendo {dps_do_boss} de dano.\n')

        # aumenta o turno
        turno += 1
        
    if hp_do_boss <= 0:
        print('\nGreat Enemy Felled')
        if len(arsenal) == 0:
            print(f'Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o {nome_do_boss}.')
        else:
            print(f'Finalmente depois de tanto me preparar consegui derrotar a/o {nome_do_boss}.')
            print(f"Acho que me preparei bem eu ainda tenho {len(arsenal)} arma/as sobrando são ela/as: {', '.join(c[0] for c in arsenal)}.")

    else:
        if hp_do_personagem <= 0:
            print('You Died')
            print(f'Droga acabei morrendo para a/o {nome_do_boss} e ele ainda tem {hp_do_boss} pontos de vida, vou ter que trazer armas mais fortes da próxima vez.')
        elif len(arsenal) <= 0:
            print(f'Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o {nome_do_boss} ainda tem {hp_do_boss} pontos de vida, vou ter que me preparar mais da próxima vez.')

# flags
recuperacao_de_vida = False # flag para saber se a runa de malenia está ativada
dano_para_todas_as_armas = False # flag para saber se o dano precisa ir para todas as armas

armas = [] # lista para colocar todas as armas que o usuario colocar

# inputs e variaveis iniciais 
nome_vida = input().split(' - ')
nome = nome_vida[0]
vida_max = int(nome_vida[1])
acoes = int(input())

# Faz um loop até a quantidade de ações desejadas
for c in range(acoes):
    escolha = input().split(' - ')

    # caso, seja um arma
    if len(escolha) >= 3:

        nivel_total = 0 # vai mudando com a quantidade de upgrades da arma
        nome_da_arma = escolha[0]
        dano_da_arma = int(escolha[1])
        tipo_da_arma = escolha[2]

        # prints iniciais
        print(f'Vou levar a/o {nome_da_arma} ela/e vai ser de grande ajuda.')
        print('Hora de Aprimorar!!!')

        # loop para colocar os números do aprimoramento
        aprimoramento = ''
        while aprimoramento != 'fim':
            
            aprimoramento = input() 
            if aprimoramento.isnumeric(): # se caso, o input de aprimoramento for um número ele avança o programa, coloque isso, para diferencias, os int dá str 'fim'
                
                # logicá para as armas basicas
                if tipo_da_arma == 'basica':
                    verifica_se_a_aprimoramento = verificar_tribonacci(int(aprimoramento)) # verifica se o número faz parte da sequencia de tribunacci
                    if verifica_se_a_aprimoramento and nivel_total < 20: # se o número fizer parte da sequencia e o nivel da arma não for maior que 20 adiciona mais um no nível atual dele
                        nivel_total += 1
                        dano_da_arma += (dano_da_arma * 10/100) # dano da arma aumenta em 10% a cada nível
                        print(f'Pronto, consegui mais um nível agora a/o {nome_da_arma} está no nível {nivel_total}!')

                # logicá para as armas especiais
                elif tipo_da_arma == 'especial':
                    verifica_se_a_aprimoramento = verificar_fatorial(int(aprimoramento)) # verifica se o número faz parte de um número fatorial válido
                    if verifica_se_a_aprimoramento and nivel_total < 10: # se o número fizer parte de um fatorial valido e seu nivel da arma for menor que 10 adiciona mais 1 em seu nivel atual
                        nivel_total += 1
                        dano_da_arma += (dano_da_arma * 20/100) # dano da arma aumenta 20% a cada nivel
                        print(f'Pronto, consegui mais um nível agora a/o {nome_da_arma} está no nível {nivel_total}!')
        
        # caso a arma tenha upado pelo menos um nível, ele printa isso
        if nivel_total > 0:
            print(f'Agora sim! Acho que a/o {nome_da_arma} está forte o suficiente, consegui colocar ele/a para o nível {nivel_total}\n')
        
        # caso não, ele printa isso
        else:
            print(f'Droga não consegui aumentar o nível da/o {nome_da_arma}\n')

        dano_da_arma = int(dano_da_arma) # arredonde o dano da arma, que foi incrementado com porcentagens.
        armas.append([nome_da_arma, dano_da_arma]) # adiciona a arma em uma lista

    # caso seja uma runa
    elif len(escolha) == 1:

        # print inicial para toda runa
        print('A batalha vai ser difícil melhor tentar ativar uma runa!')

        # print especifico de cada runa
        if escolha[0] == 'Grande Runa de Radahn':
            print(f'Me decidi vou tentar ativar a Grande Runa de Radahn, mais vida vai ajudar muito.')
        elif escolha[0] == 'Grande Runa de Morgott':
            print(f'Me decidi vou tentar ativar a Grande Runa de Morgott, quanto mais vida melhor.')
        elif escolha[0] == 'Grande Runa de Godrick': 
            print(f'Me decidi vou tentar ativar a Grande Runa de Godrick, acho que um pouco de tudo não é nada mal.')
        elif escolha[0] == 'Grande Runa de Malenia':
            print(f'Me decidi vou tentar ativar a Grande Runa de Malenia, ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez.')

        # logica para saber se a runa foi ativada
        numeros = []
        for c in range(10): # faz um loop de 10 números
            numeros.append(int(input())) # cada número é adicionado na lista
        tem_tres_na_sequencia, para_o_print_da_sequencia = tres_em_sequencia(numeros) # faz a verificação se exestem 3 numeros sequidos que estão dentro da sequencia de catalan

        # caso a runa seja ativada
        if tem_tres_na_sequencia:

            print('Isso consegui ativar a Grande Runa.')
            print(f"Acabei precisando apenas dos números: {para_o_print_da_sequencia[0]} - {para_o_print_da_sequencia[1]} - {para_o_print_da_sequencia[2]}.\n")

            # logica de ativação de cada runa
            if escolha[0] == 'Grande Runa de Radahn':
                vida_max += int(vida_max * 15/100)
            elif escolha[0] == 'Grande Runa de Morgott':
                vida_max += int(vida_max * 25/100)
            elif escolha[0] == 'Grande Runa de Godrick': 
                dano_para_todas_as_armas = True
                vida_max += int(vida_max * 10/100)
            elif escolha[0] == 'Grande Runa de Malenia':
                recuperacao_de_vida = True

        else:
            print('Caramba não consegui ativar a Grande Runa, infelizmente vou ter que me contentar com as armas que vou levar.\n')

# aprimora o dano de todas as armas se a runa de Grande Runa de Godrick for ativa
if dano_para_todas_as_armas:
    if len(armas) > 0:
        for c in armas:
            c[1] *= (110/100)
            c[1] = int(c[1])       

# input do boss
boss = input().split(' - ')
nick_do_boss = boss[0]
vida_do_boss = int(boss[1])
dano_do_boss = int(boss[2])

# função para a batalha
batalha(vida_max, vida_max, armas, nick_do_boss, vida_do_boss, dano_do_boss, recuperacao_de_vida)