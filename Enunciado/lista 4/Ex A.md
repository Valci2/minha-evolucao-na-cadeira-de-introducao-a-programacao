Bulma, nossa brilhante cientista e aventureira destemida, está em uma missão crítica: localizar as lendárias Esferas do Dragão, artefatos capazes de invocar o poderoso Shenlong e realizar qualquer desejo!

Bulma, Goku e as Esferas do Dragão

Para auxiliá-la nessa jornada, Bulma conta com seu mais novo invento: o Radar do Dragão, que detecta objetos próximos com precisão incrível. Para cada detecção, o radar fornece as seguintes informações:

    O nome do objeto detectado
    A coordenada X do objeto no mapa
    A coordenada Y do objeto no mapa

Bulma, estrategicamente posicionada na origem do mapa, precisa da sua ajuda para criar um programa que processe os dados do radar.

Seu programa deve analisar uma sequência de detecções do radar. Para cada objeto detectado, siga as instruções abaixo:

Se o radar detectar certos objetos que não são esferas, Bulma fará um comentário específico. Seu programa deve imprimir esses comentários imediatamente após a detecção do objeto correspondente:

    Rocha: Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'
    Árvore: Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'
    Nave: Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'
    Outros Objetos: Para qualquer outro tipo de objeto que não seja "esfera" e não esteja listado acima (ex: "montanha", "animal"): Radar: Detectado um(a) {tipo_objeto}. Não parece ser uma esfera... Continuando a busca. (substitua {tipo_objeto} pelo nome do objeto).

O objetivo principal, claro, é encontrar as Esferas do Dragão! Após analisar todas as detecções, seu programa deve identificar a esfera de maior prioridade e imprimir suas informações.

A prioridade é definida da seguinte forma:

    Critério Principal: A esfera mais próxima de Bulma (ou seja, a que tiver a menor distância euclidiana da origem) tem maior prioridade.
    Critério de Desempate: Se duas ou mais esferas estiverem exatamente à mesma distância, aquela que foi detectada primeiro pelo radar (aparece antes na lista de dados brutos de entrada) tem maior prioridade.

Distancia Euclidiana de P=(x,y) para a origem:

    D = (x^2 + y^2)^0.5

ATENÇÃO!!

Seu código deve ter obrigatóriamente uma função para calcular essa distância

Agora, é com você! Ajude Bulma a encontrar a esfera mais importante e a cumprir sua missão.

Input

A entrada do seu programa seguirá o seguinte formato:

    A primeira linha conterá um número inteiro N, que indica o total de objetos detectados pelo radar.
    Em seguida, haverá N blocos de dados, cada um representando uma detecção. Cada bloco consiste em três linhas:

1. O nome do objeto:

    nome_objeto (string)

2. A posição X do objeto no mapa:

    coordenada_x (inteiro)

3. A posição Y do objeto no mapa:

    coordenada_y (inteiro)

Output

Seu programa deverá gerar saídas específicas com base nos objetos detectados e nas Esferas do Dragão encontradas:
Mensagens para Objetos Comuns

Para cada objeto encontrado que não seja uma esfera, você deve enviar uma mensagem de acordo com o tipo:
rocha:

    Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'

árvore:

    Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'

nave:

    Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'

Outro objeto:

    Radar: Detectado um(a) {nome_objeto}. Não parece ser uma esfera... Continuando a busca.

    Substitua {nome_objeto} pelo nome do objeto detectado

Resultados da Busca por Esferas do Dragão

Após processar todas as detecções, a saída final dependerá se alguma esfera foi encontrada:

    Se pelo menos uma esfera for encontrada: Imprima uma única linha com os detalhes da esfera de maior prioridade:

    ALVO PRIORITÁRIO: Esfera | Distância: {distancia}m | Detecção Original: {posicao_no_radar}°

{distancia}: A distância calculada até Bulma, formatada com exatamente duas casas decimais.

{posicao_no_radar}: A ordem original em que a esfera foi detectada na entrada (1 para a primeira detecção, 2 para a segunda, e assim por diante).

    Se nenhuma esfera for encontrada: Imprima a seguinte mensagem:

    Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!

Examples

Case: 1

Input

3
rocha
10
0
árvore
-5
5
satélite
200
300

Output

Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'
Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'
Radar: Detectado um(a) satélite. Não parece ser uma esfera... Continuando a busca.
Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!

Case: 2

Input

3
esfera
100
0
esfera
0
50
esfera
10
0

Output

ALVO PRIORITÁRIO: Esfera | Distância: 10.00m | Detecção Original: 3°