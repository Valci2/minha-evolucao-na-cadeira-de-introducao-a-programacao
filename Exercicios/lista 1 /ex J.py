# variaveis de contagem

vitorias = derrotas = pts = 0
tentaram = 'Não!!!! :D'

print('Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!')

# Primeira partida

nome_cidade1 = str(input())

# caso nome da cidade seja Tapira OU!! Catente

if nome_cidade1 == 'Catende' or nome_cidade1 == 'Tabira':
    print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')

# caso o primeiro time seja algo relacionado ao sport
nome_time1 = str(input())
if 's' in nome_time1 and 'p' in nome_time1 and 'o' in nome_time1 and 'r' in nome_time1 and 't' in nome_time1:
    print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')

resultado1 = str(input())

# caso o resultado seja sequestro
if resultado1 == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    tentaram = 'sim :('
    pts += 1
    vitorias += 1
    print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')
    expressao = str(input())
    if '+' in expressao:
        a, sinal, b = expressao
        a = int(a)
        b = int(b)
        c = a + b
    elif '-' in expressao:
        a, sinal, b = expressao
        a = int(a)
        b = int(b)
        c = a - b
    elif '*' in expressao:
        a, sinal, b = expressao
        a = int(a)
        b = int(b)
        c = a * b
    elif '/' in expressao:
        a, sinal, b = expressao
        a = int(a)
        b = int(b)
        if b == 0:
            c = a # aqui caso o b seja 0, a divisao ia dar problema então como já estamos dividindo por 0, coloque pra o c receber apenas o primeiro número
        else:
            c = a / b # caso b > 0, ele faz normal

    print(f'A expressão resolvida é: {c:.2f}') # aqui ele só printa o resultado com duas casas
    print('Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!')

    # Relatorio caso o o Byte seja sequestrado, tadinho :<
    print(f'''\nRELATÓRIO DA PRÉ-TEMPORADA DO BYTE:
- Partidas jogadas: {pts}
- Vitórias: {vitorias}
- Derrotas: {derrotas}
- Tentaram roubar o bixinho: {tentaram}
- Cidades visitadas: {nome_cidade1}
- Adversários enfrentados: {nome_time1}''')
    print('\nE assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)')
    

# caso o resultado seja 'Venceu' ou 'perdeu'
if resultado1 == 'VENCEU' or resultado1 == 'perdeu':
    if resultado1 == 'VENCEU':
        vitorias += 1
        pts += 1
        print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
    elif resultado1 == 'perdeu':
        derrotas += 1
        pts += 1
        print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')


    nome_cidade2 = str(input())

    # caso a segunda cidade seja catente OU!! tabira ele printa a mesma coisa da primeira cidade
    if nome_cidade2 == 'Catende' or nome_cidade2 == 'Tabira':
        print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')

    # caso a primeira cidade seja Catente ou tabira E!! a segunda seja catente ou tabira.
    if (nome_cidade1 == 'Catende' and nome_cidade2 == 'Tabira') or (nome_cidade2 == 'Tabira' and nome_cidade1 == 'Catende'):
        print('Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...')

    nome_time2 = str(input())
    if 's' in nome_time2 and 'p' in nome_time2 and 'o' in nome_time2 and 'r' in nome_time2 and 't' in nome_time2:
        print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')

    # segundo resultado
    resultado2 = str(input())

    if resultado2 == 'VENCEU':
        vitorias += 1
        pts += 1
        print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
    elif resultado2 == 'perdeu':
        derrotas += 1
        pts += 1
        print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')

    # caso o resultado seja sequestro ele vai entra com todo o codigo de baixo denovo (dava pra fazer uma função)
    elif resultado2 == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
        tentaram = 'sim :('
        vitorias += 1
        pts += 1
        print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')
        expressao = str(input())
        if '+' in expressao:
            a, sinal, b = expressao
            a = int(a)
            b = int(b)
            c = a + b
        elif '-' in expressao:
            a, sinal, b = expressao
            a = int(a)
            b = int(b)
            c = a - b
        elif '*' in expressao:
            a, sinal, b = expressao
            a = int(a)
            b = int(b)
            c = a * b
        elif '/' in expressao:
            a, sinal, b = expressao
            a = int(a)
            b = int(b)
            if b == 0:
                c = a
            else:
                c = a / b

        print(f'A expressão resolvida é: {c:.2f}')
        print('Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!')

    # relatorio com duas partidas
    print(f'''\nRELATÓRIO DA PRÉ-TEMPORADA DO BYTE:
- Partidas jogadas: {pts}
- Vitórias: {vitorias}
- Derrotas: {derrotas}
- Tentaram roubar o bixinho: {tentaram}
- Cidades visitadas: {nome_cidade1} e {nome_cidade2}
- Adversários enfrentados: {nome_time1} e {nome_time2}''')
    
    print('\nE assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)')