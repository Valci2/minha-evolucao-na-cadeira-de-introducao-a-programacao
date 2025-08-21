def prefixado(num_prefixados):
    '''Faz as operacões prefixadas
    
    argumentos:
        num_prefixado (str): o número préfixado desejado

    retorna:
        o valor inteiro de cada expressao
    '''
    pilha = []
    operacao = num_prefixados.split()

    for numeros in operacao[::-1]:
        
        if numeros.isnumeric():
            pilha.append(int(numeros))

        else:

            operando1 = pilha.pop()
            operando2 = pilha.pop()
            
            if numeros == '+':
                pilha.append(operando1 + operando2)
            elif numeros == '-':
                pilha.append(operando1 - operando2)
            elif numeros == '*':
                pilha.append(operando1 * operando2)
            elif numeros == '/':
                pilha.append(operando1 // operando2) 

    return pilha.pop() # retorna o ultimo digito depois de fazer as operações


def numero_primo(num):
    '''Faz a verificação do número, se ele tiver 2 divisores entre um range de 0 ate ele, ele será considerado primo
    
    argumento:
        num (int): número inteiro

    retorna:
        se número for primo retorna: true
        se número nao for primo retona: false
    '''

    total_de_divisoes = 0
    for c in range(1, num+1):
        if num % c == 0:
            total_de_divisoes += 1
    
    if total_de_divisoes == 2:
        return True
    return False
    

def binario_decimal(binario_str):
    '''Faz a trasformação de binario para decimal'''
    return int(binario_str, 2)


def Processar_coordenada(expressoes, matriz):
    '''Faz o processamento das coordenadas das estrelas encontradas'''

    string_binaria = ''
    for expr in expressoes:
        resultado = prefixado(expr)
        if numero_primo(resultado):
            string_binaria += '1'
        else:
            string_binaria += '0'

    valor_decimal = binario_decimal(string_binaria)
    coordenada = valor_decimal % matriz

    return coordenada, string_binaria


def encontrar_esfera_mais_proxima(posicao_atual, dados_esferas):
    '''Faz o calculo da distancia euclidiana de cada uma das esferas, 
    depois do calculo ele verifica qual tem a menor distancia, caso sejam iguais
    ele prioriza o primeiro que aparece'''

    distancia_minima = float('inf') # faz uma varivel com valor infinito (vi no gustavo guanabara)
    indice_esfera_mais_proxima = -1

    for i, esfera in enumerate(dados_esferas):
        sx, sy, _, _ = esfera # Extrai as coordenadas (x, y) da esfera
        # Calcula a distância euclidiana
        distancia = (((sx - posicao_atual[0])**2 + (sy - posicao_atual[1])**2) ** 0.5)
        
        # Se a distância for menor, atualiza a esfera mais próxima
        if distancia < distancia_minima:
            distancia_minima = distancia
            indice_esfera_mais_proxima = i
        # Em caso de empate na distância, usa a ordem original de decodificação como critério
        elif distancia == distancia_minima:
            # Se ainda não houver uma esfera mais próxima ou se a atual foi decodificada antes
            if indice_esfera_mais_proxima == -1 or i < indice_esfera_mais_proxima:
                indice_esfera_mais_proxima = i

    return indice_esfera_mais_proxima


# contador para quantidade de estrelas
contador_de_esferas = 0
dados_esferas = [] # lista para recolher os dados de todas as esferas


n = int(input()) # input da matriz
estrada_da_coordenada_de_goku = input() # cordenadas do mano Goku
coluna_de_goku = int(estrada_da_coordenada_de_goku[1])
linha_de_goku = int(estrada_da_coordenada_de_goku[4])

input() # input vazio

traco = '' # era pra se chamar traço, mas não gosto de colocar assentos nas variveis
while traco != 'Todos os bits foram decodificados':

    traco = input() 
    
    if traco == '------------------------------------': # faz o traço para colocar as primeiras coordenadas

        contador_de_esferas += 1

        expressao_x = [] # lista para armazenar todos os inputs da coordenada x
        expressao_y = [] # lista para armazenar todos os inputs da coordenada y

        # faz a coleta de todos os inputs da coordenada x
        linha_de_espressao = input() 
        while linha_de_espressao != '':
            expressao_x.append(linha_de_espressao)
            linha_de_espressao = input()
        
        # faz a coleta de todos os inputs da coordenada y
        linha_de_espressao = input() 
        while linha_de_espressao != '':
            expressao_y.append(linha_de_espressao)
            linha_de_espressao = input()

        # faz o processo das coordenadas das esferas
        coord_coluna, bin_string_coluna = Processar_coordenada(expressao_x, n)
        coord_linha, bin_string_linha = Processar_coordenada(expressao_y, n)

        dados_esferas.append([coord_coluna, coord_linha, bin_string_coluna, bin_string_linha])


# começo da parte gráfica
print('🟠 Vamos conquistar as esferas do dragão! 🟠')
print('--------------------------------------------------------------------------')
print()

# parte do print das coordenadas e dos números binarios
i = 0
for esfera in dados_esferas:
    coluna, linha, bin_str_coluna, bin_str_linha = esfera # coloca as informações de cada esfera dentro das variveis
    print(f'Coordenada x da {i+1}ª esfera do dragão obtida pelo código binário {bin_str_coluna}: {coluna}')
    print(f'Coordenada y da {i+1}ª esfera do dragão obtida pelo código binário {bin_str_linha}: {linha}')
    print(f'As coordenadas da {i+1}ª esfera do dragão são: ({coluna}, {linha})')
    print()
    i += 1

print('--------------------------------------------------------------------------')
print()

# parte do mapa
mapa_do_dragao = []

# faz listas dentro de lista na quantidade de colunas e linhas desejadas
for listas in range(n):
    mapa_do_dragao.append([])

# coloca os pontos na matriz
for colunas in range(n):
    for linhas in range(n):
        mapa_do_dragao[linhas].append('.')

mapa_do_dragao[coluna_de_goku][linha_de_goku] = 'G' # coloca o G de Goku na matrix na localização desejada

# coloca a esfera do dragão na localização de x e y antes fornecida
for localizacao_esfera in dados_esferas:
    coluna_da_esfera, linha_da_esfera, a, a = localizacao_esfera
    mapa_do_dragao[coluna_da_esfera][linha_da_esfera] = '☆'

# printa o mapa com tudo feito
for mapa in mapa_do_dragao:
    print(' '.join(mapa))

print()

# terceira parte

trajetoria = [[coluna_de_goku, linha_de_goku]]
posicao_atual_de_goku = [coluna_de_goku, linha_de_goku] # faz uma copia dos dados
esferas_restantes = list(dados_esferas) # faz uma copia dos dados

# enquanto esferas restantes tiver algo continua o loop
while esferas_restantes:

    # pega o indici da esfera mais proxima
    indice_esfera_mais_proxima = encontrar_esfera_mais_proxima(posicao_atual_de_goku, esferas_restantes)

    # pega as esferas que estão na esferas_restantes e deleta cada esfera depois de passar por ela
    esfera_mais_proxima = esferas_restantes.pop(indice_esfera_mais_proxima)
    
    # adiciona cada posição de goku em uma lista
    trajetoria.append([esfera_mais_proxima[0], esfera_mais_proxima[1]])
    posicao_atual_de_goku = [esfera_mais_proxima[0], esfera_mais_proxima[1]]


# Coloca da uma das coordenadas em uma lista para usar no print depois
listas_das_coordenadas = []
for p in trajetoria:
    listas_das_coordenadas.append(f'({p[0]}, {p[1]})')

# print final
print('Trajetória completa de Goku: ' + ' -> '.join(listas_das_coordenadas))
print('Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉')