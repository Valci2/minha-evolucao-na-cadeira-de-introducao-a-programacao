CBF decidiu inovar no jeito de avaliar seus técnicos. Para isso, criou um simulador de desempenho estilo Cartola, onde os técnicos escalam seus jogadores e ganham pontos conforme o desempenho individual dos atletas.

Então, para desenvolver esse aplicativo, a CBF entrou em contato com você, estudante de Introdução à Programação, para criar um sistema simples, porém eficiente, que simule uma rodada de avaliações.

imagem_cartola_cbf

As posições válidas de cada jogador são:

    goleiro
    zagueiro
    lateral
    meia
    atacante

📊 Regras de Pontuação

A pontuação de cada jogador será calculada com base nos seguintes critérios:

+8 pontos por gol feito

+5 pontos por assistência

-1 ponto por cartão amarelo

-3 pontos por cartão vermelho

+5 pontos de bônus defensivo se: o jogador for goleiro, zagueiro ou lateral e o número de gols sofridos for zero

OBS: Não é necessário considerar regras como a equivalência de dois cartões amarelos a um cartão vermelho. Além disso, caso um jogador da linha defensiva sofra um gol, isso não implica que os demais jogadores da defesa também tenham sofrido.

🔁 Substituição Inteligente

Existe uma maneira de substituir UM jogador que pontuar mal na rodada, de acordo com essas regras:

• Apenas 1 reserva pode substituir 1 titular por time.

• Só terá um reserva por posição, ou seja 1 goleiro, 1 zagueiro, 1 lateral, 1 meia e 1 atacante.

• A substituição só acontece se resultar em um aumento na pontuação total do time.

• O reserva só pode substituir um jogador da mesma posição.

• Se houver várias opções de possíveis reservas, escolha aquela com o maior ganho líquido de pontos.

• Em caso de empate no ganho entre dois reservas, utilize a prioridade da posição para decidir:

Ordem de prioridade da posição (da maior para a menor):

    1º goleiro

    2º lateral

    3º zagueiro

    4º meia

    5º atacante

• Se ainda houver empate entre jogadores da mesma posição e mesmo ganho, então escolha para ser substituído dos titulares aquele que o nome seja lexicograficamente maior (vem depois na comparação alfabética das palavras).

• Se nenhuma substituição gerar melhoria, nenhuma troca deve ser feita.

• Sempre vão haver 5 reservas (como foi dito acima, um de cada posição).

Input

A entrada começa com um número inteiro N, representando o número de técnicos participantes da liga.

    N

Para cada técnico será recebido uma entrada com o nome do técnico:

    nome_tecnico

Em seguida, as informações dos jogadores que virão em blocos, precedidas por um comando que indica qual o conjunto de jogadores será informado e depois os dados sobre esses jogadores. Ou seja, a palavra titulares indica o início da entrada dos 11 jogadores titulares, e a palavra reservas indica o início da entrada dos 5 reservas.**

    comando

    informacoes_dos_jogadores

Segue exemplo de uma entrada genérica, para melhor compreensão:

    tecnico1

    titulares

    nome1,goleiro,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome2,zagueiro,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome3,zagueiro,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome4,lateral,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome5,lateral,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome6,meia,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome7,meia,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome8,meia,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome9,atacante,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome10,atacante,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    nome11,atacante,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    reservas

    reserva1,goleiro,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    reserva2,zagueiro,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    reserva3,lateral,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    reserva4,meia,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

    reserva5,atacante,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos

OBS: A ordem não é necessariamente titulares → reservas.

OBS: As posições dos titulares sempre terão essa distribuição: 1 goleiro, 2 zagueiros, 2 laterais, 3 meias e 3 atacantes.

OBS: Cada linha de jogador contém 7 valores, separados por vírgula sem espaço, nesta ordem:

    <nome>,<posição>,<gols_feitos>,<assistencias>,<amarelos>,<vermelhos>,<gols_sofridos>

Output

Ao receber todas as entradas, imprima a lista de técnicos no seguinte formato:

    “Os técnicos que participarão da avaliação da rodada serão <nome_1>, <nome_2>, … , <nome_n>.”

OBS: A ordem dos nomes deve ser a mesma da entrada.

Para cada técnico, se ele fez uma substituição imprima:

    “<nome_do_técnico> é um gênio da bola mesmo, a substituição de <nome_do_titular> por <nome_do_reserva> fez ele ganhar pontos!”

Se não:

    “Pode cortar <nome_do_tecnico> dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...”

Após avaliar todos os técnicos, imprima o vencedor (ou seja, o técnico com maior pontuação final) da seguinte forma:

    “<nome_do_vencedor> é incrível ganhou essa rodada com <pontuação_total> pontos!”

