def quantidade_de_letras(nome, nome2, tentativa=0):
    '''Faz a contagem de letras das duas strings para determinar as partes da fusão.

    Argumentos:
    nome (str): Nome do primeiro personagem.
    nome2 (str): Nome do segundo personagem.
    tentativa (int): Número da tentativa atual (0 para a primeira, 1 para a segunda, etc.).

    Retorna:
    parte do primeiro nome (str) e a parte do segundo nome (str).
'''

    # Listas para identificar os personagens envolvidos nos casos especiais de fusão
    caso_especial_um = ['Goten', 'Trunks']
    caso_especial_dois = ['Goku', 'Vegeta']
    especial = False # Flag para indicar se um caso especial foi ativado

    # Lógica específica para a primeira tentativa de fusão (tentativa 0)
    if tentativa == 0:
        # Verifica se os personagens correspondem a um dos casos de fusão especial (Gotenks ou Vegito)
        if nome in caso_especial_um and nome2 in caso_especial_um:
            print('Fusão realizada com sucesso! Gotenks entra em combate para derrotar o exército de vilões!')
            especial = True
            # Retorna o nome da fusão especial e uma string vazia para a segunda parte
            return 'Gotenks', ''
        elif nome in caso_especial_dois and nome2 in caso_especial_dois:
            print('Fusão realizada com sucesso! Vegito entra em combate para derrotar o exército de vilões!')
            especial = True
            # Retorna o nome da fusão especial e uma string vazia para a segunda parte
            return 'Vegito', ''

        # Se não for um caso especial, aplica as regras de corte de nome padrão para a primeira tentativa
        if not especial:
            # Determina a parte do primeiro nome com base no seu comprimento
            if len(nome) <= 4:
                # Se o nome tiver até 4 letras, pega apenas a primeira letra
                quantidade_de_letras_do_primeiro_nome = nome[0]
            else:
                # Se o nome tiver mais de 4 letras, calcula a metade arredondada para cima
                if len(nome) % 2 == 0:
                    resultado_da_divisao_primeira_string = int((len(nome) / 2))
                else:
                    resultado_da_divisao_primeira_string = int((len(nome) / 2) + 1)
                # Pega a parte inicial do nome até o ponto calculado
                quantidade_de_letras_do_primeiro_nome = nome[0:resultado_da_divisao_primeira_string]

            # Determina a parte do segundo nome com base no seu comprimento
            if len(nome2) <= 4:
                # Se o nome tiver até 4 letras, pega da segunda letra até o final
                quantidade_de_letras_do_segundo_nome = nome2[1:]
            elif len(nome2) > 4:
                # Se o nome tiver mais de 4 letras, calcula a metade arredondada para cima
                resultado_da_divisao_segunda_string = int((len(nome2) / 2) - 1)
                # Pega a parte final do nome a partir do ponto calculado
                quantidade_de_letras_do_segundo_nome = nome2[-resultado_da_divisao_segunda_string:]

    # Lógica específica para a segunda tentativa de fusão (tentativa 1)
    elif tentativa == 1:
        # Determina a parte do primeiro nome para a segunda tentativa
        if len(nome) <= 4:
            # Pega as duas primeiras letras se o nome for curto
            quantidade_de_letras_do_primeiro_nome = nome[0:2]
        else:
            # Calcula o ponto de corte para nomes mais longos
            if len(nome) % 2 == 0:
                resultado_da_divisao_primeira_string = int((len(nome) / 2 + 1))
            else:
                resultado_da_divisao_primeira_string = int((len(nome) / 2) + 2)
            # Pega a parte inicial do nome
            quantidade_de_letras_do_primeiro_nome = nome[0:resultado_da_divisao_primeira_string]

        # Determina a parte do segundo nome para a segunda tentativa
        if len(nome2) <= 3:
            # Pega as duas últimas letras (útil para nomes como 'Buu')
            quantidade_de_letras_do_segundo_nome = nome2[-2:]
        elif len(nome2) <= 4:
            # Pega as três últimas letras para nomes de 4 letras
            quantidade_de_letras_do_segundo_nome = nome2[-3:]
        elif len(nome2) > 4:
            # Calcula o ponto de corte para nomes mais longos
            resultado_da_divisao_segunda_string = int((len(nome2) / 2) + 1)
            # Pega a parte final do nome
            quantidade_de_letras_do_segundo_nome = nome2[resultado_da_divisao_segunda_string:]

    # Lógica específica para a terceira tentativa de fusão (tentativa 2)
    else: # tentativa == 2
        # Determina a parte do primeiro nome para a terceira tentativa
        if len(nome) <= 4:
            # Pega as duas primeiras letras se o nome for curto
            quantidade_de_letras_do_primeiro_nome = nome[0:2]
        else:
            # Calcula o ponto de corte para nomes mais longos
            if len(nome) % 2 == 0:
                resultado_da_divisao_primeira_string = int((len(nome) / 2))
            else:
                resultado_da_divisao_primeira_string = int((len(nome) / 2) + 1)
            # Pega a parte inicial do nome
            quantidade_de_letras_do_primeiro_nome = nome[0:resultado_da_divisao_primeira_string]

        # Determina a parte do segundo nome para a terceira tentativa
        if len(nome2) <= 3:
            # Pega o nome inteiro e o converte para minúsculas
            quantidade_de_letras_do_segundo_nome = nome2[0:]
            quantidade_de_letras_do_segundo_nome = quantidade_de_letras_do_segundo_nome.lower()
        elif len(nome2) == 4:
            # Pega da segunda letra até o final
            quantidade_de_letras_do_segundo_nome = nome2[1:]
        else:
            # Calcula o ponto de corte para nomes mais longos
            resultado_da_divisao_segunda_string = int(len(nome2) / 2)
            # Pega a parte final do nome
            quantidade_de_letras_do_segundo_nome = nome2[resultado_da_divisao_segunda_string:]
        
    return quantidade_de_letras_do_primeiro_nome, quantidade_de_letras_do_segundo_nome


