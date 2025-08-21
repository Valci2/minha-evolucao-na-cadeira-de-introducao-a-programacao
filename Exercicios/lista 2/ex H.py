# print inicial
print('A partida de revanche de Hugo Calderano contra a China, Potência Mundial do Tênis de Mesa, está prestes a começar!')

# verifica a nacionalidade.
nacionalidade = ''
while nacionalidade != 'Chinês':

    nacionalidade = str(input()) # aqui ele vai verificar a nacionalidade do jogador rival
    nome = str(input()) # nome do jogador

    # se a nacionalidade não for chinês ele continua pedindo 
    if nacionalidade == 'Chinês':
        print(f'{nome} foi convocado para vingar o massacre feito durante o mundial de Tênis de Mesa!')
    else:
        print(f'O {nome} não poderá disputar a partida, pois sua nacionalidade não é chinesa!')

# variaveis para fazer a pontuação dos jogadores
pontuacao_chines = pontuacao_brasileiro = 0

# faz um loop até a pontuação brasileira ser pelo menos três pontos maior
while pontuacao_brasileiro < pontuacao_chines + 3:

    acertos_chines = int(input())
    acertos_brasileiro = int(input())

    # condições de vitoria
    if acertos_brasileiro >= acertos_chines * 2:
        print('Que bela jogada, essa merece ponto extra!')
        pontuacao_brasileiro += 2

    elif acertos_brasileiro > acertos_chines:
        print('Hugo Calderano marcou um ponto de maneira esplendida!')
        pontuacao_brasileiro += 1

    elif acertos_chines >= acertos_brasileiro * 2:
        print('Que bela jogada, essa merece ponto extra!')
        pontuacao_chines += 2

    elif acertos_chines > acertos_brasileiro:
        print('Vamos Hugo, não deixe ele vencer!')
        pontuacao_chines += 1

    else:
        print('A bola bateu na rede e felizmente caiu no lado adversário!!! Hugo marca mais um ponto!')
        pontuacao_brasileiro += 1


# prints de vitoria
if pontuacao_brasileiro == 3:
    print('Hugo Calderano mostrou o porquê ele é o atual campeão mundial, uma partida relâmpago!')
elif 3 < pontuacao_brasileiro <= 10:
    print('Não demorou muito, mas o resultado era esperado, Hugo Calderano vence!')
elif pontuacao_brasileiro > 10:
    print('Demorou, mas o previsto aconteceu! Hugo Calderano não deixa dúvidas do porquê ele é o Campeão Mundial!')


# print do resutado
print(f'Placar Final: {pontuacao_brasileiro}x{pontuacao_chines}\n')


# deixa a pontuação do chines arredondado
if pontuacao_chines % 2 == 0:
    pontuacao_chines -= 1

# print do 'trofeu'
print('Aqui está o merecido prêmio de Hugo Calderano:')


# construção do 'trofeu??'
# faz a primeira linha do trofeu
print('-' * pontuacao_brasileiro)

# faz a parte de cima isso se o trofeu tiver 5 de altura pra cima
for barras in range((pontuacao_chines-2)//2):
    print('|',end='')
    for spaco in range(1, pontuacao_brasileiro-1):
        print(' ', end='')
    print('|', end='\n')

# faz a parte central do trofeu, caso o trofeu tenha 3 de altura só faz a primeira, esse e a ultima linha
print('|',end='')
for spaco in range(1, pontuacao_brasileiro-1):
    print('#', end='')
print('|', end='\n')

# faz a parte de baixo do trofeu
for barras in range((pontuacao_chines-2)//2):
    print('|',end='')
    for spaco in range(1, pontuacao_brasileiro-1):
        print(' ', end='')
    print('|', end='\n')

# faz a ultima linha do trofel
print('-' * pontuacao_brasileiro)