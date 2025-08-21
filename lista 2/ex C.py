# variaveis que armazenam a quantidade de votos e o nome dos itens
clas = can = classi = 0
classica = 'Clássica'
caneta = 'Caneta'
classineta = 'Classineta'

# esse for serve para repetir o ciclo de pedir a quantidade de votos
quant = int(input())

# aqui ele vai repetir a quantidade de votos que foi passada pelo usuário
for c in range(0, quant):
    escolha = str(input())
    if escolha == 'Clássica':
        clas += 1
    elif escolha == 'Caneta':
        can += 1
    elif escolha == 'Classineta':
        classi += 1

print('Estamos calculando... tão rápido quanto dar Run no Dikastis...')

# aqui ele vai verificar qual é o maior número de votos e imprimir o resultado
if clas > can and clas > classi:
    print(f'1º lugar: {classica} ({clas} votos)')
    if can > classi:
        print(f'2º lugar: {caneta} ({can} votos)')
        print(f'3º lugar: {classineta} ({classi} votos)')
    else:
        print(f'2º lugar: {classineta} ({classi} votos)')
        print(f'3º lugar: {caneta} ({can} votos)')

# a mesma coisa só que dessa faz se caneta for o maior número de votos
elif can > clas and can > classi:
    print(f'1º lugar: {caneta} ({can} votos)')
    if classi > clas:
        print(f'2º lugar: {classineta} ({classi} votos)')
        print(f'3º lugar: {classica} ({clas} votos)')
    else:
        print(f'2º lugar: {classica} ({clas} votos)')
        print(f'3º lugar: {classineta} ({classi} votos)')

# a mesma coisa só que dessa faz se classineta for o maior número de votos
elif classi > clas and classi > can:
    print(f'1º lugar: {classineta} ({classi} votos)')
    if clas > can:
        print(f'2º lugar: {classica} ({clas} votos)')
        print(f'3º lugar: {caneta} ({can} votos)')

# se o número de clássicos for maior que o resto
if clas > can+4 and clas > classi+4:
    print('Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!')