# Uniforme Isotônico Raquete Toalha
uni = iso = raque = toa = sabo = 0

# Definicão dá variavel escolha 
escolha = ''
while escolha != 'FIM': # Enquanto a variavel escolha for diferente de 'FIM' ele não para

    escolha = str(input()) # Input dá variavel 'escolha' 

    if escolha == 'Uniforme': # Se escolha for igual a uniforme adiciona 1 ponto no contador de uniforme
        uni += 1
        print(f'Tava faltando camisa! Agora temos {uni} uniforme(s)')

    elif escolha == 'Isotônico':
        iso += 1
        print(f'Bora garantir a hidratação! Agora temos {iso} isotônico(s)')

    elif escolha == 'Raquete':
        raque += 1
        print(f'Mais uma raquete saindo! Agora temos {raque} raquete(s)')

    elif escolha == 'Toalha':
        toa += 1
        print(f'Mais uma toalha saindo! Agora temos {toa} toalha(s)')

    elif escolha == 'Sabotagem': # Caso a variavel escolha seja 'Sabotagem'.

        sabota = str(input()) # Aqui caso a varivel receba os inputs de uniforme e etc ele retira um.

        if sabota == 'Uniforme': 
            sabo += 1 # essa variavel vai receber 1 ponto se qualquer sabotagem acontecer
            if uni == 0: # caso a quantidade de uniforme seja 
                print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
            elif uni > 0:
                uni -= 1
                print('O sueco está roubando as camisas de Hugo!')

        elif sabota == 'Isotônico':
            sabo += 1
            if iso == 0:
                print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
            elif iso > 0:
                iso -= 1
                print('O sueco está sabotando a hidratação de Hugo!')

        elif sabota == 'Raquete':
            sabo += 1
            if raque == 0:
                print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
            elif raque > 0:
                raque -= 1
                print('O sueco está roubando as raquetes de Hugo!')

        elif sabota == 'Toalha':
            sabo += 1
            if toa == 0:
                print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
            elif toa > 0:
                toa -= 1
                print('O sueco está roubando as toalhas de Hugo!')

# Resultado de tudo que aconteceu
print(f'Bora ver o relatório final dos materiais!')
print(f'Uniforme: {uni} unidade(s).')
print(f'Isotônico: {iso} unidade(s).')
print(f'Raquete: {raque} unidade(s).')
print(f'Toalha: {toa} unidade(s).')


# Texto final
if sabo > 0 and uni == 0 and iso == 0 and raque == 0 and toa == 0:
    print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
elif uni == 0 and iso == 0 and raque == 0 and toa == 0:
    print('Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.')
elif uni > 0 and iso > 0 and raque > 0 and toa > 0:
    print('Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!')
else:
    print('Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!')