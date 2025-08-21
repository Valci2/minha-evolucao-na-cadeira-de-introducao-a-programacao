# Variáveis para armazenar as partes do carro
estrutura_carro = "Nenhuma"
volante_carro = "Nenhum"
roda_carro = "Nenhuma"

# Flags para controle de qualidade e preenchimento
estrutura_qualidade_alta = False
volante_qualidade_alta = False
roda_qualidade_alta = False

estrutura_preenchida = False
volante_preenchido = False
roda_preenchida = False

# Lista para doces descartados
doces_descartados = []

# Flag para verificar se houve sabotagem (apenas para a mensagem inicial de sabotagem)
sabotagem_anunciada = False

print('Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!')

# Loop dos inputs
entrada = input()
while entrada != "Recursos Esgotados":

    if entrada == "O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!":
        if not sabotagem_anunciada: # para printar uma uma vez só
            print('Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO')
            sabotagem_anunciada = True

        # Se houver sabotagem, todos os ingredientes atuais são descartados
        if roda_preenchida:
            doces_descartados.append(roda_carro)
            roda_carro = "Nenhuma"
            roda_qualidade_alta = False
            roda_preenchida = False

        if estrutura_preenchida:
            doces_descartados.append(estrutura_carro)
            estrutura_carro = "Nenhuma"
            estrutura_qualidade_alta = False
            estrutura_preenchida = False

        if volante_preenchido:
            doces_descartados.append(volante_carro)
            volante_carro = "Nenhum"
            volante_qualidade_alta = False
            volante_preenchido = False

        # separa as o nome do doce da qualidade
    else:
        partes_doce = entrada.split(' - ')
        nome_doce = partes_doce[0]
        qualidade_doce = partes_doce[1]

        if qualidade_doce == "estragado":
            doces_descartados.append(nome_doce)
        else:
            # Lógica para rodas (Mentos, Jujuba)
            if nome_doce == "Mentos" or nome_doce == "Jujuba":
                if not roda_preenchida: # Se a roda não está preenchida
                    roda_carro = nome_doce
                    roda_preenchida = True
                    if qualidade_doce == "alta qualidade":
                        roda_qualidade_alta = True
                else: # Roda já preenchida
                    if qualidade_doce == "alta qualidade":
                        if not roda_qualidade_alta: # Se a qualidade atual é mediana e a nova é alta
                            doces_descartados.append(roda_carro) # Descarta o doce antigo de qualidade mediana
                            roda_carro = nome_doce
                            roda_qualidade_alta = True
                        else: # Já tem alta qualidade, o novo de alta qualidade é descartado
                            doces_descartados.append(nome_doce)
                    else: # Nova qualidade é mediana, mas já tem uma roda (seja mediana ou alta), então descarta
                        doces_descartados.append(nome_doce)

            # Lógica para o corpo (Bolo de rolo, Barra de chocolate, Banda de ovo de Páscoa)
            elif nome_doce == "Bolo de rolo" or nome_doce == "Barra de chocolate" or nome_doce == "Banda de ovo de Páscoa":
                if not estrutura_preenchida:
                    estrutura_carro = nome_doce
                    estrutura_preenchida = True
                    if qualidade_doce == "alta qualidade":
                        estrutura_qualidade_alta = True
                else:
                    if qualidade_doce == "alta qualidade":
                        if not estrutura_qualidade_alta:
                            doces_descartados.append(estrutura_carro) # Descarta o doce antigo de qualidade mediana
                            estrutura_carro = nome_doce
                            estrutura_qualidade_alta = True
                        else:
                            doces_descartados.append(nome_doce)
                    else:
                        doces_descartados.append(nome_doce)

            # Lógica para o volante (Pretzel, Donuts)
            elif nome_doce == "Pretzel" or nome_doce == "Donuts":
                if not volante_preenchido:
                    volante_carro = nome_doce
                    volante_preenchido = True
                    if qualidade_doce == "alta qualidade":
                        volante_qualidade_alta = True
                else:
                    if qualidade_doce == "alta qualidade":
                        if not volante_qualidade_alta:
                            doces_descartados.append(volante_carro) # Descarta o doce antigo de qualidade mediana
                            volante_carro = nome_doce
                            volante_qualidade_alta = True
                        else:
                            doces_descartados.append(nome_doce)
                    else:
                        doces_descartados.append(nome_doce)

    entrada = input() # Lê a próxima entrada

# Resultado Final

# Saída da Construção do Carro
if estrutura_preenchida and volante_preenchido and roda_preenchida:
    if estrutura_qualidade_alta or volante_qualidade_alta or roda_qualidade_alta:
        print(f'Conseguimos! Impossível você não ganhar essa corrida, Vanellope!')
        print(f'Para fazer o carro você utilizou {estrutura_carro} para ser a estrutura do carro, {volante_carro} para o volante, {roda_carro} para compor as rodas!')
    else:
        print('Pelo menos anda! Você consegue!')
else:
    print('Sinto muito, Vanellope. Não consegui te ajudar dessa vez.')

# Saída dos Doces Descartados
if len(doces_descartados) > 0:
    print(f'Alguns doces foram descartados. São eles:\n{", ".join(doces_descartados)}')