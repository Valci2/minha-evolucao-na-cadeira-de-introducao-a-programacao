Em Satan City, o céu começa a escurecer e um buraco aparece entre as nuvens. Goku sente uma energia sinistra vindo dele.

Esse buraco é, na verdade, um portal para o Submundo criado por Dr. Myuu, Dr. Gero e Androide 17, com a intenção de transportar um exército de vilões do Submundo para a Terra, e destruir o planeta!

Para parar os vilões, nossos heróis decidiram utilizar o recurso da Fusão, que pode ser feita através da Dança Metamoru. Mas não será tão simples assim, pois para o choque dos heróis, os vilões estão dispostos a deixar o ego de lado e se fundirem também!

Para realizarmos a Fusão, o programa receberá duas strings, dentre os personagens listados abaixo:

herois = [
    'Gohan',
    'Goku',
    'Goten',
    'Kuririn',
    'Piccolo',
    'Tenshinhan',
    'Trunks',
    'Uub',
    'Vegeta',
    'Yamcha'
]

viloes = [
    'Babidi',
    'Baby',
    'Broly',
    'Buu',
    'Cell',
    'Cooler',
    'Frieza',
    'Hit',
    'Janemba',
    'Zamasu'
]

A Fusão será uma junção das duas strings de personagens. Ela segue algumas regras:
PRIMEIRA STRING

-Se a primeira string tiver 4 ou menos caracteres, utilize apenas o primeiro caractere da string para a fusão.

-Se a primeira string tiver mais de 4 caracteres, utilize o resultado da divisão da quantidade de caracteres por 2, e arredonde o número para cima, se for necessário. O valor final será a quantidade de caracteres da primeira string na fusão, de frente pra trás.
SEGUNDA STRING

    Se a segunda string tiver 4 ou menos caracteres, utilize os três últimos caracteres para a fusão. Se o nome tiver 3 caracteres, serão apenas os dois últimos pois não se deve considerar o primeiro.

    Se a segunda string tiver mais de 4 caracteres, utilize o resultado da divisão da quantidade de caracteres por 2, e arredonde o número para cima, se for necessário, e subtraia o resultado por 1. O valor final será a quantidade de caracteres da segunda string na fusão, de trás pra frente.

ESTADO DA FUSÃO

Após concluir a fusão, ela pode ser considerada perfeita ou imperfeita. A fusão será considerada imperfeita se: possuir três ou menos caracteres na string, ou se a última letra da parte da primeira string selecionada para a fusão e a primeira letra da parte da segunda string selecionada para a fusão forem ambas consoantes, ou se forem ambas vogais também.

Por exemplo, uma fusão entre Piccolo e Kuririn será inicialmente imperfeita pois a primera parte termina em uma consoante e a segunda parte começa com uma consoante (Picc + rin)
Se a fusão for imperfeita, você deverá refazer o processo, e modificar os seguintes dois passos:

    Se a primeira string tiver 4 ou menos caracteres, os dois primeiros caracteres da primeira string deverão ser utilizados para a fusão, não só o primeiro.

    Se a primeira string tiver mais de 4 caracteres, adicione +1 ao resultado do arredondamento.

Após refazer pela primeira vez, se a fusão ainda continuar imperfeita, uma tentativa final deve ser feita, continuando com o primeiro passo modificado anteriormente (Se a primeira string tiver 4 ou menos caracteres, os dois primeiros caracteres...), desconsiderando o segundo, e modificando mais dois passos:

    Se a segunda string tiver 4 ou menos caracteres, utilize os três últimos caracteres para a fusão, independente da string ter 3 ou 4 caracteres.

    Se a segunda string tiver mais de 4 caracteres, não subtraia mais o resultado do arredondamento por -1.

Se ainda assim, após as duas tentativas, a fusão continuar imperfeita, ela será incompatível e não deve ser considerada.

OBS1: Um personagem que já está em uma fusão não pode entrar em outra. Então se ele tentar entrar em outra fusão, ela não será considerada. Contudo, sua mensagem de participação ainda será impressa, seguida da mensagem de invalidação. Isso simula o momento em que o personagem se apresenta, antes de ser rejeitado pela regra.

OBS2: Só é possível fusões de heróis com heróis e vilões com vilões. Caso contrário, a fusão deve ser desconsiderada.

OBS3: Toda fusão seguirá o padrão de começar com a letra maiúscula e o restante ser minúscula.
CASOS ESPECIAIS

As duplas Goku e Vegeta, e Goten e Trunks, já são experientes com a Dança Metamoru e têm fusões perfeitas. Se for uma fusão entre Goku e Vegeta, o nome dela deve ser obrigatoriamente Vegito, e se for uma fusão entre Goten e Trunks, o nome dela deve ser obrigatoriamente Gotenks. Esses casos acontecem independente da ordem das strings.

RESULTADOS

O resultado do confronto será decidido pela combinação dos poderes de cada lado. O poder de cada fusão é definido pela quantidade de caracteres de seu nome, de acordo tabela abaixo:

caracteres     |  poder
--------------------------
4              | 2000
5              | 2250
6              | 2500
7              | 2750
8 ou mais      | 3000

Caso algum lado acumule mais de 8000 de poder, ele será considerado vitorioso e o programa encerrará.

