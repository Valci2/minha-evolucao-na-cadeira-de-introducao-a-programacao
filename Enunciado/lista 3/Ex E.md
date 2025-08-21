O malvado Turbo escapou do próprio jogo com a ambição de dominar todos os jogos de corrida do fliperama. Infiltrado em “Corrida Doce”, ele apagou a memória de todos os habitantes e assumiu a identidade do Rei Doce para manter seu disfarce. Para continuar no poder, precisa manter a verdadeira herdeira do trono, Vanellope von Schweetz, fora da competição, usando a desculpa de que ela é apenas um bug no sistema por ter Pixelexia.

Mesmo assim, Vanellope sempre acreditou que nasceu para correr. Determinada a seguir seu sonho, enfrentou diversos obstáculos até conquistar uma vaga nas classificatórias. Porém, sabotada pelo Rei Doce, ela se vê em desespero: sem carro e sem chances de competir.

GIF do filme Detona Ralph no momento em que vanellope se inscreve na corrida

Com a urgência de construir um carro veloz, Vanellope corre até a fábrica determinada a garantir sua participação na corrida, mesmo que o Rei Doce tente sabotá-la durante o percurso.

É nesse momento decisivo que ela recorre a você, um talentoso estudante do CIn, para ajudá-la. Usando seus conhecimentos em listas, sua missão é construir um carro de respeito e dar a Vanellope a chance de derrotar o malvado Turbo de uma vez por todas!
🚗 Composição Ideal do Carro

Doce Redondo Maciço - para ser usado como roda.

    Mentos
    Jujuba

Doce largo - para formar o corpo do carro.

    Bolo de rolo
    Barra de chocolate
    Banda de ovo de Páscoa

Doce Redondo Furado - para ser o volante.

    Pretzel
    Donuts

Input

Para que Vanellope tenha o carro mais doce e potente do reino, é essencial escolher apenas os melhores ingredientes da Corrida Doce. Doces estragados devem ser descartados imediatamente!

Portanto, primeiro você deverá receber os doces e sua qualidade (alta qualidade, qualidade mediana ou estragado) até o recebimento da frase “Recursos Esgotados”. Da seguinte forma:

    doce1 - estragado

    doce2 - alta qualidade

    doce3 - qualidade mediana

    …

    Recursos Esgotados

ATENÇÃO: O Rei Doce poderá sabotar Vanellope. Assim o programa poderá receber entre os doces a frase abaixo. Nesse caso, todos os ingredientes que já foram inseridos no carro serão perdidos, devendo entrar para a lista de doces descartados!

    O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!

OBS: Os doces de qualidade mediana podem ser utilizados, mas caso um doce de mesmo tipo e com qualidade superior seja recebido, ele substitui o anterior no carro, e o doce de qualidade inferior é automaticamente descartado.

Output

Primeiramente você deverá printar um incentivo para o começo da construção.

    Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!

Em caso de sabotagem do Rei Doce você deverá printar:

    Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO

Caso ela consiga completar o carro (Roda, corpo e volante), mas apenas com doces de qualidade mediana:

    Pelo menos anda! Você consegue!

Caso o carro seja finalizado com excelência ( Carro completo com pelo menos um dos elementos do carro sendo de alta qualidade) você deve printar:

    Conseguimos! Impossível você não ganhar essa corrida, Vanellope!

    Para fazer o carro você utilizou {estrutura} para ser a estrutura do carro, {volante} para o volante, {doce_rodas} para compor as rodas!

Em caso dos materiais terminarem e o carro ficar incompleto:

    Sinto muito, Vanellope. Não consegui te ajudar dessa vez.

Caso algum doce tenha sido descartado, você também deverá printar todos os itens que foram descartados independentemente do motivo (falta de necessidade, estarem estragados, sabotagem do rei doce), na ordem que eles foram descartados e separados por “, ”

    Alguns doces foram descartados. São eles:

    {doce1}, {doce2}, {doce3}

OBS: Caso nenhum doce tenha sido descartado, nenhuma mensagem sobre descarte deve ser exibida.

Examples

Case: 1

Input

Barra de chocolate - qualidade mediana
Pretzel - qualidade mediana
Barra de chocolate - alta qualidade
Mentos - alta qualidade
Donuts - alta qualidade
Banda de ovo de Páscoa - alta qualidade
Pretzel - qualidade mediana
Recursos Esgotados

Output

Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!
Conseguimos! Impossível você não ganhar essa corrida, Vanellope!
Para fazer o carro você utilizou Barra de chocolate para ser a estrutura do carro, Donuts para o volante, Mentos para compor as rodas!
Alguns doces foram descartados. São eles:
Barra de chocolate, Pretzel, Banda de ovo de Páscoa, Pretzel

Case: 2

Input

Jujuba - qualidade mediana
Barra de chocolate - qualidade mediana
Pretzel - qualidade mediana
Mentos - qualidade mediana
Donuts - alta qualidade
Mentos - alta qualidade
O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!
Bolo de rolo - alta qualidade
Mentos - estragado
Jujuba - alta qualidade
Donuts - qualidade mediana
Recursos Esgotados

Output

Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!
Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO
Conseguimos! Impossível você não ganhar essa corrida, Vanellope!
Para fazer o carro você utilizou Bolo de rolo para ser a estrutura do carro, Donuts para o volante, Jujuba para compor as rodas!
Alguns doces foram descartados. São eles:
Mentos, Pretzel, Jujuba, Mentos, Barra de chocolate, Donuts, Mentos