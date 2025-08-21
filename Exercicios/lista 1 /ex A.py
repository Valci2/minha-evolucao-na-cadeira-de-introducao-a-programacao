print('Byte está com fome?')

resp = input() # aqui é a primeira resposta para pergunta ('Byte está com fome?')

if resp == 'sim': # caso sim
    
    print('O que você vai dar para ele comer?')
    comida = input() # escolhe a comida
    
    # caso da comida favorita:

    if comida == 'carne':
        print(f"Byte comeu {comida} e está feliz!")
        print(f"Depois desse banquete, Byte pode tirar um cochilo feliz")
      
    elif comida == 'ração':
        print(f"Byte comeu {comida} e está feliz!")
        print(f"Depois desse banquete, Byte pode tirar um cochilo feliz")
    
    elif comida == 'petisco':
        print(f"Byte comeu {comida} e está feliz!")
        print(f"Depois desse banquete, Byte pode tirar um cochilo feliz")

    # caso comida sem ser a favorita
    else:
        print(f'Byte não gosta de {comida}')
        print("Byte se irritou e foi dormir pra ver se sonha com suas refeições prediletas...")

elif resp == 'não': # caso a primerira resposta seja não
  
    print('Já que Byte não está com fome, ele pode passear')
    print('Está chovendo?')
    
    escolha = input() # aqui é a segunda resposta para pergunta ('Está chovendo?')

    if escolha == 'sim': # caso sim
        print("Já que está chovendo, Byte vai ter que brincar em casa")

    elif escolha == 'não': # caso não
        print('Byte está indo passear')

    else: # caso de resposta fora de sim e não
        print('Insira uma resposta válida')

else:
  print('Insira uma resposta válida')