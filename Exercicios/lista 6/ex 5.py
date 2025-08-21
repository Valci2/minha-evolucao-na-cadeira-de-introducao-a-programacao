def cada_pontuacao(tecnico):
    return tecnico['pontuacao']

def calcula_pontuacao_jogador(jogador):
    pontuacao = 0
    pontuacao += jogador['gols_feitos'] * 8 + jogador['assistencias'] * 5
    pontuacao -= jogador['amarelos'] * 1 + jogador['vermelhos'] * 3

    if jogador['posicao'] in ['goleiro', 'zagueiro', 'lateral'] and jogador['gols_sofridos'] == 0:
        pontuacao += 5
        
    return pontuacao

def organiza_jogador(linha):
    nome, posicao, g, a, am, vm, gs = linha.split(',')
    jogador = {
        'nome': nome,
        'posicao': posicao,
        'gols_feitos': int(g),
        'assistencias': int(a),
        'amarelos': int(am),
        'vermelhos': int(vm),
        'gols_sofridos': int(gs)
    }
    jogador['pontuacao'] = calcula_pontuacao_jogador(jogador)
    return jogador

def calcula_pontuacao_time(time):
    total_de_pontuacao = 0
    for pontos in time:
        total_de_pontuacao += pontos['pontuacao']
    return total_de_pontuacao

def encontra_melhor_substituicao(titulares, reservas):

    prioridade_posicao = {}
    prioridade_posicao['goleiro'] = 1,
    prioridade_posicao['lateral'] = 2,
    prioridade_posicao['zagueiro'] = 3,
    prioridade_posicao['meia'] = 4,
    prioridade_posicao['atacante'] = 5

    melhor_ganho = 0
    melhor_substituicao = ''
    pontuacao_original = calcula_pontuacao_time(titulares)

    for reserva in reservas:
        for titular in [t for t in titulares if t['posicao'] == reserva['posicao']]:
            time_simulado = titulares.copy()
            time_simulado.remove(titular)
            time_simulado.append(reserva)

            nova_pontuacao = calcula_pontuacao_time(time_simulado)
            ganho = nova_pontuacao - pontuacao_original

            if ganho > melhor_ganho:
                melhor_ganho = ganho
                melhor_substituicao = (titular, reserva)

            elif ganho == melhor_ganho and ganho > 0:

                if melhor_substituicao == '':
                    melhor_substituicao = (titular, reserva)

                else:
                    atual = melhor_substituicao
                    p1 = prioridade_posicao[reserva['posicao']]
                    p2 = prioridade_posicao[atual[1]['posicao']]

                    if p1 < p2 or (p1 == p2 and titular['nome'] > atual[0]['nome']):
                        melhor_substituicao = (titular, reserva)

    return melhor_substituicao, melhor_ganho


# --- PROGRAMA PRINCIPAL ---
quantidade_de_tecnicos = int(input())
tecnicos = []
resultados = []

for _ in range(quantidade_de_tecnicos):
    nome_tecnico = input()
    tecnicos.append(nome_tecnico)
    titulares = []
    reservas = []
    lidos = 0

    while lidos < 16:
        linha = input()
        if linha == 'titulares':
            for _ in range(11):
                jogador = organiza_jogador(input())
                titulares.append(jogador)
                lidos += 1
        elif linha == 'reservas':
            for _ in range(5):
                jogador = organiza_jogador(input())
                reservas.append(jogador)
                lidos += 1

    substituicao, ganho = encontra_melhor_substituicao(titulares, reservas)
    pontuacao_final = calcula_pontuacao_time(titulares)
    fez_substituicao = False

    if substituicao:
        titular_que_saem, reserva_que_entram = substituicao
        pontuacao_final += ganho
        fez_substituicao = True

    resultados.append({
        'nome': nome_tecnico,
        'pontuacao': pontuacao_final,
        'fez_substituicao': fez_substituicao,
        'titular': substituicao[0]['nome'] if substituicao else '',
        'reserva': substituicao[1]['nome'] if substituicao else ''
    })

# Saída
print(f"Os técnicos que participarão da avaliação da rodada serão {', '.join(tecnicos)}.")

for r in resultados:
    if r['fez_substituicao']:
        print(f"{r['nome']} é um gênio da bola mesmo, a substituição de {r['titular']} por {r['reserva']} fez ele ganhar pontos!")
    else:
        print(f"Pode cortar {r['nome']} dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...")

vencedor = max(resultados, key=cada_pontuacao)
print(f"{vencedor['nome']} é incrível ganhou essa rodada com {vencedor['pontuacao']} pontos!")

if not vencedor['fez_substituicao']:
    print(f"Temos que pedir desculpas a {vencedor['nome']}, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!")