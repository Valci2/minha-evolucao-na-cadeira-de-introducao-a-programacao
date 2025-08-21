def batalha(hp_do_personagem, forca_do_personagem, copia_do_hp_do_personagem, hp_boss, forca_do_boss, hp_copia_do_boss, nome_do_boss, nivel_do_jogador, tentativas=1, primeiro_print=False):
    '''Faz a batalha contra o chefe e retorna a quantidade de tentativas que foram necessarias para derrotalo
    
    argumentos:
        vitalidade (int): vida do personagem
        forca (int): forca do personagem
        vitalidade_boss (int): vida do boss
        forca_boss (int): forca do boss
        vitalidade_copia_do_boss (int): copia da vida do boss
        boss (str): nome do boss
        dificildade (str): em qual dificildade a gameplay vai estar
        copia_da_vitalidade (int): copia da vitalidade do personagem
        tentativas (str): variavel das tentativas que recebe um a cada tentativa nova

    retorna:
        tentativas: quantidade de tentativas ate derrotar o boss
    '''
    # condição de parada. caso o boss perca.
    if hp_boss <= 0:
        return tentativas
    
    else:
        if hp_do_personagem <= 0 and hp_boss > 0:
            if nivel_do_jogador == 'Iniciante':
                forca_do_personagem = forca_do_personagem + (forca_do_personagem* 5/100) # caso a dificuldade seja iniciante ele adiciona 5% do total da forca atual
                forca_do_boss = forca_do_boss - (forca_do_boss * 10/100) # retira 10% da forca do boss
            
            elif nivel_do_jogador == 'Veterano': 
                forca_do_personagem = forca_do_personagem + (forca_do_personagem * 10/100) # agora é 10%.
                forca_do_boss = forca_do_boss - (forca_do_boss * 20/100) # retira 20% da forca do boss
            
            elif nivel_do_jogador == 'Mestre do Souls':
                forca_do_personagem = forca_do_personagem + (forca_do_personagem * 20/100) # agora e 20%
                forca_do_boss = forca_do_boss - (forca_do_boss * 33/100) # retira 33% das forca do boss
            
            # caso o boss ainda esteja vivo chama a função denovo
            return batalha(copia_do_hp_do_personagem, forca_do_personagem, copia_do_hp_do_personagem, hp_copia_do_boss, forca_do_boss, hp_copia_do_boss, nome_do_boss, nivel_do_jogador, tentativas + 1, primeiro_print)
    
    # enquanto a vida do boss e a vida do personagem é maior que zero continua o loop
    while hp_boss > 0 and hp_do_personagem > 0:

        # se o boss for o Sif
        if nome_do_boss == 'Sif, a Grande Loba Cinzenta':

            hp_boss -= forca_do_personagem # ele retira da vida do boss a quantidade de forca do personagem

            if hp_boss < (hp_copia_do_boss * 10/100) and not primeiro_print: # se a vida do boss for menor que 10% dá vida máxima
                print('Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!')
                forca_do_boss -= 15 # ele perde 15 pontos no dps
                primeiro_print = True # flag para printar apenas uma vez
            
            if hp_boss > 0: # caso o boss seja derrotado antes, o boss não tera a possibilidade de atacar
                hp_do_personagem -= forca_do_boss # ele retira da vida do personagem a quantidade de forca do boss

        # se o boss for for o Gwyn
        elif boss == 'Gwyn, Lorde das Cinzas':
            
            hp_boss -= forca_do_personagem
            
            if hp_boss < (hp_copia_do_boss * 50/100) and not primeiro_print: # se a vida do atual do Gwyn for menor que 50% da vida maxima dele e caso ele não tenha consigo os 10 pontos extras naquela partida, ele comeca a dar mais 10 pontos de dano
                forca_do_boss += 10
                primeiro_print = True
            
            if hp_boss > 0:
                hp_do_personagem -= forca_do_boss
            
    return batalha(hp_do_personagem, forca_do_personagem, copia_do_hp_do_personagem, hp_boss, forca_do_boss, hp_copia_do_boss, nome_do_boss, nivel_do_jogador, tentativas, primeiro_print)
        

