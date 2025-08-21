Em um futuro não muito distante, Byte, cansado das suas incontáveis aventuras como mascote de IP, decidiu tirar férias. Mas não seriam férias comuns: ele queria uma aventura digna de sua reputação!

Inspirado pela fase brilhante do seu time do coração, o glorioso Santa Cruz Futebol Clube, que agora brilha na elite da Série A e sonha com a Libertadores, Byte resolveu realizar um sonho: tornar-se jogador profissional do maior time de futebol do Nordeste.

Byte Tricolor

Começando a sua carreira, ele vai disputar, no máximo, 2 partidas na pré-temporada de treinamento antes de ser oficialmente convocado para o elenco principal.

No entanto, há um detalhe: o seu maior rival, o Sport, pode aparecer entre os times adversários desses jogos-treino. Mas existe uma regra no Estatuto Tricolor: o nome "Sport" nunca pode ser dito corretamente. Assim, ele sempre aparece disfarçado - suas letras “s, p, o, r, t”, em minúsculo, estarão embaralhadas no meio de palavras aleatórias, como um código secreto.

O problema é que a rivalidade é séria, mas tão séria que alguns torcedores do Sport, movidos por inveja da fase iluminada do Santa e da estreia do Byte, planejam sequestrá-lo!

Caso isso aconteça, Byte só poderá escapar vencendo uma temida batalha matemática. Nela, precisará resolver uma expressão matemática e só conseguirá fugir se acertar o resultado. E sempre que Byte consegue escapar dos sequestradores, uma coisa acontece: ele volta imediatamente para casa e abandona a carreira de jogador. Afinal, percebe que talvez o futebol profissional não seja lugar para um cachorro.

Input

Para cada partida, serão recebidas as seguintes informações:

    Nome da cidade onde será realizada a partida (string)

    Nome do time adversário (string)

    Resultado da partida (“VENCEU” ou “perdeu”) (string)

Em partidas marcadas por tentativas de sequestro, o resultado da partida não será nem "VENCEU" nem "perdeu". Será:

    Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida! (string)

Em caso de sequestro, após a mensagem anterior, deve-se receber uma expressão numérica:

    Expressão númerica (de dois números inteiros e com uma das quatro operações: + [adição], - [subtração], * [multiplicação] e / [divisão, nunca por 0]) (string)

Obs. 1: O resultado da expressão numérica deve ser calculado utilizando apenas condicionais e as quatro operações (soma, subtração, multiplicação e divisão).

Obs. 2: Na expressão numérica, haverá apenas 1 operador e 2 operandos. Os operandos serão sempre números inteiros não negativos até 9.

Obs. 3: Quando a expressão numérica for respondida (calculada), Byte conseguirá se livrar do sequestro, o que contará como uma vitória para o seu time.

ATENÇÃO: O uso de qualquer outro assunto ainda não visto na disciplina (laços de repetição, listas, funções, recursão, tuplas e dicionários) está PROIBIDO! Isso inclui também o conceito de índices e indexação de iteráveis (strings, listas, etc.).
Dicas

Pode ser muito útil estudar um pouco sobre Desempacotamento com Strings, um dos tópicos desse material:
CLIQUE AQUI!
.

Além disso, você deve saber reconhecer quando uma string possui uma substring - caso não saiba,
CLIQUE AQUI!

Output

Inicialmente, o programa deve printar uma mensagem que um dos assessores do Byte recolheu da ASCOM do CIn:

    Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!

Para cada partida, quando uma partida for realizada em Catende OU em Tabira:

    É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.

Logo após imprimir a frase acima referente à segunda partida (se houver a segunda partida) e se as duas partidas foram em Catende E em Tabira (ou Tabira e Catende), imprimir:

    Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...

Quando a partida for contra o seu principal rival (identificado atraves da análise do "código secreto"):

    Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!

Quando o Santa Cruz vencer uma partida normal (partida sem tentativa de sequestro):

    TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!

Quando o Santa Cruz perder uma partida normal (partida sem tentativa de sequestro)::

    Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...

Quando houver uma tentativa de sequestro de Byte em uma partida:

    Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!

Em seguida, calcule a expressão numérica informada no input associado ao caso de tentativa de sequestro, e imprima o seu resultado:

    A expressão resolvida é: {x}

Obs.: Note que x é a variável contendo o resultado da operação. Além disso, o resultado mostrado deve SEMPRE exibir somente as duas primeiras casas decimais após a vírgula.

Após vencer a batalha matemática:

    Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!

Sempre imediatamente após o fim de todas as rodadas OU após Byte desistir da sua carreira futebolística, deve-se imprimir um relatório da pré-temporada, após o print de uma linha vazia (apenas para espaçamento):

    RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:

    - Partidas jogadas: w

    - Vitórias: y

    - Derrotas: z

    - Tentaram roubar o bixinho: (”sim :(” ou “Não!!!! :D”)

    - Cidades visitadas: A (ou A e B, se forem duas)

    - Adversários enfrentados: C (ou C e D, se forem duas)

    (linha vazia)

    E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)

Note que w, y e z são números inteiros não negativos, e A, B, C e D são nomes que devem aparecer conforme a necessidade.

Examples

Case: 1

Input

Recife
Náutico
VENCEU
Paulista
Íbis
perdeu

Output

Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!
TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!
Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...

RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:
- Partidas jogadas: 2
- Vitórias: 1
- Derrotas: 1
- Tentaram roubar o bixinho: Não!!!! :D
- Cidades visitadas: Recife e Paulista
- Adversários enfrentados: Náutico e Íbis

E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)

Case: 2

Input

Petrolina
América
VENCEU
Recife
sropteam
Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!
5/2

Output

Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!
TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!
Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!
Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!
A expressão resolvida é: 2.50
Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!

RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:
- Partidas jogadas: 2
- Vitórias: 2
- Derrotas: 0
- Tentaram roubar o bixinho: sim :(
- Cidades visitadas: Petrolina e Recife
- Adversários enfrentados: América e sropteam

E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)

Case: 3

Input

Catende
Leão XIII
VENCEU
Tabira
Tubiba FC
perdeu

Output

Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!
É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.
TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!
É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.
Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...
Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...

RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:
- Partidas jogadas: 2
- Vitórias: 1
- Derrotas: 1
- Tentaram roubar o bixinho: Não!!!! :D
- Cidades visitadas: Catende e Tabira
- Adversários enfrentados: Leão XIII e Tubiba FC

E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)