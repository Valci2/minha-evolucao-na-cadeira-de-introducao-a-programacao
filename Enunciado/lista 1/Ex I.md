Byte é um cãozinho curioso e destemido — exceto quando se trata de passeios por lugares suspeitos… Dizem que nos labirintos vive uma assustadora Python — e não estamos falando da linguagem de programação! 😱

Para enfrentar mais essa aventura, Byte precisa de um bom acompanhante. Quatro professores estão dispostos a ajudá-lo: Prof. Fernanda Madeiral, Prof. Ricardo Massa, Prof. Juliano Iyoda e Prof. Sérgio Soares. Cada um deles tem uma disponibilidade específica, e sua missão é escrever um programa que, a partir das entradas sobre o dia, turno, horário (em alguns casos), local e humor de Byte, defina quem vai acompanhá-lo.

Os passeios podem acontecer em três turnos: manhã, tarde ou noite. Os locais possíveis são o parque, o bosque ou um labirinto — onde dizem que a assustadora Python vive atormentando os curiosos. Já o humor de Byte varia entre: calminho, pura energia e rebelde (quando ele está quase indomável).

Labirinto

Input

Entradas esperadas (seguindo essa ordem):

Inicialmente, seu programa receberá a entrada com o dia da semana: segunda-feira, terça-feira, …

    (str) dia_semana

Seguido pela entrada do turno: manhã, tarde ou noite.

    (str) turno

Apenas se o dia da semana recebido for segunda-feira ou sexta-feira, haverá uma entrada extra, que deverá informar o horário numericamente (entrada de número inteiro):

    (int) hora

Em seguida, receberá o local: parque, bosque ou labirinto

    (str) local

Por último, o humor de Byte: calminho, pura energia ou rebelde

    (str) humor_Byte

Output
Outputs conforme o dia da semana:

Se o dia da semana for segunda-feira até as 7h da manhã:

    “Byte acordou em plena madrugada, quem tá acordado(a) pra levar ele essa hora?!"

Por outro lado, se for sexta-feira a partir das 16h:

    "SEXTOU, quem vai levar Byte pra bater pata por aí??"

Outputs conforme o local:

Se o local for labirinto:

    "Byte quer passear num labirinto, cuidado pra não se perder!"

Outputs conforme o humor de Byte:

Se o humor de Byte for pura energia:

    "Byte está energizado com a ideia de passear, leve uma bolinha pra ele!"

Se o humor de Byte for calminho:

    “Byte está calminho, o passeio vai ser na paz, pode confiar!"

Se o humor de Byte for rebelde:

    "Byte está se comportando mal hoje, vamos ver quem terá coragem para acompanhá-lo em seu passeio"

Como Decidir o(a) Acompanhante de Byte:

Apenas 1 professor acompanha Byte, considerando-se as condições abaixo (nessa ordem):
1- A Prof. Fernanda Madeiral adora trabalhar com desafios lógicos e topou participar de passeios por labirintos, em qualquer dia e horário, desde que Byte não esteja rebelde.

Para esse caso, imprima:

    “A prof. Fernanda Madeiral aceitou o desafio: labirinto caótico, uma Python no caminho… e Byte como companheiro. Afinal, o que pode dar errado?”

2- Se Byte estiver rebelde e o local do passeio for labirinto, o acompanhante será o Prof. Juliano Iyoda, independente do dia e horário. Nesse caso, você deve imprimir o seguinte:

    “Mestre Iyoda e Byte adentram o labirinto. Uma missão ousada e um destino desconhecido."

3- O Prof. Sergio Soares participará de passeios no turno da manhã, desde que não seja na segunda-feira. Nesses casos, imprima:

    "Nesta manhã de {dia_semana}, é o Prof. Sergio Soares quem comanda o passeio com Byte"

4- O Prof. Ricardo Massa passeará com Byte nas manhãs de segunda e nas tardes de todos os dias, desde que o passeio seja pelo parque ou pelo bosque.

Se for segunda-feira de manhã, imprima:

    "{dia_semana}: uns indo pro trabalho, outros lidando com o Byte. Prof. Ricardo Massa escolheu a segunda opção. Força, guerreiro. {local}, aí vamos nós."

Se for qualquer dia no turno da tarde, imprima:

    "Sol da tarde, coleira na mão: prof. Ricardo Massa entra em cena para o passeio com Byte."

5- O Prof. Juliano Iyoda não tem medo dos perigos noturnos e passeará com Byte no parque ou no bosque no turno da noite. Nesses casos, imprima:

    "Quando a noite cai e Byte chama, Mestre Iyoda atende. Que o {local} esteja preparado para essa dupla!”

💡Dica: utilize F-strings para imprimir os locais e os dias da semana, quando necessário.
Clique aqui para saber como utilizá-las.

Examples

Case: 1

Input

segunda-feira
manhã
4
labirinto
calminho

Output

Byte acordou em plena madrugada, quem tá acordado(a) pra levar ele essa hora?!
Byte quer passear num labirinto, cuidado pra não se perder!
Byte está calminho, o passeio vai ser na paz, pode confiar!
A prof. Fernanda Madeiral aceitou o desafio: labirinto caótico, uma Python no caminho… e Byte como companheiro. Afinal, o que pode dar errado?