def identificacao_de_consoante_e_vogais(primeira_parte_do_personagem, segunda_parte_do_personagem, nome_do_personagem):
    '''Verifica as condições de sucesso ou desastre de uma fusão com base nas partes dos nomes.

    Argumentos:
        primeira_parte_do_personagem (str): Parte inicial do nome do primeiro personagem.
        segunda_parte_do_personagem (str): Parte final do nome do segundo personagem.
        nome_do_personagem (str): O nome original do primeiro personagem (usado para determinar a equipe).

    Retorna:
        - bool: True se a fusão é um desastre (imperfeita), False caso contrário.
        - str: O nome completo da fusão.
        - int: O tipo de equipe (1 para heróis, 2 para vilões, 0 se for um desastre).
    '''
    # Listas de consoantes e vogais (incluindo maiúsculas e minúsculas) para verificação
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
                  'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    
    vogais = ['a', 'e', 'i', 'o', 'u',
              'A', 'E', 'I', 'O', 'U']

    # Concatena as partes dos nomes para formar o nome da fusão e capitaliza a primeira letra
    nome_da_fusao = (primeira_parte_do_personagem + segunda_parte_do_personagem).capitalize()

    # Verifica as condições para que a fusão seja considerada um "desastre" (imperfeita)
    if (primeira_parte_do_personagem[-1] in consoantes and segunda_parte_do_personagem[0] in consoantes) or \
       (primeira_parte_do_personagem[-1] in vogais and segunda_parte_do_personagem[0] in vogais) or \
       len(nome_da_fusao) <= 3: # Se a fusão tiver 3 ou menos caracteres

        print(f'A sincronização foi um desastre... {nome_da_fusao} é uma fusão imperfeita!')
        
        # Retorna True para desastre, o nome da fusão e 0 para indicar que não pertence a uma equipe
        return True, nome_da_fusao, 0

    # Se a fusão não foi um desastre, determina a equipe com base no primeiro personagem
    elif nome_do_personagem in herois:
        print(f'Fusão realizada com sucesso! {nome_da_fusao} entra em combate para derrotar o exército de vilões!')
        # Retorna False para não desastre, o nome da fusão e 1 para indicar a equipe de heróis
        return False, nome_da_fusao, 1
    
    elif nome_do_personagem in viloes:
        print(f'Fusão realizada com sucesso! {nome_da_fusao} entra em combate com sede de destruir Satan City!')
        # Retorna False para não desastre, o nome da fusão e 2 para indicar a equipe de vilões
        return False, nome_da_fusao, 2