# inputs e variaveis iniciais
dificildade = input()
status = input().split(' ')
vitalidade = int(status[0]) * 20
forca = int(status[1]) * 5
boss = input()

# batalha caso o boss seja sif
if boss == 'Sif, a Grande Loba Cinzenta':
    
    # sempre printa no começo da batalha com o boss
    print('Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!')

    # variaveis de vida e forca
    vitalidade_boss = 3432 # vida do boss
    forca_boss = 35 # forca do boss
    total_de_tentativas = batalha(vitalidade, forca, vitalidade, vitalidade_boss, forca_boss, vitalidade_boss, boss, dificildade) # faz o calculo de tentativas necessarias para derrotar o boss

    print(f'Você precisou de {total_de_tentativas} tentativas para vencer o(a) Sif, a Grande Loba Cinzenta!') # printa a quantidade de tentativas para derrotar o boss

    # printa de acordo com a dificuldade e com a quantidade de tentativas
    if dificildade == 'Iniciante':
        if total_de_tentativas <= 5:
            print('Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!')
        elif 5 < total_de_tentativas <= 10:
            print('Até que não foi tão ruim assim, continue assim novato!')
        else:
            print('Bem vindo a Dark Souls.')

    elif dificildade == 'Veterano':
        if total_de_tentativas <= 5:
            print('Você já andou por Lordran antes, não é? Impressionante.')
        elif 5 < total_de_tentativas <= 10:
            print('Nada mal, guerreiro. Mas os próximos desafios não terão piedade.')
        else:
            print('Mesmo os veteranos sangram em Dark Souls...')
    
    elif dificildade == 'Mestre do Souls':
        if total_de_tentativas == 1:
            print('Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!')
        elif 1 < total_de_tentativas <= 10:
            print('Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...')
        else:
            print('Nem mesmo os Mestres escapam ilesos da chama...')
            
    # sempre printa no final da batalha
    print('A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.')

# batalha caso o boss seja gwyn
elif boss == 'Gwyn, Lorde das Cinzas':

    # sempre printa no começo da batalha com o boss
    print('Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!')

    # variaveis de vida e forca
    vitalidade_boss = 4185
    forca_boss = 55
    total_de_tentativas = batalha(vitalidade, forca, vitalidade, vitalidade_boss, forca_boss, vitalidade_boss, boss, dificildade)

    print(f'Você precisou de {total_de_tentativas} tentativas para vencer o(a) Gwyn, Lorde das Cinzas!')
    
    if dificildade == 'Iniciante':
        if total_de_tentativas <= 5:
            print('Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!')
        elif 5 < total_de_tentativas <= 10:
            print('Até que não foi tão ruim assim, continue assim novato!')
        else:
            print('Bem vindo a Dark Souls.')
    
    elif dificildade == 'Veterano':
        if total_de_tentativas <= 5:
            print('Você já andou por Lordran antes, não é? Impressionante.')
        elif 5 < total_de_tentativas <= 10:
            print('Nada mal, guerreiro. Mas os próximos desafios não terão piedade.')
        else:
            print('Mesmo os veteranos sangram em Dark Souls...')
    
    elif dificildade == 'Mestre do Souls':
        if total_de_tentativas == 1:
            print('Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!')
        elif 1 < total_de_tentativas <= 10:
            print('Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...')
        else:
            print('Nem mesmo os Mestres escapam ilesos da chama...')

    # printa no final da batalha
    print('A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...')
    
    # printa de acordo com a quantidade de tentativas independente da dificuldade
    if total_de_tentativas == 1:
        print('O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...')
    else:
        print('Mas o ciclo... o ciclo continua.')