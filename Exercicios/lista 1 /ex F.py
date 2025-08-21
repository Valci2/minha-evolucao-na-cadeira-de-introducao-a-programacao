nome1 = str(input())
indicou1 = str(input())
nome2 = str(input())
indicou2 = str(input())
nome3 = str(input())
indicou3 = str(input())

# calcula a pontuação do nome 1.

no1 = 0
no2 = 0
no3 = 0

if indicou1 == 'felino espião':
    no1 = 0
elif 'gato' in nome1:
    no1 = 0
else:
    no1 = len(nome1)
    if 'cin' in nome1:
        no1 += 10
        print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

# calcula a pontuação do nome 2.

if indicou2 == 'felino espião':
    no2 = 0
elif 'gato' in nome2:
    no2 = 0
else:
    no2 = len(nome2)
    if 'cin' in nome2:
        no2 += 10
        print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

# calcula a pontuação do nome 3.

if indicou3 == 'felino espião':
    no3 = 0
elif 'gato' in nome3:
    no3 = 0
else:
    no3 = len(nome3)
    if 'cin' in nome3:
        no3 += 10
        print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

# verifica se a pessoa que indicou não é um felino espião.

if indicou1 == 'felino espião' or indicou2 == 'felino espião' or indicou3 == 'felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')

# faz o ranking dos nomes.

print('RANKING DOS NOMES:')
if no1 > no2 and no1 > no3:
    print(f'Primeiro lugar: {nome1}')
    if no2 > no3:
        print(f'Segundo lugar: {nome2}')
        print(f'Terceiro lugar: {nome3}')
    else:
        print(f'Segundo lugar: {nome3}')
        print(f'Terceiro lugar: {nome2}')

elif no2 > no1 and no2 > no3:
    print(f'Primeiro lugar: {nome2}')
    if no1 > no3:
        print(f'Segundo lugar: {nome1}')
        print(f'Terceiro lugar: {nome3}')
    else:
        print(f'Segundo lugar: {nome3}')
        print(f'Terceiro lugar: {nome1}')
        
elif no3 > no1 and no3 > no2:
    print(f'Primeiro lugar: {nome3}')
    if no1 > no2:
        print(f'Segundo lugar: {nome1}')
        print(f'Terceiro lugar: {nome2}')
    else:
        print(f'Segundo lugar: {nome2}')
        print(f'Terceiro lugar: {nome1}')