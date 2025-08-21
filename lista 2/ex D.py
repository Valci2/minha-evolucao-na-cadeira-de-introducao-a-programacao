# inicio do programa
print('Robô Hugo 4.0 foi inicializado…')

# inputs do programa
f_max = int(input())
forca_inicial = int(input())
nivel = str(input())
forca_media_jogador = int(input())

# nivel de difilcudade
if nivel == 'facil':
    print('Iniciando no modo iniciante... Ótimo para aquecer os motores!')
    incremento = 1
elif nivel == 'medio':
    print('Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!')
    incremento = 3
elif nivel == 'dificil':
    print('Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!')
    incremento = 5

# variaveis de acumulação
forca_rebatida = 0
forca_acumulada = 0
tempo = 0
parada = False

# vai fazer o loop até a forca a acumulada do robor ser maior que a força maxima requisitada
while forca_acumulada < f_max and not parada:

    tempo += 1
    forca_rebatida = forca_inicial + (tempo * incremento)

    if forca_rebatida <= 150:
        forca_acumulada += forca_rebatida
        print(f'Rebatida {tempo}: força = {forca_rebatida}, força acumulada = {forca_acumulada}')
    
    elif forca_rebatida > 150:
        print('Bola fora! A força da rebatida excedeu os limites da mesa.')
        parada = True


# só printa se a forca do robo não ultrapassar 150 na forca de rebatida
if not parada:
    print('Energia do robô esgotada! Encerrando o confronto…')

# calculo da força média do robo
if tempo <= 0:
    forca_media_robo = 0

else:
    forca_media_robo = forca_acumulada // tempo

# prints das informações da partida
print('Partida finalizada! Estas são as estatísticas do embate:')
print(f'O robô realizou {tempo} rebatidas em {tempo} segundos, com força total de {forca_acumulada}.')
print(f'Força média do robô: {forca_media_robo}')
print(f'Força média do jogador: {forca_media_jogador}')


# condições para definir o ganhador
if forca_media_jogador > forca_media_robo:
    print('Vitória do jogador! O talento humano ainda é imbatível!')
elif forca_media_robo > forca_media_jogador:
    print('Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!')
else:
    print('Empate técnico! Um duelo digno de mestres do tênis de mesa.')