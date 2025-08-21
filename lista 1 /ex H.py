# os inputs

humor = str(input())
senta = int(input())
da_patinha = int(input())
fica = int(input())
pega = int(input())
comando = str(input())


# se o comando for senta e fica, ele não faz. mas adiciona um ponto no truque colocado
# agora os outros coamndos ele faz. e adiciona um ponto no truque colocado

if comando == 'Senta':
    senta += 1
    if humor == 'Brincalhão':
        print('Ele parece estar muito animado para isso!')
    if senta >= 3 and humor != 'Brincalhão':
        print('Byte é o melhor')

elif comando == 'Dá a patinha':
    da_patinha += 1
    if da_patinha >=3:
        print('Ele é um bom garoto!')

elif comando == 'Fica':
    fica += 1
    if humor == 'Brincalhão':
        print('Ele não consegue ficar parado') 
    if fica >= 3 and humor != 'Brincalhão':
        print('Ele está aprendendo')

elif comando == 'Pega':
    pega += 1
    if humor == 'Preguiçoso':
        print('Quem não tem seu momento de preguiça?')
    if pega >= 3 and humor != 'Preguiçoso':
        print('Ele é muito ágil!')

    # resultado do que ele aprendeu, se ele aprendeu algo

if senta >= 3 or da_patinha >= 3 or fica >= 3 or pega >= 3:
    print(f'O nosso novo mascote estava {humor} e aprendeu o(s) seguinte(s) truque(s):')
    if senta >= 3:
        print('Senta')
    if da_patinha >= 3:
        print('Dá a patinha')
    if fica >= 3:
        print('Fica')
    if pega >= 3:
        print('Pega')

elif senta < 3 or da_patinha < 3 or fica < 3 or pega < 3: # aqui é caso ele não tenha aprendido nada
    print('Parece que ele não aprendeu esse truque ainda')