Na cozinha do Sítio do Pica-Pau Amarelo, Dona Benta está preparando um delicioso bolo de chocolate para o aniversário de sua neta Narizinho. No entanto, em mais uma de suas travessuras, Saci Pererê escondeu os óculos da dedicada vovó. Sem eles, ela não consegue enxergar a receita direito, nem os rótulos dos produtos presentes na cozinha. Para não arriscar, ela decide criar uma lista de compras do zero.

Mas calma, Dona Benta, a senhora não está sozinha nessa missão! O time de alunos de Introdução à Programação (IP) se prontificou a ajudar com dedicação e alegria. Eles estão sempre por perto, prontos para criar um sistema para anotar a lista — seja para adicionar um ingrediente básico (variáveis) ou para reorganizar a ordem da lista (condicionais, laços e manipulação de listas). Por isso, você foi convocado para ajudar Dona Benta nessa missão!

A sua tarefa é gerenciar a lista de compras que Dona Benta está criando, aplicando suas instruções e lidando com as travessuras do Saci, que a todo momento tenta confundir a vovó e bagunçar a sua anotação. Você precisará adicionar, remover e reordenar os ingredientes até que a lista esteja perfeita para ir ao mercado.

Input

Você receberá entradas por uma quantidade indeterminada de vezes até que a lista de compras esteja pronta:

Para cada entrada abaixo, realize a respectiva ação associada na lista de compras:

    Anotar ingrediente

Receba como entrada o nome de um ingrediente (string) e o adicione no final da lista de compras.

    Ingrediente Urgente!

Receba como entrada o nome de um ingrediente (string) e o adicione no início da lista, pois Dona Benta se lembrou que este é o item mais importante.

    Saci disse que já tem

Receba como entrada o nome de um ingrediente (string) e o remova da lista. O Saci convenceu a vovó que o item já existe na cozinha (mesmo que seja mentira!).

    Saci trocou a ordem

O Saci soprou a lista e trocou a ordem de dois itens! Receba duas entradas: um índice atual do ingrediente e o novo índice para onde ele foi movido. Troque a posição do ingrediente com o que estiver no novo índice.

    Organizar a lista

Dona Benta pede para organizar melhor. Receba duas entradas, cada uma com o nome de um ingrediente (string), e inverta as posições deles na lista para agrupar itens parecidos.

    Deixar para depois

Dona Benta decide que um ingrediente não é tão essencial. Receba uma entrada contendo o nome de um ingrediente (string) e mova-o para o final da lista.

    Ler a lista para a vovó

Imprima todos os ingredientes da lista de compras, separados por uma vírgula e um espaço.

    E por hoje é só, pessoal!

A lista de compras está pronta! Finaliza o recebimento de entradas e imprime a lista final de ingredientes a serem comprados.

Obs:

    Nunca haverá dois ingredientes com o mesmo nome na lista.
    Sempre que for solicitado para imprimir a lista, a ordem dos ingredientes deve ser respeitada.
    Não existem casos em que não seja possível realizar a operação fornecida.

Output

    Caso a entrada seja Ler a lista para a vovó, você deve imprimir a lista de compras da seguinte forma:

    ingrediente1, ingrediente2, ingrediente3, ..., ingredienteN

    Caso a entrada seja E por hoje é só, pessoal!, imprima a frase abaixo e em seguida encerre o programa:

    Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: ingrediente1, ingrediente2, ingrediente3, ..., ingredienteN

ATENÇÃO: Em ambos os casos, é preciso imprimir os nomes de todos os ingredientes separados por uma vírgula e um espaço em branco, seguindo a ordem da lista.

Examples

Case: 1

Input

Anotar ingrediente
Farinha de Trigo
Anotar ingrediente
Ovos
Ler a lista para a vovó
Anotar ingrediente
Leite
E por hoje é só, pessoal!

Output

Farinha de Trigo, Ovos
Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: Farinha de Trigo, Ovos, Leite

Case: 2

Input

Anotar ingrediente
Açúcar
Anotar ingrediente
Manteiga
Ingrediente Urgente!
Chocolate em Pó
E por hoje é só, pessoal!

Output

Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: Chocolate em Pó, Açúcar, Manteiga