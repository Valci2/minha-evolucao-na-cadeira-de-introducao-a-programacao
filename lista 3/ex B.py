# variaveis utilizadas no codigo
exercito = []
monitoramento = 0

# inputs iniciais
nivel_sung = int(input())
quantidade_de_monstros = int(input())

# flag para saber se ele perdeu ou não
perdeu = False

# loop para quantidade de monstros desejada
while not perdeu and monitoramento < quantidade_de_monstros:

    # inputs dos monstros
    nome_do_monstro = str(input())
    nivel_da_criatura = int(input())

    # se o nivel da criatura for maior que a de sung ele perde
    if nivel_da_criatura >= nivel_sung:
        
        print(f'Jin-Woo foi derrotado por {nome_do_monstro}...')
        perdeu = True

    # caso contrario ele continua 
    else:
            
        # variável para saber se o monstro deve entrar no exercito do próprio
        entra_ou_nao = str(input())
        monitoramento += 1

        # caso ele entre ele é adicionado na lista
        if entra_ou_nao == 'Erga-se':

            nivel_sung += nivel_da_criatura // 3

            if nome_do_monstro not in exercito:

                exercito.append(nome_do_monstro)
                indice_do_monstro = exercito.index(nome_do_monstro)
                exercito.insert(indice_do_monstro + 1, 1)
                    
            else:
                    
                contador_de_monstros = exercito.index(nome_do_monstro) + 1
                exercito[contador_de_monstros] += 1 


# armazena a quantidade de elementos em exercito para printar tudo no for em baixo
quantidade = len(exercito)

# caso o sung faça uma caçada perfeita
if not perdeu:
    print('Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!')

# sempre printa isso
print('===== Exército das Sombras de Jin-Woo =====')

# caso ele monte seu exercito
if len(exercito) > 0:

    for prints in exercito:
        print(f'{prints}', end=': ' if quantidade % 2 == 0 else '\n')
        quantidade -= 1

# caso ele perca
if len(exercito) == 0:
    print('Jin-Woo não conseguiu formar seu exército...')