IMPORTANTE: (VOCÊ DEVE UTILIZAR FUNÇÕES PARA A FUSÃO E O INCREMENTO DE PODER)

DICA: É possível retornar mais de um valor em uma função, porém, você deve armazenar esses valores em variáveis distintas para evitar o uso de tuplas e ter sua questão desconsiderada

Input

Você receberá o nome dos dois personagens que participarão da fusão:

    nome1

    nome2

O programa recebe essas entradas até um lado for declarado o vencedor.

Output

Para cada nome recebido, printe:

    "{personagem} se elege para participar da fusão!"

Se for uma fusão com uma personagem que já está fundido, printe apenas a seguinte mensagem para cada personagem repetido e receba dois novos nomes para a fusão:

    "{personagem} já participou de uma fusão. Fusão inválida."

Se uma fusão for considerada imperfeita, printe:

    "A sincronização foi um desastre... {fusao} é uma fusão imperfeita!"

Se for uma fusão entre um herói e um vilão, printe:

    "Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis."

Se for uma fusão entre heróis perfeita, printe:

    "Fusão realizada com sucesso! {fusao} entra em combate para derrotar o exército de vilões!"

Se for uma fusão entre vilões perfeita, printe:

    "Fusão realizada com sucesso! {fusao} entra em combate com sede de destruir Satan City!"

Se a fusão falhar depois de várias tentativas e for considerada incompatível, printe:

    "Aparentemente essa combinação é incompatível..."

Se o poder acumulado dos heróis ultrapassar 8000, printe:

    "O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal."

Se o poder acumulado dos vilões ultrapassar 8000, printe:

    "Os vilões são fortes demais! Satan City está em apuros!"

OBS: Não existem casos que o poder acumulado dos heróis e dos vilões ultrapassam 8000 ao mesmo tempo.

Examples

Case: 1

Input

Yamcha
Gohan
Cell
Frieza
Trunks
Goten
Piccolo
Kuririn
Goku
Uub
Goku
Tenshinhan

Output

Yamcha se elege para participar da fusão!
Gohan se elege para participar da fusão!
Fusão realizada com sucesso! Yaman entra em combate para derrotar o exército de vilões!
Cell se elege para participar da fusão!
Frieza se elege para participar da fusão!
A sincronização foi um desastre... Cza é uma fusão imperfeita!
Fusão realizada com sucesso! Ceza entra em combate com sede de destruir Satan City!
Trunks se elege para participar da fusão!
Goten se elege para participar da fusão!
Fusão realizada com sucesso! Gotenks entra em combate para derrotar o exército de vilões!
Piccolo se elege para participar da fusão!
Kuririn se elege para participar da fusão!
A sincronização foi um desastre... Piccrin é uma fusão imperfeita!
Fusão realizada com sucesso! Piccorin entra em combate para derrotar o exército de vilões!
Goku se elege para participar da fusão!
Uub se elege para participar da fusão!
A sincronização foi um desastre... Gub é uma fusão imperfeita!
A sincronização foi um desastre... Goub é uma fusão imperfeita!
A sincronização foi um desastre... Gouub é uma fusão imperfeita!
Aparentemente essa combinação é incompatível...
Goku se elege para participar da fusão!
Tenshinhan se elege para participar da fusão!
A sincronização foi um desastre... Gnhan é uma fusão imperfeita!
Fusão realizada com sucesso! Gonhan entra em combate para derrotar o exército de vilões!
O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.

Case: 2

Input

Hit
Janemba
Yamcha
Trunks
Babidi
Baby
Trunks
Tenshinhan
Trunks
Kuririn
Cooler
Broly
Buu
Frieza

Output

Hit se elege para participar da fusão!
Janemba se elege para participar da fusão!
A sincronização foi um desastre... Hmba é uma fusão imperfeita!
Fusão realizada com sucesso! Himba entra em combate com sede de destruir Satan City!
Yamcha se elege para participar da fusão!
Trunks se elege para participar da fusão!
A sincronização foi um desastre... Yamks é uma fusão imperfeita!
A sincronização foi um desastre... Yamcks é uma fusão imperfeita!
A sincronização foi um desastre... Yamnks é uma fusão imperfeita!
Aparentemente essa combinação é incompatível...
Babidi se elege para participar da fusão!
Baby se elege para participar da fusão!
Fusão realizada com sucesso! Bababy entra em combate com sede de destruir Satan City!
Trunks se elege para participar da fusão!
Tenshinhan se elege para participar da fusão!
Fusão realizada com sucesso! Trunhan entra em combate para derrotar o exército de vilões!
Trunks se elege para participar da fusão!
Kuririn se elege para participar da fusão!
Trunks já participou de uma fusão. Fusão inválida.
Cooler se elege para participar da fusão!
Broly se elege para participar da fusão!
Fusão realizada com sucesso! Cooly entra em combate com sede de destruir Satan City!
Buu se elege para participar da fusão!
Frieza se elege para participar da fusão!
A sincronização foi um desastre... Bza é uma fusão imperfeita!
Fusão realizada com sucesso! Buza entra em combate com sede de destruir Satan City!
Os vilões são fortes demais! Satan City está em apuros!