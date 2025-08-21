O aniversário de Byte estava chegando e seus amigos humanos e caninos decidiram presenteá-lo com uma nova bolinha de tênis super rara durante a sua festa. Depois de ver a surpresa, o nosso mascote ficou super animado. Ninguém nunca tinha visto um cachorro tão feliz assim.

byte.png

Só que depois de passar a euforia, Byte se encontrou em um gigantesco impasse: qual nome uma bolinha tão especial deveria receber? Ele não conseguia pensar em nada e isso começou a deixá-lo muito preocupado. Seus amigos que estavam na comemoração tentaram ajudar, mas eram tantas sugestões que o pobre cachorro ficou mais confuso ainda…

Por isso você, um brilhante estudante de IP, decidiu ajudá-lo a selecionar o melhor nome possível por meio de um programa que criará um ranking com as três sugestões que os amigos de Byte oferecerem. No entanto, cuidado! Há certos impostores felinos na festa e eles querem sabotar o nome da bolinha do nosso amigo.

Como funcionará a pontuação dos nomes:

-Em hipótese alguma o nome deve ter a palavra “gato” no meio. Se isso acontecer, a pontuação do nome será zerada.

-Byte adora trocadilhos com o CIn, então se o nome de alguma forma tiver a palavra “cin”, adicione mais 10 pontos.

-Outra forma de pontuar é ver o tamanho da palavra. O número de letras deve ser adicionado na pontuação. Como por exemplo: o nome “fofinha” tem 7 letras, logo, na pontuação, seriam adicionados 7 pontos.

-Por fim, deve-se analisar quem está indicando o nome. Se for um “ser humano” ou “cachorro” tudo segue normalmente. Mas se for um “felino espião”, a pontuação do nome deve ser zerada.

OBS: Os nomes devem ter apenas letras minúsculas.

OBS2: Não existirá a possibilidade de empate.

Input

O programa receberá três sugestões de nomes e quem os indicou para organizar a pontuação:

nome_1

quem_indicou_1

nome_2

quem_indicou_2

nome_3

quem_indicou_3

Output

Se algum nome for indicado por um “felino espião”, o programa deve imprimir:

“Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.”

A cada nome que tiver a palavra “cin” e não for indicado por um “felino espião”:

“Os melhores nomes são aqueles que fazem referência a minha casinha :)”

Por fim, imprima o ranking, esse deve ser o último output:

RANKING DOS NOMES:

Primeiro lugar: nome_primeiro_lugar

Segundo lugar: nome_segundo_lugar

Terceiro lugar: nome_terceiro_lugar

Examples

Case: 1

Input

bolinha
cachorro
fofinhazinha
ser humano
doce
cachorro

Output

RANKING DOS NOMES:
Primeiro lugar: fofinhazinha
Segundo lugar: bolinha
Terceiro lugar: doce

Case: 2

Input

gatolino
cachorro
zumbizinha
ser humano
bob
ser humano

Output

RANKING DOS NOMES:
Primeiro lugar: zumbizinha
Segundo lugar: bob
Terceiro lugar: gatolino

Case: 3

Input

cininho
ser humano
gosmenta
felino espião
laika estrelinda
cachorro

Output

Os melhores nomes são aqueles que fazem referência a minha casinha :)
Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.
RANKING DOS NOMES:
Primeiro lugar: cininho
Segundo lugar: laika estrelinda
Terceiro lugar: gosmenta