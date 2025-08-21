# variaveis que usei no código
lista_das_armas = []
armas_usadas_com_sucesso = dano = contador_de_armas = 0
arma_escolhida = ''
quantidade_de_armas = int(input())

# laço de repetição para adicionar as armas na lista
while contador_de_armas < quantidade_de_armas: 
    lista_das_armas.append(str(input()))
    contador_de_armas += 1

# faz uma copia da lista
lista_copia_das_armas = lista_das_armas[:]

# lê todas as armas necessarias até o usuario digitar 'fim'
while arma_escolhida != 'fim':

    # input para adicionar e usar as armas escolhidas. caso seja um input 'fim' ele sai do loop
    arma_escolhida = str(input())

    # se a arma que ele escolher estiver na lista
    if arma_escolhida in lista_das_armas:

        # se a arma estiver na lista e ainda não foi usada
        if arma_escolhida in lista_das_armas and arma_escolhida in lista_copia_das_armas:
            print(f'{arma_escolhida} usado(a) com sucesso!')
            armas_usadas_com_sucesso += 1

        # se a arma estivesse na lista mas foi usada
        if arma_escolhida not in lista_copia_das_armas and arma_escolhida in lista_das_armas:
            print(f'{arma_escolhida} já foi usado(a)!')
            dano += 1

        # remove a arma da lista se a arma for usada
        if arma_escolhida in lista_copia_das_armas:
            lista_copia_das_armas.remove(arma_escolhida)

    # caso a palavra digitada seja 'fim' ele para o programa, já que o mesmo input para sair do loop é o mesmo input para fazer a verificação
    elif arma_escolhida == 'fim':
        None

    # se a arma nunca foi adicionada na lista
    elif arma_escolhida not in lista_copia_das_armas:
        print(f'{arma_escolhida} não está disponível!')
        dano += 1

# print que sempre vai acontecer
print(f'Batalha encerrada! Os Vingadores utilizaram {armas_usadas_com_sucesso} arma(s).')

# print a depender do dano
if dano == 0:
    print('Vitória! Os Vingadores salvaram o UNIVERSO!')
    print()
    print('Tony Stark:\nSalvar o mundo de novo? Vou precisar de um aumento.')
    print()
    print('Thor:\nEspero que tenha cerveja depois disso!')
    print()
    print('Homem-Aranha:\nPosso dizer que ajudei, né? Tipo… oficialmente?\nDá pra postar isso no Insta dos Vingadores?')

elif dano == 1:
    print('Os Vingadores sofreram um golpe do Thanos!')
    print('Vitória por pouco! Os Vingadores ganharam...')
    print()
    print('Tony Stark:\nQuase que eu fico sem troco para o cafezinho.')
    print()
    print('Thor:\nEsse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!')
    print()
    print('Peter Quill (Star-Lord):\nCara, quase perdi o ritmo do meu walkman!')

else:
    print(f'Os Vingadores sofreram {dano} golpes do Thanos!')
    print('Derrota... Os Vingadores não conseguiram todas as armas necessárias.')
    print()
    print('Tony Stark:\nEssa não foi das melhores ideias...')
    print()
    print('Thor:\nCulpa do humano. Eu sabia que devíamos ter chamado o Hulk.')