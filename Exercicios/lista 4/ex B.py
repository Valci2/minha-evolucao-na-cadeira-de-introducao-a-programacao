def calculo_de_dano(ataque, motivacao, vida_do_alvo, nome):
    '''Calcula o dano causado por um ataque e retorna a nova vida do alvo.

        Argumentos:
        ataque (str): O tipo de ataque ('Potente' ou 'Normal').
        motivacao (int): O fator de motivação do atacante.
        vida_do_alvo (int): A vida atual do alvo.

    Retorna:
        int: A nova vida do alvo após o ataque.'''

    dano = 0.0
    if ataque == 'Potente':
        dano = motivacao * 40
        dano = int(dano)
        print(f'{nome} usou Golpe Potente e causou {dano} de dano!')
    elif ataque == 'Normal':
        dano = motivacao * 20
        dano = int(dano)
        print(f'{nome} usou Golpe Normal e causou {dano} de dano!')

    nova_vida = vida_do_alvo - dano
    return nova_vida

def iniciar_combate(nome_oponente, vida_inicial_oponente, motivacao_oponente_param, vida_vegeta_atual, motivacao_vegeta_param):
    '''Gerencia um combate entre Vegeta e um oponente.

    Argumentos:
        nome_oponente (str): O nome do oponente.
        vida_inicial_oponente (int): A vida inicial do oponente.
        motivacao_oponente_param (float): A motivação do oponente para este combate.
        vida_vegeta_atual (int): A vida atual de Vegeta.
        motivacao_vegeta_param (float): A motivação atual de Vegeta.

    Retorna:
        vida_vegeta_final (int): A vida de Vegeta ao final do combate.
        vencedor_vegeta (bool): True se Vegeta venceu, False caso contrário.
    '''
    motivacao_oponente = motivacao_oponente_param
    ataque_alternado = False
    vencedor_oponente = False
    vencedor_vegeta = False
    vida_do_oponente = vida_inicial_oponente
    turno = 1
    dois_potentes = 0
    vida_de_vegeta = vida_vegeta_atual
    motivacao_vegeta = motivacao_vegeta_param

    # print que indica com qual oponente o vegeta vai lutar
    print(f'\n--- Iniciando o combate contra {nome_oponente} ---\n')

    while not vencedor_vegeta and not vencedor_oponente:

        if not ataque_alternado:
            print(f'--- Turno {turno} ---') # printa o turno

        ataque = str(input()) # input para saber qual ataque (normal ou potente) o usuario vai querer usar

        if not ataque_alternado:  # Vegeta é o primeiro a atacar

            if ataque == 'Potente': 
                dois_potentes += 1 # caso ele dé um potente, o programa ingrementa +1 na variavel dois potentes para verificar se ele deu dois potentes seguidos
            elif ataque == 'Normal':
                dois_potentes = 0 # caso ele dé um potente e um normal a varivale dois potentes reseta e se torna zero denovo 

            # caso ele dé dois potentes sequidos ele perde na hora
            if dois_potentes >= 2: 
                vencedor_oponente = True
                print('Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!')
                print(f'|Vegeta: 0 HP vs {nome_oponente}: {vida_do_oponente} HP|\n')
                print(f'Vegeta foi derrotado! A Terra está a salvo graças a {nome_oponente}!')

            # caso ele não dé dois potentes ele segue o programa normal
            else:
                vida_do_oponente = calculo_de_dano(ataque, motivacao_vegeta, vida_do_oponente, 'Vegeta')
                ataque_alternado = True

                if vida_do_oponente <= 0:
                    print(f'|Vegeta: {vida_de_vegeta} HP vs {nome_oponente}: 0 HP|\n')
                    print(f'Vitória de Vegeta!\nVegeta venceu a batalha contra {nome_oponente} com {vida_de_vegeta} HP restantes!')
                    vencedor_vegeta = True
        
        # O oponente ataca
        elif ataque_alternado:  
            vida_de_vegeta = calculo_de_dano(ataque, motivacao_oponente, vida_de_vegeta, nome_oponente)
            ataque_alternado = False
            turno += 1

            if vida_de_vegeta <= 0: # Caso a vida de Vegeta chegue a ser igual ou menor que 0, ele zera o número negativo e o oponente é declarado vencedor
                vida_de_vegeta = 0
                vencedor_oponente = True
            elif vida_do_oponente <= 0:
                vida_do_oponente = 0

            print(f'|Vegeta: {vida_de_vegeta} HP vs {nome_oponente}: {vida_do_oponente} HP|\n')

            # printa na vez do oponente
            if vencedor_oponente:
                print(f'Vegeta foi derrotado! A Terra está a salvo graças a {nome_oponente}!')

    return vida_de_vegeta, vencedor_vegeta


# Inputs iniciais
motivacao_vegeta_inicial = float(input())
motivacao_oponente = float(input())
vegeta_venceu = False

# Variáveis iniciais
vida_de_vegeta = 100
motivacao_vegeta = motivacao_vegeta_inicial

# primeiro print do progrma
print('A saga de Vegeta começa!')

# Combate contra Piccolo
vida_de_vegeta, vegeta_venceu = iniciar_combate('Piccolo', 100, motivacao_oponente, vida_de_vegeta, motivacao_vegeta)

# Combate contra Gohan
if vegeta_venceu:
    vegeta_venceu = False
    motivacao_vegeta = (motivacao_vegeta * (1 + (vida_de_vegeta / 100))) # Atualiza a motivação com a vida restante
    vida_de_vegeta = 100
    motivacao_oponente = float(input())
    vida_de_vegeta, vegeta_venceu = iniciar_combate('Gohan', 100, motivacao_oponente, vida_de_vegeta, motivacao_vegeta)

# Combate contra Goku
if vegeta_venceu: # Verifica se Vegeta venceu Gohan para seguir para o combate com Goku
    vegeta_venceu = False
    motivacao_vegeta = (motivacao_vegeta * (1 + (vida_de_vegeta / 100))) # Atualiza a motivação com a vida restante
    vida_de_vegeta = 100
    motivacao_oponente = float(input())
    vida_de_vegeta, vegeta_venceu_goku = iniciar_combate('Goku', 200, motivacao_oponente, vida_de_vegeta, motivacao_vegeta) # Goku tem 200 de HP

    # Mensagem final se Vegeta vencer todos
    if vegeta_venceu_goku:
        print(f'\nVegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!')