Se o vencedor não realizou nenhuma substituição, também imprima a seguinte frase:

    “Temos que pedir desculpas a <nome_do_vencedor>, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!”

Examples

Case: 1

Input

2
Hélio dos Anjos
titulares
Muriel,goleiro,0,0,0,0,0
Carlinhos,zagueiro,0,0,0,0,0
Rayan,zagueiro,0,0,0,0,0
Arnaldo,lateral,0,0,0,0,0
Luiz Paulo,lateral,0,0,0,0,0
Marco Antônio,meia,1,0,0,0,0
Patrick Allan,meia,0,1,0,0,0
Igor Pereira,meia,0,0,0,0,0
Vinícius,atacante,1,0,0,0,0
Kelvin,atacante,1,0,0,0,0
Paulo Sérgio,atacante,2,1,0,0,0
reservas
Wellerson,goleiro,0,0,0,0,0
Mateus Silva,zagueiro,0,0,0,0,0
Igor Fernandes,lateral,0,0,0,0,0
Wenderson,meia,0,0,0,0,0
Bruno Mezenga,atacante,0,0,0,0,0
Daniel Paulista
titulares
Caíque França,goleiro,0,0,0,0,1
Chico,zagueiro,0,0,0,0,1
Antônio Carlos,zagueiro,0,0,0,0,1
Hereda,lateral,0,0,0,0,1
Cariús,lateral,0,0,0,0,1
Sérgio Oliveira,meia,0,0,1,0,1
Zé Lucas,meia,0,0,0,0,1
Lucas Lima,meia,0,0,0,0,1
Pablo,atacante,1,0,0,0,1
Barletta,atacante,0,0,0,0,1
Romarinho,atacante,0,0,0,0,1
reservas
Thiago Couto,goleiro,0,0,0,0,1
Rafael Thyere,zagueiro,0,0,0,0,1
Dalbert,lateral,0,0,0,0,1
Du Queiroz,meia,1,0,0,0,1
Atencio,atacante,0,0,0,0,1

Output

Os técnicos que participarão da avaliação da rodada serão Hélio dos Anjos, Daniel Paulista.
Pode cortar Hélio dos Anjos dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...
Daniel Paulista é um gênio da bola mesmo, a substituição de Sérgio Oliveira por Du Queiroz fez ele ganhar pontos!
Hélio dos Anjos é incrível ganhou essa rodada com 75 pontos!
Temos que pedir desculpas a Hélio dos Anjos, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!

Case: 2

Input

2
Hélio dos Anjos
titulares
Muriel,goleiro,0,0,0,0,0
Carlinhos,zagueiro,0,0,0,0,0
Rayan,zagueiro,0,0,0,0,0
Arnaldo,lateral,0,0,0,0,0
Luiz Paulo,lateral,0,0,0,0,0
Marco Antônio,meia,1,0,0,0,0
Patrick Allan,meia,0,1,0,0,0
Igor Pereira,meia,0,0,0,0,0
Kelvin,atacante,0,0,1,0,0
Paulo Sérgio,atacante,1,0,0,0,0
Vinícius,atacante,0,0,0,0,0
reservas
Wellerson,goleiro,0,0,0,0,0
Mateus Silva,zagueiro,0,0,0,0,0
Igor Fernandes,lateral,0,0,0,0,0
Wenderson,meia,0,0,0,0,0
Bruno Mezenga,atacante,1,0,0,0,0
Marcelo Cabo
titulares
Felipe Alves,goleiro,0,0,0,0,1
Eurico,zagueiro,0,0,0,0,1
Matheus Vinicius,zagueiro,0,0,0,0,1
Israel,lateral,0,0,0,0,1
Toty,lateral,0,0,0,0,1
Gabriel Galhardo,meia,0,0,0,0,1
Balotelli,meia,0,0,0,0,1
Willian JR,meia,0,0,0,0,1
Geovany,atacante,1,0,0,0,1
Thiago Galhardo,atacante,0,0,0,0,1
Thiaguinho,atacante,0,0,0,0,1
reservas
Rijebedy,goleiro,0,0,0,0,1
William Alves,zagueiro,0,0,0,0,1
Vinicius Silva,lateral,0,0,0,0,1
Matheus Melo,meia,0,0,0,0,1
João Pedro,atacante,0,0,0,0,1

Output

Os técnicos que participarão da avaliação da rodada serão Hélio dos Anjos, Marcelo Cabo.
Hélio dos Anjos é um gênio da bola mesmo, a substituição de Kelvin por Bruno Mezenga fez ele ganhar pontos!
Pode cortar Marcelo Cabo dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...
Hélio dos Anjos é incrível ganhou essa rodada com 54 pontos!