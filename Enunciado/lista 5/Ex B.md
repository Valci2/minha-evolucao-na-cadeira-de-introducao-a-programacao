Você está prestes a embarcar em uma jornada épica por Lordran, enfrentando alguns dos chefes mais lendários da franquia Dark Souls. Sua missão é desenvolver um sistema de batalha que conte quantas tentativas o jogador precisou para vencer o chefe, levando em conta a experiência do jogador, seus atributos e as características únicas de cada chefe.
🎮 Contexto

O seu código deve incluir os 2 possíveis chefes (cada Test Case contém somente um chefe):
🐺 Sif, a Grande Loba Cinzenta

Sif, a Grande Loba era parceira do Andarilho do Abismo, Artorias, até que o mesmo foi engolido pelo Abismo. Após isso, Sif, guardou o túmulo de seu companheiro caído, para garantir que mais ningúem sofra o mesmo destino de Artorias. ;-;

    Vida: 3432

    DPS: 35

    Quando sua vida fica abaixo de 10% da vida inicial, Sif é considerada gravemente ferida.

    Ao ser ferida, o DPS da Loba é reduzido em 15 pontos e uma mensagem é exibida: "Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!"

sif
🔥 Gwyn, Lorde das Cinzas

Gwyn é o último chefe em Dark Souls! Foi um guerreiro poderosíssimo e formidável, o maior dentre os Lordes. Conhecido como o Senhor da Luz Solar, ele desempenhou um papel crucial no fim da Era dos Anciões!

    Vida: 4185

    DPS: 55

    Quando sua vida cai para 50% ou menos, ele entra no estado de chamas!

    Ou seja, a partir do momento em que Gwyn entra nesse estado, o jogador perde 10 pontos ADICIONAIS de vida por turno até o fim da batalha!

gwyn
📈 Sistema de Progressão

O jogador pode estar em um dos seguintes níveis de experiência:

    Iniciante

    Veterano

    Mestre do Souls

Se o jogador morrer, ele recomeça a batalha com os seguintes ajustes:

Experiência: Aumento no DPS (atual) do jogador / Redução no DPS (atual) do chefe

Iniciante: +5% -10%

Veterano: +10% -20%

Mestre do Souls: +20% -33%

OBS: É obrigatório o uso de recursão para simulação dessas batalhas.

Input
🔁 Batalha

Experiência do jogador (string):

    Iniciante, Veterano, ou Mestre do Souls

Stats do jogador (2 inteiros separados por um espaço entre eles):

    Vitalidade Força

    Exemplo: 20 20

Nome do chefe a ser enfrentado (string):

    Sif, a Grande Loba Cinzenta

    Gwyn, Lorde das Cinzas

A vida inicial do jogador é:

    Vitalidade * 20

O DPS inicial do jogador é:

    Força * 5

O combate acontece turno a turno:

O jogador SEMPRE ataca primeiro.

Se o chefe ainda estiver vivo, ele revida.

Output
⚔️ Saída Inicial
Inicialmente você deve printar uma mensagem de acordo com o chefe que foi enfrentado:
Sif, a Grande Loba Cinzenta:

    Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!

Gwyn, Lorde das Cinzas:

    Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!

🏁 Saída Final
Ao fim da batalha (quando o chefe for derrotado), o programa deve imprimir:

    Você precisou de {tentativas} tentativas para vencer o(a) {chefe}!

Mensagem de acordo com a experiência e tentativas necessárias pra vencer o boss:
Tentativas | Mensagem
Iniciante:

    Tentativas ≤ 5: Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!

    5 < Tentativas ≤ 10: Até que não foi tão ruim assim, continue assim novato!

    Tentativas >10: Bem vindo a Dark Souls.

Veterano:

    Tentativas ≤ 5: Você já andou por Lordran antes, não é? Impressionante.

    5 < Tentativas ≤ 10: Nada mal, guerreiro. Mas os próximos desafios não terão piedade.

    Tentativas >10: Mesmo os veteranos sangram em Dark Souls...

Mestre do Souls:

    Tentativas == 1: Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!

    1 < Tentativas ≤ 10: Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...

    Tentativas >10: Nem mesmo os Mestres escapam ilesos da chama...

Print especial do chefe derrotado:
Sif, a Grande Loba Cinzenta:

    A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.

Gwyn, Lorde das Cinzas:

Ao fim da batalha, sempre printe:

    A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...

Caso seja derrotado de primeira:

    O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...

Caso não:

    Mas o ciclo... o ciclo continua.

Examples

Case: 1

Input

Veterano
20 20
Sif, a Grande Loba Cinzenta

Output

Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!
Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!
Você precisou de 5 tentativas para vencer o(a) Sif, a Grande Loba Cinzenta!
Você já andou por Lordran antes, não é? Impressionante.
A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.

Case: 2

Input

Mestre do Souls
50 50
Gwyn, Lorde das Cinzas

Output

Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!
Você precisou de 1 tentativas para vencer o(a) Gwyn, Lorde das Cinzas!
Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!
A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...
O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...