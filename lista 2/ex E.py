# variaveis iniciais
cont = 0
vogais = 'aeiouAEIOU'
quant = int(input())

if quant == 2:
    
    nome = str(input())
    posição = int(input())
    rank = int(input())
    velocidade = float(input())
    nome2 = str(input())
    posição2 = int(input())
    rank2 = int(input())
    velocidade2 = float(input())
    print(f'Caso encerrado: {nome} e {nome2} roubaram o troféu!')

elif quant == 1:

    nome = str(input())
    posição = int(input())
    rank = int(input())
    velocidade = float(input())
    print(f'Não há dúvidas... {nome} é o culpado!')

else:

    nome_suspeito1 = ''
    pontuacao_suspeito1 = 0
    ordem_suspeito1 = 0

    nome_suspeito2 = ''
    pontuacao_suspeito2 = 0
    ordem_suspeito2 = 0

    nome_suspeito3 = ''
    pontuacao_suspeito3 = 0
    ordem_suspeito3 = 0

    while cont < quant:

        pontuação = esconde = quantidade_vogais = 0
        print(f'COMEÇANDO A {cont+1}ª RODADA DE INVESTIGAÇÃO')
        nome = str(input())
        posição = int(input())
        rank = int(input())
        velocidade = float(input())

        # Verificando a quantidade de vogais no nome
        for letras in nome:
            if letras in vogais:
                quantidade_vogais += 1

        # Calcula se a quantidade de vogais é par ou ímpar
        if quantidade_vogais % 2 == 0:
            pontuação += 10
        elif quantidade_vogais % 2 == 1:
            pontuação += 5

        # calcula posição do atleta
        if 45 <= posição <= 135:
            pontuação += 10
            print(f'{nome} estava em posição estratégica para pegar o troféu... muito suspeito!')
        elif 225 <= posição <= 315:
            pontuação += 5
            esconde += 1
        else:
            pontuação += 2
            esconde += 1


        # Verificando o rank do atleta
        if 1 <= rank <= 10:
            pontuação += 10
            print(f'{nome} é um dos melhores do mundo... e também um dos principais suspeitos!')
        elif 11 <= rank <= 50:
            pontuação += 5
            esconde += 1
        else:
            pontuação += 2
            esconde += 1


        # Verificando a velocidade do atleta
        if velocidade > 140:
            pontuação += 10
            print(f'Alta velocidade detectada! {nome} pode ter fugido rapidamente com o troféu!')
        elif 100 <= velocidade <= 140:
            pontuação += 5
            esconde += 1
        else:
            pontuação += 2
            esconde += 1


        # Verificando se o atleta está escondendo algo
        if esconde >= 3:
            print(f'Hum, esse {nome} sei não viu... Deve tá escondendo alguma coisa.')


        # Atualizando os suspeitos com base na pontuação
        if pontuação > pontuacao_suspeito1:
            nome_suspeito3 = nome_suspeito2
            pontuacao_suspeito3 = pontuacao_suspeito2
            ordem_suspeito3 = ordem_suspeito2
            
            nome_suspeito2 = nome_suspeito1
            pontuacao_suspeito2 = pontuacao_suspeito1
            ordem_suspeito2 = ordem_suspeito1
            
            nome_suspeito1 = nome
            pontuacao_suspeito1 = pontuação
            ordem_suspeito1 = cont

        elif pontuação > pontuacao_suspeito2:
            nome_suspeito3 = nome_suspeito2
            pontuacao_suspeito3 = pontuacao_suspeito2
            ordem_suspeito3 = ordem_suspeito2
            
            nome_suspeito2 = nome
            pontuacao_suspeito2 = pontuação
            ordem_suspeito2 = cont
            
        elif pontuação > pontuacao_suspeito3:
            nome_suspeito3 = nome
            pontuacao_suspeito3 = pontuação
            ordem_suspeito3 = cont

            
        cont += 1

    # Exibindo os resultados das investigações
    print('\nRESULTADOS DAS INVESTIGAÇÕES:\n')
    print(f'Os 3 principais suspeitos são:')
    print(f'1. {nome_suspeito1} - {pontuacao_suspeito1} pontos')
    print(f'2. {nome_suspeito2} - {pontuacao_suspeito2} pontos')
    print(f'3. {nome_suspeito3} - {pontuacao_suspeito3} pontos\n')
    
    # Determinando o culpado
    if pontuacao_suspeito1 == pontuacao_suspeito2:
        print(f'Que absurdo... {nome_suspeito1} e {nome_suspeito2} roubaram o troféu juntos!')
    elif pontuacao_suspeito1 > pontuacao_suspeito2:
        print(f'Mistério resolvido: O culpado é {nome_suspeito1}! Ele roubou o troféu de Calderano.')