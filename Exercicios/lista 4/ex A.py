def Distancia_Euclidiana(x, y):
    
    '''calcula o valor de uma distancia euclidiana, utilzando dois argumentos, x primeiro valor colocado
    e y segundo valor colocado'''

    return ((x**2 + y**2) ** 0.5) # faz o calculo da distancia

# variaveis que eu utilizei
calculo = 0
esfera_encontrada = 0
menor_calculo = float('inf')

# primeiro input
quantidade_de_objetos = int(input())

# um loop na quantidade desejada pelo usuario
for c in range(quantidade_de_objetos):

    # onde ele vai colocar o nome do objeto
    nome_do_objeto = str(input())
    
    # faz a verificação dos obejetos
    if nome_do_objeto == 'rocha':
        print("Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'")
    elif nome_do_objeto == 'árvore':
        print("Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'")
    elif nome_do_objeto == 'nave':
        print("Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'")
    elif nome_do_objeto != 'esfera':
        print(f'Radar: Detectado um(a) {nome_do_objeto}. Não parece ser uma esfera... Continuando a busca.')

    # variaveis para as coordenadas desejadas
    coordenada_x = int(input())
    coordenada_y = int(input())

    # caso seja uma esfera ele faz o calculo e deixa a posição encontrada salvas
    if nome_do_objeto == 'esfera':

        calculo = Distancia_Euclidiana(coordenada_x, coordenada_y) # substitui a cada esfera nova colocada
        if calculo < menor_calculo:
            menor_calculo = calculo
            esfera_encontrada = c + 1 # substitui a cada esfera nova colocada

    # só printa no final do loop. para ter certeza que outra esfera não vai ser encontrada
if esfera_encontrada > 0:
    print(f'ALVO PRIORITÁRIO: Esfera | Distância: {menor_calculo:.2f}m | Detecção Original: {esfera_encontrada}°')

# só printa no final do loop. só printa se nenhuma esfera for encontrada
else:
    print('Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!')