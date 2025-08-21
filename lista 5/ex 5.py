def resgate(matriz, movimentos=0, chegou=False):
    ''''''
    



mapa = []

linha = int(input())
coluna = int(input())

for linhas in range(linha):
    mapa.append([])
for colunas in range(linha):
    mapa[colunas].append(input().strip(' '))

print('=== SEKIRO: O RESGATE DE CESAR ===')
print('Wolf deve resgatar CESAR!')

chegou, movimentos = resgate(mapa)




if chegou:
    print(f'SUCESSO! Wolf resgatou o Cesar em {movimentos} movimentos!')
else:
    print('MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!')


if movimentos <= 4:
    print('PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!')
elif 4 < movimentos < 8:
    print('BOM! Caminho eficiente! Mas você quase decepcionou Cesar')
elif movimentos >= 8:
    print('Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!')

