# locais de paris
locais_de_paris = ['Torre Eiffel', 'Museu do Louvre', 'Catacumbas de Paris', 
                   'Biblioteca Nacional', 'Galeria Lafayette', 'Parque dos Príncipes', 
                   'Catedral de Notre-Dame', 'Jardim de Luxemburgo', 'Padaria Dupain Cheng']

# locais de paris com segurança baixa
locais_com_baixa_segurança = ['Catacumbas de Paris', 'Parque dos Príncipes', 'Padaria Dupain Cheng']

# listas para armazenar os suspeitos e locais inválidos
suspeitos_locais = []
suspeitos_tempo = []
suspeitos_seguranca = []
suspeitos_testemunhas = []
locais_invalidos = []
locais_com_tempo_invalidos = []
seguranca_baixa = []
hora = 0

# faz os loops dos seis suspeitos
for c in range(0, 6):

    suspeito = str(input()).split(' - ')
    nome = suspeito[0]
    horario_str = suspeito[1]
    local = suspeito[2]
    testemunha = suspeito[3]

    # Converte o horário para minutos para facilitar a comparação
    horas_minutos = horario_str.split(":")
    horario_int = int(horas_minutos[0]) * 100 + int(horas_minutos[1])

    # inicialização das verificações dos suspeitos
    # Verifica se o local é válido
    if local not in locais_de_paris:
        locais_invalidos.append(local)
        suspeitos_locais.append(nome)

    # Verifica se o local é válido e se o horário está correto
    if len(locais_invalidos) == 0 and local in locais_de_paris:
        if local == 'Torre Eiffel' and horario_int not in range(900, 2300):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Museu do Louvre' and horario_int not in range(800, 1800):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Catacumbas de Paris' and horario_int not in range(1000, 2000):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Biblioteca Nacional' and horario_int not in range(700, 2200):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Galeria Lafayette' and horario_int not in range(1000, 2100):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Parque dos Príncipes' and horario_int not in range(600, 2300):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Catedral de Notre-Dame' and horario_int not in range(800, 1830):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Jardim de Luxemburgo' and horario_int not in range(700, 1900):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
        elif local == 'Padaria Dupain Cheng' and horario_int not in range(400, 2000):
            locais_com_tempo_invalidos.append(local)
            suspeitos_tempo.append(nome)
            hora = horario_str
    
    # Verifica se o local é de segurança baixa
    if len(locais_com_tempo_invalidos) == 0 and local in locais_de_paris:
        if local in locais_com_baixa_segurança:
            seguranca_baixa.append(local)
            suspeitos_seguranca.append(nome)


    # Verifica se não há testemunha
    if len(seguranca_baixa) == 0 and local in locais_de_paris:
        if testemunha == 'sim' or testemunha == 'nenhuma':
            if testemunha == 'nenhuma':
                suspeitos_testemunhas.append(nome)


# deixa as listas em ordem alfabetica
suspeitos_locais.sort()
suspeitos_tempo.sort()
suspeitos_seguranca.sort()
suspeitos_testemunhas.sort()
locais_invalidos.sort()
locais_com_tempo_invalidos.sort()
seguranca_baixa.sort()

# Verifica as condições e imprime o resultado
# local invalido
if len(locais_invalidos) == 1:
    print(f'Esse lugar {locais_invalidos[0]} nem existe! {suspeitos_locais[0]} com certeza foi akumatizado!')

elif len(locais_invalidos) > 1:
    print(f"{', '.join(locais_invalidos)} nem existem! {', '.join(suspeitos_locais)} estão mentindo!")

# fora do tempo de funcionamento
elif len(locais_com_tempo_invalidos) == 1:
    print(f'{locais_com_tempo_invalidos[0]} nem estava aberto às {hora}! {suspeitos_tempo[0]} recebeu memórias falsas!')

elif len(locais_com_tempo_invalidos) > 1:
    print(f"{', '.join(locais_com_tempo_invalidos)} estavam fechados nesse horário! {', '.join(suspeitos_tempo)} podem ter sido manipulados pelo Hawk Moth!")

# locais de segurança baixa
elif len(seguranca_baixa) == 1:
    print(f'{suspeitos_seguranca[0]} estava em um local de segurança baixa... Ele pode ter mentido!')

elif len(seguranca_baixa) > 1:
    print(f"{', '.join(suspeitos_seguranca)} estavam em locais de segurança baixa... Eles podem estar forjando um álibi!")

# testemunhas
elif len(suspeitos_testemunhas) == 1:
    print(f'{suspeitos_testemunhas[0]} não teve testemunha para confirmar o álibi. É o mais suspeito até agora.')

elif 2 <= len(suspeitos_testemunhas) <= 5:
    print(f"{', '.join(suspeitos_testemunhas)} não foram confirmados por ninguém. O Hawk Moth pode vir atrás deles de novo")

elif len(suspeitos_testemunhas) == 6:
    print('Ninguém viu ninguém… estranho!!')

# todos os suspeitos com álibis válidos
else:
    print('Poxa vida, todos os àlibis parecem válidos… mas algo continua errado')

