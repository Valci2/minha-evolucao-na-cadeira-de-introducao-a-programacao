ataque = defesa = erro = 0

print('------- Início do Treino -------')
quant = int(input())

# esse for serve para repetir o ciclo de pedir a estrategia [Ataque/Defesa] e o golpe
for c in range(0, quant):
    bola = str(input())
    golpe = str(input())

    # esse if verifica qual foi a estrategia e o golpe lançados para atribuir a quantidade de pontos
    if bola == 'Ataque' and golpe == 'Topspin':
        ataque += 5
        print(f'Você conseguiu rebater uma bola de {bola}! Golpe executado: {golpe}.')

    elif bola == 'Ataque' and golpe == 'Smash':
        ataque += 10
        print(f'Você conseguiu rebater uma bola de {bola}! Golpe executado: {golpe}.')

    elif bola == 'Defesa' and golpe == 'Push':
        defesa += 5
        print(f'Você conseguiu rebater uma bola de {bola}! Golpe executado: {golpe}.')

    elif bola == 'Defesa' and golpe == 'Chop':
        defesa += 10
        print(f'Você conseguiu rebater uma bola de {bola}! Golpe executado: {golpe}.')

    # esse elif é para casos de erros
    elif bola == 'Ataque' and golpe == 'Errou':
        ataque -= 10
        erro += 1
        print('Você errou! Levanta a cabeça que ainda tem mais.')

    elif bola == 'Defesa' and golpe == 'Errou':
        defesa -= 10
        erro += 1
        print('Você errou! Levanta a cabeça que ainda tem mais.')

# esse if serve para verificar se a defesa é maior que o ataque ou ao contrario
if ataque > 0 and ataque > defesa:
    print('Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!')
elif defesa > 0 and defesa > ataque:
    print('Defesa ganha campeonatos! Agora sim estou preparado.')
else:
    print('Foi um treino equilibrado.')

# esse if verifica se existe pelo menos um erro no meio do treino
if erro > 0:
    print('Infelizmente não foi um treino perfeito, mas pude melhorar muito.')

# mostra o resutado de tudo
print('------- Atributos -------')
print(f'Ataque: {ataque}' if ataque > 0 else 'Ataque: 0') # esse if dentro do print serve para mostras q quantidade de ataque isso se o ataque for maior que zero
print(f'Defesa: {defesa}' if defesa > 0 else 'Defesa: 0') # a mesma coisa do ataque