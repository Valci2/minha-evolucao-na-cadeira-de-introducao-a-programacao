Krypto, o Supercão, é um cidadão americano que, por força das circunstâncias, precisou seguir a carreira de combate ao crime e acabou não realizando seu maior sonho: se formar em um curso de tecnologia. Felizmente, apesar dos desafios enfrentados ao longo da jornada, Krypto e seus colegas conseguiram pacificar toda a região que protegem. Foi então que, motivado por esse feito, Krypto decidiu vir ao Brasil, prestar o ENEM e se candidatar à única faculdade das Américas que aceita alunos caninos: o CIn.

Pelo fato de não falar português tão bem e de não ser tão desenrolado quanto os brasileiros, Krypto pediu ajuda ao querido mascote de IP, o Byte, para que ele o auxiliasse a calcular quanto ele precisará gastar mensalmente para alugar, na excelentíssima Avenida General Poly Dog, sua mais nova Fortaleza da Solidão.

Agora, cabe a você, aluno do CIn, ajudar o Byte a criar um programa que o ajude a estimar os gastos de Krypto em sua nova jornada.

Input

O programa deverá receber 5 inputs:

Quantos dólares o Superman irá enviar mensalmente para Krypto

    Valor mensal em dólar (int)

Quanto está valendo o dólar, atualmente, em reais:

    Cotação atual do dólar (float)

Quantos reais Krypto irá gastar com ração mensalmente:

    Gasto mensal (em reais) com ração (int)

Quantos reais Krypto irá gastar com aluguel mensalmente:

    Gasto mensal (em reais) com aluguel (int)

Quantos reais Krypto irá gastar com ônibus mensalmente:

    Gasto mensal (em reais) com ônibus (int)

Output

Primeiramente, o seu programa deverá imprimir, de acordo com os gastos de Krypto:

Caso o valor que o Superman envie para ele seja superior aos seus gastos (em real):

    Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!

Caso o valor que o Superman envie para ele seja igual aos seus gastos (em real):

    Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!

Caso o valor que o Superman envie para ele seja menor aos seus gastos (em real):

    Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!

Em seguida, o programa deverá imprimir:

Se o maior gasto de Krypto for com ração:

    A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!

Se o maior gasto de Krypto for com aluguel:

    Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!

Se o maior gasto de Krypto for com ônibus:

    Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!

Ao final, o programa deve imprimir um relatório:

    MESADA (dólares): {valor_mesada_dolar} dólares

    MESADA (reais): {valor_mesada_real} reais

    MAIOR GASTO: {nome_maior_gasto}

Obs. 1: É PROIBIDO o uso da função max para descobrir qual é o maior gasto.

Obs. 2: Em nenhum caso, os valores de cada gasto serão iguais.

Obs. 3: No relatório, todos os valores devem estar com duas casas decimais.

Obs. 4: No relatório, o nome do maior gasto deve estar com a primeira letra maiúscula.

Obs. 5: Entre cada dado do relatório existe uma quebra de linha.

Examples

Case: 1

Input

470
8
400
300
80

Output

Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!
A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!
MESADA (dólares): 470.00 dólares
MESADA (reais): 3760.00 reais
MAIOR GASTO: Ração