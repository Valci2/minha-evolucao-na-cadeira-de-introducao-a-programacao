Byte, o cãozinho mais querido do Centro de Informática, decidiu tirar o dia para explorar novos lugares da UFPE. Mas como é muito apegado ao CIn, não pretende se afastar por muito tempo. Seu plano é simples: visitar apenas UM ponto da universidade que ele considera interessante, aproveitar um pouco o passeio e depois voltar para casa.

ALT text

Para organizar tudo direitinho, Byte usou um mapa da universidade baseado em coordenadas cartesianas. O CIn, seu ponto de partida e de retorno, está localizado na posição (500, 100). Como gosta de praticidade, Byte sempre se desloca em linha reta, buscando a menor distância entre os pontos. Além disso, ele caminha a uma velocidade constante de 2 m/s.

Mas Byte não quer só andar — ele também pretende parar para olhar melhor o lugar e descansar! Por isso, ele decidiu que fará uma pausa de 15 minutos no local visitado durante seu passeio.

Agora que o trajeto está definido, aqui estão os quatro locais que Byte considera visitar, junto com suas posições no mapa:

        Concha Acústica da UFPE → (400, 500)
        Laguinho da UFPE → (300, 1000)
        Hospital das Clínicas → (1000, 1000)
        Ginásio e Pista de Atletismo da UFPE → (800, 100)

Uma cópia do mapa de Byte pode ser visto abaixo:

Alt text

Cada unidade do mapa representa 1 metro na realidade, ou seja, uma distância de 10 no mapa representa 10 metros.

A sua missão agora é ajudar Byte e desenvolver um algoritmo que calcule:

        A distância total percorrida EM METROS, considerando o trajeto: CIn → Local Visitado → CIn.
        O tempo total gasto EM MINUTOS, somando o tempo de deslocamento com a pausa.

Input

Inicialmente, será informado o lugar que Byte visitará:

    Lugar (string)

Output

Ao final do algoritmo, deverá ser exibida a seguinte mensagem:

    Byte visitou {lugar}, caminhou {distancia_em_metros} metros e gastou {tempo_em_minutos} minutos passeando!

Obs.: Tanto o valor da distância como o do tempo devem ser formatados para ZERO casas decimais.

Após isso, o programa deve imprimir uma mensagem que representa um comentário de Byte sobre o local:

Caso o lugar visitado seja a Concha Acústica da UFPE:

    Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!

Caso seja Laguinho da UFPE o lugar visitado por Byte:

    Nossa, mas esse lago é longe hein?!

Se for o Hospital das Clínicas:

    Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!

Por fim, se o local visitado for o Ginásio e Pista de Atletismo da UFPE:

    Que legal! O Ginásio é bem perto do CIn!

Examples

Case: 1

Input

Concha Acústica da UFPE

Output

Byte visitou Concha Acústica da UFPE, caminhou 825 metros e gastou 22 minutos passeando!
Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!