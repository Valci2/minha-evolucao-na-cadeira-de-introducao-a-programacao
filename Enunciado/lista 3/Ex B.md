No universo de Solo Leveling, portais surgiram misteriosamente ligando o mundo real a dungeons cheias de monstros. Para combatê-los, humanos despertaram poderes e passaram a ser chamados de caçadores.

Sung Jin-Woo era conhecido como o caçador mais fraco de todos, um rank E que mal conseguia sobreviver em missões simples. Mas tudo muda quando ele é escolhido por um sistema misterioso, que lhe dá a chance de crescer sozinho, ficando mais forte a cada batalha — e adquirindo uma habilidade única: reviver inimigos como sombras leais ao seu comando.

Durante uma de suas explorações em dungeons, ainda de nível baixo, Jin-Woo recebe a oportunidade de testar sua força contra criaturas aleatórias. Porém, ele sabe que qualquer erro poderá ser fatal.

Cada criatura enfrentada pode ser adicionada ao Exército das Sombras, caso seja derrotada. Se for mais forte ou do mesmo nível que Jin-Woo, o caçador será imediatamente aniquilado. O exército só cresce com cautela… e com inteligência!

E cabe a você, aluno do CIn, ser operador(a) do sistema de rastreamento da Associação de Caçadores. Sua missão é simular essa caçada com base em uma sequência de criaturas, controlando o nível de Jin-Woo e construindo (ou não) seu exército.

Sua simulação deve considerar:

    O nível inicial de Jin-Woo.
    A quantidade de criaturas enfrentadas.
    O nome e o nível de cada criatura.
    Se derrotada, Jin-Woo pode escolher adicioná-la ao seu exército.
    Caso o nível da criatura seja igual ou superior ao dele, a caçada termina imediatamente.

Input

Seu programa deve ler, nesta ordem:

1.Um número inteiro n_jinwoo, representando o nível inicial de Jin-Woo.

    n_jinwoo (inteiro)

2.Um número inteiro qtd, representando o número de criaturas a enfrentar.

    qtd (inteiro)

3.Para cada criatura:

Uma string nome, o nome da criatura:

    nome_criatura (string)

Um inteiro nivel, o nível da criatura.

    nivel_criatura (inteiro)

Se Jin-Woo venceu, leia uma resposta Erga-se ou Deixar, indicando respectivamente se ele deseja adicioná-la ao exército ou não.

    resposta (string)

Observações

    Toda criatura adicionada ao exército aumenta o nível de Jin-Woo em nivel_da_criatura // 3.
    Mesmo se Jin-Woo derrotar uma criatura, ele pode escolher não adicioná-la.
    Se ele morrer, o programa para imediatamente a leitura de criaturas.
    Cada criatura pode ser adicionada mais de uma vez ao exército, e isso deve ser contabilizado corretamente.

Output

Após o fim da caçada (por derrota ou por fim da lista), seu programa deve imprimir:

Caso Jin-Woo tenha sido aniquilado: Imprima uma linha com a mensagem:

    Jin-Woo foi derrotado por <nome_da_criatura>...

em que <nome_da_criatura> é o nome da criatura que causou sua derrota.

Caso Jin-Woo tenha sobrevivido a todas as criaturas, imprima:

    Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!

Em seguida, sempre imprima:

    ===== Exército das Sombras de Jin-Woo =====

Se o exército estiver vazio:

    Jin-Woo não conseguiu formar seu exército...

Caso contrário, para cada criatura no exército:

    <nome_da_criatura>: <quantidade_captura>

em que <nome_da_criatura> é o nome da criatura que foi capturada e <quantidade_captura> é a quantidade de vezes em que a criatura foi capturada

Examples

Case: 1

Input

10
5
Igris
4
Erga-se
Arqueiros
2
Deixar
Magos
3
Erga-se
Assassinos
1
Erga-se
Magos
2
Erga-se

Output

Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!
===== Exército das Sombras de Jin-Woo =====
Igris: 1
Magos: 2
Assassinos: 1

Case: 2

Input

10
1
Cavaleiros
20

Output

Jin-Woo foi derrotado por Cavaleiros...
===== Exército das Sombras de Jin-Woo =====
Jin-Woo não conseguiu formar seu exército...