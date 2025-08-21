dia_semana = str(input()) # o dia da que estamos na semana
turno = str(input()) # turno da manhã, tarde ou noite

if dia_semana == 'segunda-feira' or dia_semana == 'sexta-feira': # caso o dia for segunda ou sexta ele pergunta o horario
    hora = int(input())
    if dia_semana == 'segunda-feira' and hora < 7:
        print('Byte acordou em plena madrugada, quem tá acordado(a) pra levar ele essa hora?!')
    elif dia_semana == 'sexta-feira' and hora >= 16:
        print('SEXTOU, quem vai levar Byte pra bater pata por aí??')

local = str(input()) # local onde vai
humor = str(input()) # humor de byte

# output se local for o labrinto
if local == 'labirinto':
    print('Byte quer passear num labirinto, cuidado pra não se perder!')

# output de humor
if humor == 'pura energia':
    print('Byte está energizado com a ideia de passear, leve uma bolinha pra ele!')
elif humor == 'calminho':
    print('Byte está calminho, o passeio vai ser na paz, pode confiar!')
elif humor == 'rebelde':
    print('Byte está se comportando mal hoje, vamos ver quem terá coragem para acompanhá-lo em seu passeio')

# escolha dos acompanhantes (na ordem especificada)

# Prof. Fernanda Madeiral
if local == 'labirinto' and humor != 'rebelde':
    print('A prof. Fernanda Madeiral aceitou o desafio: labirinto caótico, uma Python no caminho… e Byte como companheiro. Afinal, o que pode dar errado?')

# Mestre Iyoda (se Byte rebelde e labirinto)
elif local == 'labirinto' and humor == 'rebelde': 
    print('Mestre Iyoda e Byte adentram o labirinto. Uma missão ousada e um destino desconhecido.')

# Prof. Sergio Soares (manhã, não segunda)
elif turno == 'manhã' and dia_semana != 'segunda-feira': 
    print(f'Nesta manhã de {dia_semana}, é o Prof. Sergio Soares quem comanda o passeio com Byte')

# Prof. Ricardo Massa (segunda manhã, parque ou bosque)
elif (dia_semana == 'segunda-feira' and turno == 'manhã' and (local == 'parque' or local == 'bosque')): 
    print(f'{dia_semana}: uns indo pro trabalho, outros lidando com o Byte. Prof. Ricardo Massa escolheu a segunda opção. Força, guerreiro. {local}, aí vamos nós.')

# Prof. Ricardo Massa (tarde, parque ou bosque)
elif turno == 'tarde' and (local == 'parque' or local == 'bosque'): 
    print('Sol da tarde, coleira na mão: prof. Ricardo Massa entra em cena para o passeio com Byte.')

# Mestre Iyoda (noite, parque ou bosque)
elif turno == 'noite' and (local =='parque' or local == 'bosque'): 
    print(f'Quando a noite cai e Byte chama, Mestre Iyoda atende. Que o {local} esteja preparado para essa dupla!')