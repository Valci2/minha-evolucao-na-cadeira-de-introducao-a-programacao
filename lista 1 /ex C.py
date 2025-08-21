# armazena quantos dedos cada um dos cinco monitores colocaram

monitor1 = int(input())
monitor2 = int(input())
monitor3 = int(input())
monitor4 = int(input())
monitor5 = int(input())

# verifica se os valores estão entre 0 e 10 e se não forem, não faz nada

if 0 <= monitor1 <= 10 and 0 <= monitor2 <= 10 and 0 <= monitor3 <= 10 and 0 <= monitor4 <= 10 and 0 <= monitor5 <= 10:

    # soma os valores
    total = monitor1 + monitor2 + monitor3 + monitor4 + monitor5

    # o total e dividi por 5 e o resto da divisão indica quem vai passear com o cachorro
    
    if total % 5 == 0:
        print(f'Arthur vai ter a honra de passear com Byte hoje!')
    if total % 5 == 1:
        print(f'Bruna vai ter a honra de passear com Byte hoje!')
    if total % 5 == 2:
        print(f'César vai ter a honra de passear com Byte hoje!')
    if total % 5 == 3:
        print(f'Daniel vai ter a honra de passear com Byte hoje!')
    if total % 5 == 4:
        print(f'Eduarda vai ter a honra de passear com Byte hoje!')