def pontuacao(nome):
    '''Calcula a pontuação que uma fusão ganha com base no comprimento do seu nome.

    Argumento:
    nome (str): O nome da fusão.

    Retorna:
    int: A pontuação correspondente ao comprimento do nome.
    '''
    
    if len(nome) == 4:
        return 2000
    elif len(nome) == 5:
        return 2250
    elif len(nome) == 6:
        return 2500
    elif len(nome) == 7:
        return 2750
    elif len(nome) >= 8:
        return 3000
    # Retorna 0 para nomes com menos de 4 caracteres (geralmente fusões imperfeitas)
    return 0
    

def fusao(primeiro_nome, segundo_nome):
    '''Gerencia o processo completo de fusão entre dois personagens, incluindo tentativas e validações.

    Argumentos:
    primeiro_nome (str): Nome do primeiro personagem.
    segundo_nome (str): Nome do segundo personagem.

    Retorna:
        - int: Pontuação adicionada à equipe de heróis.
        - int: Pontuação adicionada à equipe de vilões.
        - str: Nome do primeiro personagem (para registro de participação).
        - str: Nome do segundo personagem (para registro de participação).
    '''
    
    desastre = True # Flag que indica se a fusão atual é um desastre
    tentativa = 0 # Contador de tentativas para a fusão

    # Tenta realizar a fusão por até 3 vezes (tentativas 0, 1, 2) ou até que não seja um desastre
    while tentativa <= 2 and desastre:
        
        ja_apareceu = False # Flag para verificar se um personagem já participou de outra fusão

        if desastre: # Continua no loop se a fusão ainda for um desastre

            # Verifica se algum dos personagens já está na lista de participantes de fusões anteriores
            if primeiro_nome in ja_participaram or segundo_nome in ja_participaram:
                # Imprime a mensagem de fusão inválida para o primeiro personagem, se aplicável
                if primeiro_nome in ja_participaram:
                    print(f'{primeiro_nome} já participou de uma fusão. Fusão inválida.')
                # Imprime a mensagem para o segundo personagem, se aplicável e o primeiro não foi o caso
                if segundo_nome in ja_participaram:
                    print(f'{segundo_nome} já participou de uma fusão. Fusão inválida.')
                
                tentativa = 3 # Força a saída do loop de tentativas
                ja_apareceu = True # Marca que um personagem já apareceu
                return 0, 0, '', '' # Retorna valores que indicam uma fusão inválida
            
            else:
                # Obtém as partes dos nomes para a fusão, dependendo da tentativa atual
                primeira_parte_do_nome, segunda_parte_do_nome = quantidade_de_letras(primeiro_nome, segundo_nome, tentativa)

                # Verifica se o resultado da 'quantidade_de_letras' é um dos casos especiais (Vegito ou Gotenks)
                if primeira_parte_do_nome == 'Vegito' or primeira_parte_do_nome == 'Gotenks':
                    desastre = False # A fusão é bem-sucedida neste caso
                    herois_viloes = 1 # Casos especiais são sempre heróis
                    nome_da_fusao = 'Gotenks' if primeira_parte_do_nome == 'Gotenks' else 'Vegito'
                
                else:
                    # Avalia a fusão normal usando a função de identificação de consoantes/vogais
                    desastre, nome_da_fusao, herois_viloes = identificacao_de_consoante_e_vogais(
                        primeira_parte_do_nome, segunda_parte_do_nome, primeiro_nome
                    )
                    tentativa += 1 # Incrementa o contador de tentativas

    # Após as tentativas, verifica o resultado final da fusão
    if desastre and not ja_apareceu:
        # Se a fusão ainda for um desastre e nenhum personagem já havia participado
        print('Aparentemente essa combinação é incompatível...')
        return 0, 0, '', '' # Retorna valores que indicam uma fusão falha
    
    elif not desastre and not ja_apareceu:
        # Se a fusão foi bem-sucedida e nenhum personagem já havia participado
        pontuação_da_equipe = pontuacao(nome_da_fusao) # Calcula a pontuação baseada no nome da fusão

        if herois_viloes == 1: # Se a fusão pertence à equipe de heróis
            return pontuação_da_equipe, 0, primeiro_nome, segundo_nome
        
        elif herois_viloes == 2: # Se a fusão pertence à equipe de vilões
            return 0, pontuação_da_equipe, primeiro_nome, segundo_nome


