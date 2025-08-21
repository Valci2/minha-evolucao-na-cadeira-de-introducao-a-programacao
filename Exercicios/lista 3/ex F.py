# input da quantidade de ondas que vai ter
quantidade_de_ondas = int(input())

# vitoria dos herois e vilões
vitorias_dos_herois = 0
vitorias_dos_viloes = 0

# variaveis que eu vou usar
onda_atual = 0
onda_menos_acirrada = 0
diferenca_onda_menos_acirrada = 0
menor_ameaca = 0
nome_dos_personagens_de_menor_ameaca = ''

# enquanto a quantidade de ondas não for igual a desejada
while onda_atual < quantidade_de_ondas:

    # variaveis que vão resetar
    primeiro = True
    posicao_personagem = 0
    viloes_participantes = 0
    herois_participantes = 0
    personagem = str(input()). split(', ')

    # a quantidade de personagens precisa ser mais de 3
    if len(personagem) >= 3:

        # vê elemento por na varivel onde vamos dar os input dos herois
        for c in personagem:

            # faz a pontuação dos vilões e herois respectivamente.
            viloes_participantes += c.count('V-')
            herois_participantes += c.count('H-')
            
            # esse posicao_personagem serve para ele identificar quando o ultimo personagem for colocado
            posicao_personagem += 1

            # faz a verifição do primeiro personagem (que não conta na pontuação)
            if 'V' in c and primeiro:
                viloes_participantes -= 1
                primeiro = False

            elif 'H' in c and primeiro: 
                herois_participantes -= 1
                primeiro = False

            # Verifica o último personagem (que não conta na pontuação)
            if posicao_personagem == len(personagem):
                if 'V' in c:
                    viloes_participantes -= 1
                elif 'H' in c:
                    herois_participantes -= 1

        # faz a diferença da pontuação dos herois e vilões 
        diferenca = herois_participantes - viloes_participantes

        # caso a diferença seja maior que zero soma para os herois e caso seja menor tira
        if diferenca > 0:
            vitorias_dos_herois += 1
        elif diferenca < 0:
            vitorias_dos_viloes += 1

        # esse if é para salvar a onda com menor indice, os nome dos personagens de menor 
        # indice personagens, a onda que teve menos acirrada e a diferença da pontuação
        if abs(diferenca) > menor_ameaca:

            menor_ameaca = abs(diferenca)
            nome_dos_personagens_de_menor_ameaca = personagem
            onda_menos_acirrada = onda_atual + 1
            diferenca_onda_menos_acirrada = diferenca

        # verifica a onda atual para encerrar o while
        onda_atual += 1


# variavel que irei usar no futuro 
quantidade = len(nome_dos_personagens_de_menor_ameaca)

# caso a difenrença da disputa mais encerrada seja maior, printa isso para os herois
if diferenca_onda_menos_acirrada > 0:   
    print(f'🌀Onda {onda_menos_acirrada} foi a menos acirrada e a mais favorável para os heróis!')
    print(f'Participantes analisados:', ', '.join(nome_dos_personagens_de_menor_ameaca))

# caso a difenrença da disputa mais encerrada seja menor, printa isso para os vilões
elif diferenca_onda_menos_acirrada < 0:
    print(f'🌀Onda {onda_menos_acirrada} foi a menos acirrada e a mais favorável para os vilões!')
    print(f'Participantes analisados:', ', '.join(nome_dos_personagens_de_menor_ameaca))

# caso a diferença seja zero
else:
    print('🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!')

# esse print sempre vai aonda_atualecer
print('Agora vamos ao resultado geral das ondas...')
print(f'Heróis: {vitorias_dos_herois} | Vilões: {vitorias_dos_viloes}')

# printa de acordo com a pontuação dos herois e vilões
if vitorias_dos_herois > vitorias_dos_viloes:
    print('Ufa, os heróis dominaram! Central City está seguro outra vez')
elif vitorias_dos_viloes > vitorias_dos_herois:
    print('Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!')
else: 
    print('Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço')