# Processa o primeiro cão

nome1 = str(input())
no1 = int(input())
no2 = int(input())
no3 = int(input())
total1 = no1 + no2 + no3 # soma as notas

if nome1 == 'Byte':
    print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')

else:
    if total1 == 30:
        print(f'Com uma pontuação perfeita, {nome1} conquista o título de mascote do CIn!') # se o nome for byte e ele tiver 30 pontos ao todo o programa já para aqui

    else:
        # Processa o segundo cão
        nome2 = str(input())
        not1 = int(input())
        not2 = int(input())
        not3 = int(input())
        total2 = not1 + not2 + not3

        if nome2 == "Byte":
            print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")

        else:
            if total2 == 30:
                print(f"Com uma pontuação perfeita, {nome2} conquista o título de mascote do CIn!")

            else:
                # Processa o terceiro cão
                nome3 = str(input())
                nota1 = int(input())
                nota2 = int(input())
                nota3 = int(input())
                total3 = nota1 + nota2 + nota3

                if nome3 == "Byte":
                    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")

                else:
                    if total3 == 30:
                        print(f"Com uma pontuação perfeita, {nome3} conquista o título de mascote do CIn!")

                    else:

                        # Avaliar quem está fora da disputa e encontrar o vencedor

                        vencedor = '' # contém uma string vazia
                        maior_pontuacao = 0 # contém um int vazio

                        if total1 >= 15: # se a nota total do 1 cachorro for maior ou igual a 15, ele continua na competição, caso não ele sai
                            if total1 > maior_pontuacao: # esse quase sempre é verdadeiro, se a nota total do primeiro for maior que a variavel maior pontuação (0)
                                maior_pontuacao = total1 # maior pontuação recebera o total1
                                vencedor = nome1 # o nome do maior ficara preso no maior pontuação
                            elif total1 == maior_pontuacao and vencedor == '': 
                                vencedor_nome = nome1
                        else:
                            print(f"Infelizmente {nome1} está fora da disputa") # caso ele não atenda os requisitos de pelo menos 15 pomtos

                        if total2 >= 15:
                            if total2 > maior_pontuacao: # aqui se total2 for maior que maior pontuação que agora é o int de total 1, ele substitui as variaveis que estão com total 1
                                maior_pontuacao = total2
                                vencedor = nome2
                            elif total2 == maior_pontuacao and vencedor == '':
                                vencedor = nome2
                        else:
                            print(f"Infelizmente {nome2} está fora da disputa")

                        if total3 >= 15:
                            if total3 > maior_pontuacao:
                                maior_pontuacao = total3
                                vencedor = nome3
                            elif total3 == maior_pontuacao and vencedor == '':
                                vencedor= nome3
                        else:
                            print(f"Infelizmente {nome3} está fora da disputa")

                        print(f"Após uma disputa acirrada, o novo mascote do CIn é {vencedor}!")