# Lista de todos os heróis que podem participar das fusões
herois = [
    'Gohan',
    'Goku',
    'Goten',
    'Kuririn',
    'Piccolo',
    'Tenshinhan',
    'Trunks',
    'Uub',
    'Vegeta',
    'Yamcha'
]

# Lista de todos os vilões que podem participar das fusões
viloes = [
    'Babidi',
    'Baby',
    'Broly',
    'Buu',
    'Cell',
    'Cooler',
    'Frieza',
    'Hit',
    'Janemba',
    'Zamasu'
]

# Lista para armazenar os nomes dos personagens que já participaram de uma fusão bem-sucedida
ja_participaram = []

# Pontuação total acumulada pela equipe de heróis
pontuacao_total_dos_herois = 0
# Pontuação total acumulada pela equipe de vilões
pontuacao_total_dos_viloes = 0

# --- Loop Principal do Jogo ---
# O jogo continua enquanto nenhuma das equipes atingir ou ultrapassar 8000 pontos
while pontuacao_total_dos_herois <= 8000 and pontuacao_total_dos_viloes <= 8000:
    
    # Solicita o nome do primeiro guerreiro para a fusão
    primeiro_personagem_para_fusão = str(input())
    compatibilidade = False

    # Confirmação da eleição do primeiro guerreiro, se ele for reconhecido
    if primeiro_personagem_para_fusão in herois:
        print(f'{primeiro_personagem_para_fusão} se elege para participar da fusão!')
    elif primeiro_personagem_para_fusão in viloes:
        print(f'{primeiro_personagem_para_fusão} se elege para participar da fusão!')

    # Solicita o nome do segundo guerreiro para a fusão
    segundo_personagem_para_fusão = str(input())

    if segundo_personagem_para_fusão in herois:
        print(f'{segundo_personagem_para_fusão} se elege para participar da fusão!')
    elif segundo_personagem_para_fusão in viloes:
        print(f'{segundo_personagem_para_fusão} se elege para participar da fusão!')

    # Confirmação da eleição do segundo guerreiro e verifica compatibilidade de facções
    if segundo_personagem_para_fusão in herois:
        # Se o primeiro personagem é um vilão e o segundo um herói, a fusão é incompatível
        if primeiro_personagem_para_fusão in viloes and primeiro_personagem_para_fusão not in ja_participaram:
            print('Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.')
        else:
            compatibilidade = True

    elif segundo_personagem_para_fusão in viloes:
        # Se o primeiro personagem é um herói e o segundo um vilão, a fusão é incompatível
        if primeiro_personagem_para_fusão in herois and primeiro_personagem_para_fusão not in ja_participaram:
            print('Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.')
        else:
            # Caso contrário, o segundo vilão é eleito
            compatibilidade = True

    # Tenta realizar a fusão e recebe as pontuações e os nomes dos participantes
    if compatibilidade:
        pontuacao_dos_herois, pontuacao_dos_viloes, participante1, participante2 = fusao(
            primeiro_personagem_para_fusão, segundo_personagem_para_fusão
        )

        # Atualiza as pontuações totais das equipes com base no resultado da fusão
        pontuacao_total_dos_herois += pontuacao_dos_herois
        pontuacao_total_dos_viloes += pontuacao_dos_viloes

        # Adiciona os personagens que participaram à lista de 'já participaram'
        # Esta lista é usada para evitar que o mesmo personagem participe de múltiplas fusões
        ja_participaram.append(participante1)
        ja_participaram.append(participante2)

# --- Mensagem Final do Jogo ---
# Determina o vencedor ou o desfecho do jogo com base nas pontuações finais
if pontuacao_total_dos_herois >= 8000:
    print('O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.')
elif pontuacao_total_dos_viloes >= 8000:
    print('Os vilões são fortes demais! Satan City está em apuros!')