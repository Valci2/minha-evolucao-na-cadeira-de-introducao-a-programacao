Na série The Flash, após a explosão do Acelerador de Partículas várias ondas de batalha começaram a acontecer entre heróis e vilões. Por isso, a equipe da STAR Labs contratou você, grande programador do Cin, para desenvolver um sistema simples em que cada onda é uma lista contendo os personagens que participaram daquela rodada, na ordem em que apareceram.

Input

Seu programa receberá uma entrada contendo a quantidade N de ondas que vão acontecer.

    N (inteiro)

Para cada onda, você receberá uma sequência de nomes de personagens separados por uma vírgula e um espaço.

    personagem1, personagem2, personagem3, ..., personagemn

    Se o personagem vier na forma V-nome do personagem, o personagem é um vilão.
    Se o personagem vier na forma H-nome do personagem, o personagem é um herói.

Obs: O input sempre terá no mínimo 3 personagens.
Disputa

    Foi combinado com a equipe da STAR Labs que em todas as ondas, o primeiro e o último personagem nunca farão parte da disputa, independente de serem heróis ou vilões.

Dica: faça a utilização de sublista em cada onda.

    O vencedor (heróis ou vilões) de cada onda é dado pela diferença da quantidade de herois e da quantidade vilões.

    diferença = (número de heróis) - (número de vilões)

    Caso a onda tenha diferença negativa, significa que os vilões dominaram aquela onda e eles ganharam um ponto.
    Caso a diferença seja positiva, significa que os heróis venceram aquela onda e ganharam um ponto pro time dos heróis.
    Agora caso a diferença seja igual a zero, nenhum do dois ganham pontos.

Output

No fim da analise de todas as ondas, imprima a onda que teve a maior diferença entre a quantidade de heróis e vilões

    Caso a onda com maior diferença tenha sido vencida pelo heróis:

    🌀Onda {menor_indice} foi a menos acirrada e a mais favorável para os heróis!

    Caso a onda com maior diferença tenha sido vencida pelo vilões:

    🌀Onda {menor_indice} foi a menos acirrada e a mais favorável para os vilões!

    Caso não tenha nenhuma onda com maior diferença (diferenças iguais a 0(zero)):

    🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!

Obs.1: A primeira onda recebida terá o índice 1.

Obs.2: Caso mais de uma onda possua a mesma diferença, printe o índice da menor onda

Após isso, se houver uma onda vencedora, imprima os participantes presentes nessa onda com maior diferença (incluindo o primeiro e o último que não participaram da contagem da disputa), separados por ", ":

    Participantes analisados: {melhor_onda}

Depois de ter a pontuação final, imprima:

    Agora vamos ao resultado geral das ondas...

    Heróis: {quantidade_vitorias_herois} | Vilões: {quantidade_vitorias_viloes}

    Caso a quantidade de vitorias dos heróis seja maior que a dos vilões, printa:

    Ufa, os heróis dominaram! Central City está seguro outra vez

    Caso a quantidade de vitorias dos vilões seja maior que a dos heróis, deve printar:

    Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!

    Caso seja empate, imprima:

    Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço

Examples

Case: 1

Input

3
H-Flash, V-ReverseFlash, H-Vibe, H-KidFlash, V-Zoom
H-Supergirl, V-Grodd, V-KingShark, H-Arrow, V-CaptainCold
V-KillerFrost, V-Ragdoll, V-Bloodwork, H-Firestorm, H-XS

Output

🌀Onda 1 foi a menos acirrada e a mais favorável para os heróis!
Participantes analisados: H-Flash, V-ReverseFlash, H-Vibe, H-KidFlash, V-Zoom
Agora vamos ao resultado geral das ondas...
Heróis: 1 | Vilões: 2
Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!

Case: 2

Input

3
H-Flash, V-Zoom, H-KidFlash, H-Caitlin, V-ReverseFlash
H-Wells, V-Grodd, H-Vibe, H-XS, V-CaptainCold
V-KillerFrost, V-Ragdoll, H-Firestorm, H-ElongatedMan, V-Cicada

Output

🌀Onda 1 foi a menos acirrada e a mais favorável para os heróis!
Participantes analisados: H-Flash, V-Zoom, H-KidFlash, H-Caitlin, V-ReverseFlash
Agora vamos ao resultado geral das ondas...
Heróis: 3 | Vilões: 0
Ufa, os heróis dominaram! Central City está seguro outra vez