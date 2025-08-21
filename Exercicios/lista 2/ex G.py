# variaveis que vou utilizar mais pra frente
inicio = fim = numero_sagrado = -1
tudo = False
final = 0

# inicio do programa
print('🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓\nHoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!\n')

# só para o loop quando todos os valores certos forem atribuidos.
while not tudo:

    if final == 0:
        print('Qual será o número que marcará o INÍCIO dessa tabuada fatorial?')
        final += 1

    inicio = int(input())

    # se o inicio tiver um valor valido o codigo continua.
    if inicio >= 0:

        print(f'O número {inicio} é ótimo como número inicial!')
        print()

        # aqui ele só para quando o código do final for maior que o número inicial.
        while fim < inicio:

            if final == 1:
                print('Qual será o número que marcará o FIM dessa tabuada fatorial?')
                final += 1

            fim = int(input())

            if fim >= inicio:
                print(f'O número {fim} é ótimo como número final!')
                print()
            else:
                print(f'O número {fim} é inválido! O FIM NÃO pode ser MENOR que o número inicial {inicio}.')
            tudo = True

    else:
        print(f'O número {inicio} é inválido! O INÍCIO NÃO pode ser NEGATIVO.')


# aqui só irá para com um número sagrado valido.
while numero_sagrado < 0:

    if final == 2:
        print('Qual será o número cujo FATORIAL será calculado?')
        final += 1

    numero_sagrado = int(input())

    if numero_sagrado >= 0:
        print(f'O número {numero_sagrado} é ótimo para o cálculo do fatorial!')
        print()

    else:
        print(f'O número {numero_sagrado} é inválido! Números válidos são maiores ou iguais a zero.')

# faz os fatoriais dos números.
for c in range(inicio, fim + 1):

    n = c * numero_sagrado
    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i
    print(f'({c} * {numero_sagrado})! = {fatorial}')

# print final
print()
print('🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!\n🏓 Que sua energia vital continue brilhando nas próximas batalhas!')

