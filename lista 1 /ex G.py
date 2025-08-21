x = 500 # cin dentro do plano cartesiano, eixo x
y = 100 # cin dentro do plano cartesiano, eixo y

escolha = str(input()) # local a ser visitado

if escolha == 'Concha Acústica da UFPE':

    local_x = 400 # eixo x da conta acústica
    local_y = 500 # eixo y
    x_e_y = abs(x-local_x)**2 + abs(y-local_y)**2 # pega os valores absolutos dos dois eixos eleva ao quadrado e por fim soma os dois.
    total = x_e_y**(1/2) # faz a radicição do calculo feito antes.
    distancia_ida_volta = total*2 # pega essa raiz e multiplica por dois, para o resultado ser a ida e a volta da distancia percorrida.
    distancia_arredondada = round(distancia_ida_volta) # arredonda a distancia de ida e volta.
    tempo = (distancia_arredondada/2/60) # pega a distancia arreedondada e divide pelo velocidade percorrida e depois divide pelos segundos.
    tempo_total = round(tempo) + 15 # arredonda o tempo de ida e volta e soma os 15 minutos que ele ficou dentro do local escolhido.


    print(f'Byte visitou Concha Acústica da UFPE, caminhou {distancia_arredondada} metros e gastou {tempo_total} minutos passeando!')
    print('Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!')

elif escolha == 'Laguinho da UFPE':

    local_x = 300
    local_y = 1000
    x_e_y = abs(x-local_x)**2 + abs(y-local_y)**2
    total = x_e_y**(1/2)
    distancia_ida_volta = total*2
    distancia_arredondada = round(distancia_ida_volta)
    tempo = (distancia_arredondada/2/60)
    tempo_total = round(tempo) + 15

    print(f'Byte visitou Laguinho da UFPE, caminhou {distancia_arredondada} metros e gastou {tempo_total} minutos passeando!')
    print('Nossa, mas esse lago é longe hein?!')

elif escolha == 'Hospital das Clínicas':

    local_x = 1000
    local_y = 1000
    x_e_y = abs(x-local_x)**2 + abs(y-local_y)**2
    total = x_e_y**(1/2)
    distancia_ida_volta = total*2
    distancia_arredondada = round(distancia_ida_volta)
    tempo = (distancia_arredondada/2/60)
    tempo_total = round(tempo) + 15

    print(f'Byte visitou Hospital das Clínicas, caminhou {distancia_arredondada} metros e gastou {tempo_total} minutos passeando!')
    print('Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!')

elif escolha == 'Ginásio e Pista de Atletismo da UFPE':

    local_x = 800
    local_y = 100
    x_e_y = abs(x-local_x)**2 + abs(y-local_y)**2
    total = x_e_y**(1/2)
    distancia_ida_volta = total*2
    distancia_arredondada = round(distancia_ida_volta)
    tempo = (distancia_arredondada/2/60)
    tempo_total = round(tempo) + 15

    print(f'Byte visitou Ginásio e Pista de Atletismo da UFPE, caminhou {distancia_arredondada} metros e gastou {tempo_total} minutos passeando!')
    print('Que legal! O Ginásio é bem perto do CIn!')