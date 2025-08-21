def descriptografia(criptografia):
    '''Faz a descriptografia do nome forcecido pelo usuario
    
    argumentos: 
        criptografia (str): recebe um nome que esteja criptografado

    retorna:
        descriptografia (str): retorna o nome descriptografado
    '''
    # lista ascii para descriptografia
    ascii_chars = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
    ]

    # variaveis que vão receber strings depois
    segunda_metade_com_shift = ''
    descriptografia = ''

    # pega a exatamente a medade da quantidades de letras que tem na string
    metade = len(criptografia) // 2
    primeira_metade = criptografia[:metade] # divide entra a primeira (caso a quantidade de letras seja impar ele pega menos uma letra)
    segunda_metade = criptografia[metade:] # e a segunda metade da string

    # pega o index cada letras da segunda parte e para pegar a proxima letra da lista ascii 
    for letras in segunda_metade:
        index_na_lista = ascii_chars.index(letras)
        if index_na_lista == 94:
            index_na_lista = -1
        segunda_metade_com_shift += ascii_chars[index_na_lista + 1] 
    
    # junta a primeira parte (original) e a segunda parte (com shift +1)
    tudo_junto = primeira_metade + segunda_metade_com_shift
    tudo_junto = tudo_junto[::-1] # pega a junção e inverte

    # pega todas as letras do string completa e faz um shift (-3) para chegarmos na descriptografia
    for letras in tudo_junto:
        index_na_lista = ascii_chars.index(letras)
        if index_na_lista == 2:
            index_na_lista = 91
        elif index_na_lista == 1:
            index_na_lista = 90
        elif index_na_lista == 0:
            index_na_lista = 89
        descriptografia += ascii_chars[index_na_lista - 3]

    # retorna a palavra descriptografada
    return descriptografia


lista_dos_nomes = [] # lista para armazenar todas os dicinarios
tecnico_encontrado = False # flag para saber se a um tecnico

quantidade_de_jogadores = int(input()) # input para quantidade de jogadores

if 1 <= quantidade_de_jogadores <= 25:

    for _ in range(quantidade_de_jogadores): # loop para adicionar a quantidade de jogadores desejados
        
        # reseta o dicionario para cada input
        dicionario_dos_nomes = {}

        # input da string criptografada
        nome_criptografado = input()
        # descriptografa usando um a função
        nome_descriptografado = descriptografia(nome_criptografado)

        # cria as keys para o nome descriptografado e criptografado
        dicionario_dos_nomes['nome_criptografado'] = nome_criptografado
        dicionario_dos_nomes['nome_descriptografado'] = nome_descriptografado
        # adiciona em uma lista, cada um dos dicionarios
        lista_dos_nomes.append(dicionario_dos_nomes)

        # print para cada nome descriptografado e criptografado
        print(f'Criptografada: {dicionario_dos_nomes["nome_criptografado"]}')
        print(f'Descriptografada: {dicionario_dos_nomes["nome_descriptografado"]}')
        print('-' * 50)

# pega todos os nomes dos dicionarios que estão na lista
for  c in lista_dos_nomes:
    if c['nome_descriptografado'] == 'Ronaldo':
        print('Ronaldo Fenômeno detectado! Autor dos gols na final!')
    elif c['nome_descriptografado'] == 'Ronaldinho':
        print('Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...')
    elif c['nome_descriptografado'] == 'Cafu':
        print('Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!')
    elif c['nome_descriptografado'] == 'Marcos':
        print('Marcos está na área! O paredão do Brasil em 2002!')
    elif c['nome_descriptografado'] == 'Luiz Felipe Scolari':
        print('Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!')
    else:
        print(f"{c['nome_descriptografado']} está confirmado na escalação!")

print() # print para pular linha
# se tiver menos de 11 jogadores contando (com o tecnico)
if len(lista_dos_nomes) < 11:
    print('!!!!!!!!!! Escalação incompleta! !!!!!!!!!!')
    print(f'Só foram encontrados {len(lista_dos_nomes) - 1} jogadores. Faltam jogadores para completar o time.') # descontando o tecnico
    for c in lista_dos_nomes:
        if c['nome_descriptografado'] == 'Luiz Felipe Scolari':
            tecnico_encontrado = True
else:
    # caso a quantidade de jogadores (contando com o tecnico) seja maior que 11
    print('++++++++++ Escalação Confirmada ++++++++++')
    print('Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002')
    print('==================================================')
    for c in lista_dos_nomes: # verifica cada nome de cada jogador e tecnico
        if c['nome_descriptografado'] != 'Luiz Felipe Scolari':
            print(f"->{c['nome_descriptografado']}")
        else:
            tecnico_encontrado = True
    print('==================================================')

# caso o não tenhamos o tecnico
if not tecnico_encontrado:
    print('!!!!!!!!!! Técnico não encontrado! !!!!!!!!!!')
    print('Como vamos jogar sem treinar? Como vamos ganhar o penta?')
# caso tenhamos
else:
    print('========== Técnico ==========')
    print('Luiz Felipe Scolari (Felipão)')
    if len(lista_dos_nomes) - 1 >= 11:
        print('===== Tudo pronto! Rumo ao Penta! =====')
        print('Escalação completa com técnico confirmado.')
        print('Que comece o espetáculo, Brasil rumo ao penta!')