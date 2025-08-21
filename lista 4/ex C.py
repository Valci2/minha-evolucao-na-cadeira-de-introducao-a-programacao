def calcular_poder(tecnica):
    '''
    Calcula o poder (dano) de uma técnica baseando-se no comprimento da string.
    '''

    return len(tecnica) % 8

def verifica_entrada_terceiro_personagem(lutador1, lutador2, lista_inimigos_com_ajuda):
    '''
    Verifica se um terceiro personagem deve entrar na batalha.
    Retorna True se sim, False caso contrário.
    '''

    for equipe in lista_inimigos_com_ajuda:
        # Verifica se ambos os lutadores estão presentes na mesma equipe
        if lutador1 in equipe and lutador2 in equipe:
            return True
    return False

# input para quantidade de partidas
quantidade_de_partidas = int(input())

# print inicial
print(f'O torneio do poder irá começar com {quantidade_de_partidas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!')

# lista com os nomes dos personagens que vão ter uma maozinha se enfrentarem seus respectivos adversarios
nomes_dos_que_precisam_de_ajuda = ['Goku', 'Frieza', 'Gohan', 'Androide 17']
inimigos_com_ajuda = [['Goku', 'Jiren'], ['Frieza', 'Jiren'], ['Gohan', 'Namekuseijins'], ['Androide 17', 'Ribrianne']]

# loop na quantidade de partidas que vai ter
for c in range(quantidade_de_partidas):
    

    recebeu_ajuda = 0 # variavel para indentificar quem vai receber ajudar

    nome_lutador1, tecnica_lutador1 = str(input()).split(' - ')
    nome_lutador2, tecnica_lutador2 = str(input()).split(' - ')
    
    poder_da_primeira_habilidade = calcular_poder(tecnica_lutador1)
    poder_da_segunda_habilidade = calcular_poder(tecnica_lutador2)

    # faz a verificação para identificar se o terceiro personagem vai entrar
    terceiro_personagem_entra = verifica_entrada_terceiro_personagem(nome_lutador1, nome_lutador2, inimigos_com_ajuda)

    # se tiver 3 personagens
    if terceiro_personagem_entra:
        
        # recebe o nome e a tecnica do terceiro lutador
        nome_lutador3, tecnica_lutador3 = str(input()).split(' - ')

        print(f'A intensidade dos dois lutadores motivou {nome_lutador3} a entrar na batalha também!')
        
        poder_da_terceira_habilidade = calcular_poder(tecnica_lutador3)

        # verifica qual o personagem que vai receber a ajuda
        if nome_lutador1 in nomes_dos_que_precisam_de_ajuda:
            poder_da_primeira_habilidade += poder_da_terceira_habilidade
            recebeu_ajuda = 1 # Lutador 1 recebeu ajuda
        else:
            poder_da_segunda_habilidade += poder_da_terceira_habilidade
            recebeu_ajuda = 2 # Lutador 2 recebeu ajuda

        # Lógica para determinar o vencedor da batalha de 3
        if recebeu_ajuda == 1 and poder_da_primeira_habilidade > poder_da_segunda_habilidade:
            print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {tecnica_lutador1}, {tecnica_lutador2} e {tecnica_lutador3}! A batalha acaba com {nome_lutador1} e {nome_lutador3} no topo!')
        
        elif recebeu_ajuda == 2 and poder_da_segunda_habilidade > poder_da_primeira_habilidade:
            print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {tecnica_lutador1}, {tecnica_lutador2} e {tecnica_lutador3}! A batalha acaba com {nome_lutador2} e {nome_lutador3} no topo!')
        
        elif recebeu_ajuda == 2 and poder_da_primeira_habilidade > poder_da_segunda_habilidade:
            print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {tecnica_lutador1}, {tecnica_lutador2} e {tecnica_lutador3}! A batalha acaba com {nome_lutador1} no topo!')
        
        else: # Se o lutador 1 não recebeu ajuda, ou se receberam mas o lutador 2 venceu
            print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {tecnica_lutador1}, {tecnica_lutador2} e {tecnica_lutador3}! A batalha acaba com {nome_lutador2} no topo!')

    else: # Caso não tenha terceiro personagem
        
        if poder_da_primeira_habilidade > poder_da_segunda_habilidade:
            print(f'Incrível! {nome_lutador1} mostrou sua força e defenderá seu universo até o final!')
        else:
            print(f'Incrível! {nome_lutador2} mostrou sua força e defenderá seu universo até o final!')