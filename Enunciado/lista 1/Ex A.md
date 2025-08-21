O nosso querido mascote Byte acaba de chegar aos ambientes do Centro de Informática (CIn). Estamos todos muito felizes com a sua chegada, que deve entrar para a história, pois já sabemos que ele é o melhor mascote que já existiu!

Sua tarefa é criar um programa em Python que simule as interações básicas com Byte, considerando se ele está com fome ou não. O programa deve:

    Perguntar se Byte está com fome e agir de acordo com a resposta.
    Se ele estiver com fome, perguntar o que ele vai comer e responder adequadamente.
    Se ele não estiver com fome, verificar se está chovendo para decidir se ele pode passear.

    OBS_1: as únicas comidas que Byte gosta são: carne, ração e petisco;
    OBS_2: todos os input devem utilizar caracteres minúsculos

Input

Você receberá uma única string indicando se Byte está com fome ou não (OBS: só é permitido "sim" ou "não", com caracteres em minúsculo).

    fome

Se ele estiver com fome, o próximo input deverá indicar uma comida e encerrar o programa:

    comida

Caso Byte não esteja com fome, irá considerar dar um passeio, por isso, haverá mais um input indicando se está chovendo ou não (também só é permitido receber "sim" ou "não", com caracteres em minúsculo).

    chovendo

Output

A primeira saída deve ser:

    "O Byte está com fome?"

A resposta recebida deve ser sim ou não, caso haja uma outra resposta, seu programa deverá imprimir a seguinte frase:

    "Insira uma resposta válida"

E o programa encerra.

Se ele estiver com fome, você deve retornar:

    "O que você vai dar para ele comer?"

De acordo com sua resposta, se for uma comida que ele gosta (carne, ração ou petisco), você deve retornar:

    "Byte comeu {comida} e está feliz!"

Em seguida, imprima a seguinte frase e encerre o programa:

    "Depois desse banquete, Byte pode tirar um cochilo feliz"

De acordo com sua resposta, se for uma comida que ele não gosta, você deve retornar:

    "Byte não gosta de {comida}"

Em seguida, imprima a seguinte frase e encerre o programa:

    "Byte se irritou e foi dormir pra ver se sonha com suas refeições prediletas..."

Porém, se Byte não estiver com fome, a saída deve ser:

    "Já que Byte não está com fome, ele pode passear"

    "Está chovendo?"

Se estiver chovendo, imprima:

    "Já que está chovendo, Byte vai ter que brincar em casa"

E se não estiver chovendo retorne: "Byte está indo passear"

A resposta recebida deve ser sim ou não, caso haja uma outra resposta, seu programa deverá imprimir a seguinte frase:

    "Insira uma resposta válida"

Examples

Case: 1

Input

sim
carne

Output

O Byte está com fome?
O que você vai dar para ele comer?
Byte comeu carne e está feliz!
Depois desse banquete, Byte pode tirar um cochilo feliz

Case: 2

Input

não
sim

Output

O Byte está com fome?
Já que Byte não está com fome, ele pode passear
Está chovendo?
Já que está chovendo, Byte vai ter que brincar em casa