# lsita dos ingredientes
ingredientes = []

anotação = ''
while anotação != 'E por hoje é só, pessoal!':
    anotação = str(input())

    if anotação not in ingredientes:

        # Anotar ingrediente, adiciona no final da lista
        if anotação == 'Anotar ingrediente':
            ingredientes.append(str(input()))


        # Ingrediente Urgente!, adiciona no inicio da lista
        elif anotação == 'Ingrediente Urgente!':
            ingredientes.insert(0, str(input()))


        # Deixar para depois, tira de algum lugar da lista e adiciona no final
        elif anotação == 'Deixar para depois':
            ingrediente = str(input())
            if ingrediente in ingredientes:
                ingredientes.remove(ingrediente)
                ingredientes.append(ingrediente)


        # Ler a lista para a vovó, lê a lista para vovó ;)
        elif anotação == 'Ler a lista para a vovó':
            quantidade = len(ingredientes)
            for lista in ingredientes:
                quantidade -= 1
                print(f'{lista}', end=', ' if quantidade > 0 else '\n')


        # Saci disse que já tem, elimina um ingredinete se o ingrediente estiver na lista
        elif anotação == 'Saci disse que já tem':
            ingrediente = str(input())
            if ingrediente in ingredientes:
                ingredientes.remove(ingrediente)


        # Saci trocou a ordem, troca a ordem dos itens, através do index
        elif anotação == 'Saci trocou a ordem':

                indice_desejado = int(input())
                item_para_trocar = ingredientes[indice_desejado]

                indice_trocado = int(input())
                item_trocado = ingredientes[indice_trocado]

                if indice_trocado <= len(ingredientes) and indice_desejado <= len(ingredientes):
                    ingredientes.remove(item_para_trocar) # remove o primeiro item que o saci quer trocar
                    ingredientes.insert(indice_trocado, item_para_trocar) # insere o primeiro item no lugar do segundo item

                    ingredientes.remove(item_trocado) # remove o segundo item que o saci quer trocar
                    ingredientes.insert(indice_desejado, item_trocado) # insere o segundo item no lugar do primeiro item

        # organiza a ordem dá lista atreves de uma string
        elif anotação == 'Organizar a lista':

            ingrediente_para_mudar = str(input())
            ingrediente_para_substituir = str(input())

            # verifica se os ingredientes estão na lista
            if ingrediente_para_mudar in ingredientes and ingrediente_para_substituir in ingredientes: 

                a = ingredientes.index(ingrediente_para_mudar) # deixei o nome da variavel de a, mas a é o index do ingrediente que vai ser substituído
                b = ingredientes.index(ingrediente_para_substituir) # b é a mesma coisa, só que é o segundo ingrediente que vai ser trocado 

                ingredientes[a] = ingrediente_para_substituir # substitui o nome do ingrediente que 1 para o o lugar do ingrediente 2
                ingredientes[b] = ingrediente_para_mudar  # substitui o nome do ingrediente que 2 para o o lugar do ingrediente 1


# print antes do print final
print(f"Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: {', '.join(ingredientes)}")
