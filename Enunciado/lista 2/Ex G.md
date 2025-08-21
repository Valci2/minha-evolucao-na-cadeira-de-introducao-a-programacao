O jovem Lavoi é uma lenda em ascensão no circuito mundial de tênis de mesa. Conhecido por seus saques imprevisíveis e sua mente matemática, ele foi convidado para o Torneio Fatorial da Tabuada de Mesa, uma competição nada convencional, onde as partidas são decididas por... cálculos matemáticos de tabuada fatorial!

Pingue-Pongue

O mestre do torneio, um ancião chamado Joabu, lançou o seguinte desafio:

    "Lavoi, para provar que és digno de enfrentar os maiores atletas da Federação dos Pongueiros Sagrados, deves calcular uma série de valores fatoriais baseados em tua energia interior. Escolhe com sabedoria o início e o fim de tua jornada, bem como o número sagrado que carregas. A cada passo, deverás multiplicar esse número sagrado pelo estágio em que te encontras... e então calcular o fatorial do resultado obtido."

Pingue-Pongue-de-gatos
🧠 Traduzindo a missão em etapas:

    Lavoi deve escolher um número inicial que representa o primeiro estágio do torneio.

Esse número não pode ser negativo, pois ninguém começa um campeonato andando para trás!

    Em seguida, ele escolhe um número final que indica o último estágio do torneio.

Esse número não pode ser menor que o número inicial, pois ele deve seguir o fluxo natural da competição.

    Além disso, ele define seu número sagrado, que representa a sua energia vital nas partidas.

Esse número também não pode ser negativo, afinal, energia negativa é proibida pelos Pongueiros Sagrados.

Por fim, para cada estágio (incluindo o início e o fim), Lavoi deve:

    Multiplicar o número do estágio pelo número sagrado.
    Calcular o fatorial do valor resultante da multiplicação.
    Exibir o resultado no formato:

    ({estágio} * {número_sagrado})! = {fatorial}

Input

O programa deve receber três valores, um por vez, respeitando a seguinte ordem:

    O INÍCIO da tabuada fatorial (int)

    O FIM da tabuada fatorial (int)

    O NÚMERO SAGRADO (int)

Obs. 1: O programa deve validar cada um desses números e, caso alguma entrada não seja válida, deve solicitar novamente o valor, informando a devida mensagem de erro.

Obs. 2: Lembre-se que nenhuma informação pode ser um inteiro negativo. Além disso, o número que representa o FIM da tabuada fatorial não pode ser menor que o início.

Output

Ao iniciar o programa, as seguintes frases introdutórias devem ser impressas:

    🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓

    Hoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!

Obs.: Antes de imprimir a segunda frase, faça uma quebra de linha. Após imprimir a segunda frase, pule uma linha (faça um print vazio).

Em seguida, o programa deve pedir para que Lavoi informe o número de início da jornada fatorial:

    Qual será o número que marcará o INÍCIO dessa tabuada fatorial?

Se o número digitado for maior ou igual a zero, o programa deve imprimir:

    O número {numero_inicio} é ótimo como número inicial!

Caso contrário, deve imprimir:

    O número {numero_inicio} é inválido! O INÍCIO NÃO pode ser NEGATIVO.

O programa continuará solicitando esse número. A partir de segunda solicitação, não precisa mais exibir a pergunta "Qual será o número que marcará o INÍCIO dessa tabuada fatorial?". A solicitação repete-se até que uma entrada válida seja fornecida.

Após um número válido ser inserido, pule uma linha (faça um print vazio), independente se foi uma entrada válida de primeira ou se foi uma entrada válida após múltiplas tentativas.

Depois disso, o programa deve perguntar:

    Qual será o número que marcará o FIM dessa tabuada fatorial?

Se o número digitado for maior ou igual ao valor de início, o programa imprime:

    O número {numero_fim} é ótimo como número final!

Caso contrário, imprime:

    O número {numero_fim} é inválido! O FIM NÃO pode ser MENOR que o número inicial {numero_inicio}.

Esse valor também será solicitado repetidamente até que uma entrada válida seja fornecida. Após um número válido ser inserido, pule uma linha (faça um print vazio).

Em seguida, o programa deve perguntar:

    Qual será o número cujo FATORIAL será calculado?

Se o número digitado for maior ou igual a zero, imprime:

    O número {numero_sagrado} é ótimo para o cálculo do fatorial!

Caso contrário, imprime:

    O número {numero_sagrado} é inválido! Números válidos são maiores ou iguais a zero.

Novamente, a entrada é repetida até ser válida. Após um número válido ser inserido, pule uma linha (faça um print vazio).

Para cada número no intervalo de inicio até fim, o programa irá calcular:

1 - O valor do produto entre o número atual e o numero_sagrado.

2 - O fatorial desse valor.

E imprimirá o resultado no seguinte formato:

    ({estágio} * {número_sagrado})! = {fatorial}

Exemplo:

(Início = 1; Fim = 3; Número Sagrado = 2):

    (1 * 2)! = 2

    (2 * 2)! = 24

    (3 * 2)! = 720

Após exibir todos os cálculos, pule uma linha (faça um print vazio) e imprima:

    🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!

    🏓 Que sua energia vital continue brilhando nas próximas batalhas!

Examples

Case: 1

Input

1
3
2

Output

🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓
Hoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!

Qual será o número que marcará o INÍCIO dessa tabuada fatorial?
O número 1 é ótimo como número inicial!

Qual será o número que marcará o FIM dessa tabuada fatorial?
O número 3 é ótimo como número final!

Qual será o número cujo FATORIAL será calculado?
O número 2 é ótimo para o cálculo do fatorial!

(1 * 2)! = 2
(2 * 2)! = 24
(3 * 2)! = 720

🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!
🏓 Que sua energia vital continue brilhando nas próximas batalhas!

Case: 2

Input

-5
-7
2
4
3

Output

🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓
Hoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!

Qual será o número que marcará o INÍCIO dessa tabuada fatorial?
O número -5 é inválido! O INÍCIO NÃO pode ser NEGATIVO.
O número -7 é inválido! O INÍCIO NÃO pode ser NEGATIVO.
O número 2 é ótimo como número inicial!

Qual será o número que marcará o FIM dessa tabuada fatorial?
O número 4 é ótimo como número final!

Qual será o número cujo FATORIAL será calculado?
O número 3 é ótimo para o cálculo do fatorial!

(2 * 3)! = 720
(3 * 3)! = 362880
(4 * 3)! = 479001600

🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!
🏓 Que sua energia vital continue brilhando nas próximas batalhas!

Case: 3

Input

3
-3
-2
6
3

Output

🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓
Hoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!

Qual será o número que marcará o INÍCIO dessa tabuada fatorial?
O número 3 é ótimo como número inicial!

Qual será o número que marcará o FIM dessa tabuada fatorial?
O número -3 é inválido! O FIM NÃO pode ser MENOR que o número inicial 3.
O número -2 é inválido! O FIM NÃO pode ser MENOR que o número inicial 3.
O número 6 é ótimo como número final!

Qual será o número cujo FATORIAL será calculado?
O número 3 é ótimo para o cálculo do fatorial!

(3 * 3)! = 362880
(4 * 3)! = 479001600
(5 * 3)! = 1307674368000
(6 * 3)! = 6402373705728000

🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!
🏓 Que sua energia vital continue brilhando nas próximas batalhas!