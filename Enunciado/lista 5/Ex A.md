Matheus Stepple, conhecido nos corredores do CIn não apenas por sua habilidade em programação, mas também como um grande jogador de jogos soulslike, decide finalmente se aventurar pelo Japão feudal de Sekiro. Porém, no topo do Castelo de Ashina. Ele encontra seu primeiro grande rival, Genichiro.

Após uma batalha intensa e exaustiva, Stepple é derrotado – um evento que, para a progressão normal da história do jogo, é inevitável e esperado.

Sekiro

Mas para ele, um veterano de batalhas implacáveis, ser forçado a perder pelo roteiro é inaceitável. Chateado com a derrota "obrigatória", ele decide que não vai seguir o script. Ele quer vencer.

Para isso, Stepple convoca os talentosos estudantes de Introdução a Programação para uma missão de honra.

Sekiro2

Sua tarefa é criar para Stepple um simulador de combate perfeito. Um programa em Python onde ele possa testar exaustivamente cada ação e reação, cada técnica e contra-ataque, para finalmente encontrar uma maneira de quebrar o roteiro e vencer a luta.
As Regras do Combate:

Para que o simulador seja útil, ele precisa ser uma réplica fiel da batalha. Stepple já analisou e anotou todas as regras. Que são:
1. Os Combatentes:

Os status (atributos) de cada guerreiro serão gerenciados usando esses status:

    Sekiro (Lobo): Vitalidade: 100, Postura: 0, Postura máxima: 100, Cabaças curativas: 2;
    Genichiro: Vitalidade: 100, Postura: 0, Postura máxima: 100;

2. Arsenal de Ações:

    Ações de Sekiro: ataque, defesa, defesa perfeita, usar cabaça, desviar, contra ataque mikiri.
    Ações de Genichiro: ataque, defesa, recuperação de postura, ataque kanji.

3. A Simulação:

    O combate é interativo e por turnos. A cada turno, você escolherá a ação de Genichiro primeiro, e depois a ação de resposta do Lobo.
    O duelo deve continuar até que um dos combatentes seja definitivamente derrotado (Vitalidade chegando a 0 ou a postura chegando a 100).

4. As Interações de Lâminas:

O resultado de cada turno é definido pelas regras de dano à Vitalidade (Vit) e à Postura (Pos), que estão descritas no Output.
ATENÇÃO:

Você precisa criar uma função recursiva para a batalha entre turnos.

Input

O programa espera receber os dados na seguinte ordem, repetidamente a cada turno, para que a lógica funcione corretamente:

Ação de Genichiro:

    Ação (str)

Ação de Sekiro (o Lobo):

    Ação (str)

Após a entrada da ação de Genichiro, o programa espera a ação do lobo para continuar o turno

Output
🐺⚔️ Regras completas do combate — Simulação Sekiro x Genichiro

O programa deve iniciar com a seguinte mensagem:

    O duelo começa! Suas decisões determinarão o vencedor.

Em seguida, a cada início de turno, a seguinte mensagem deve ser exibida:

    --- Turno {i} ---

Caso não seja selecionada uma ação válida na entrada de Genichiro ou do Lobo (ações que eles não têm no arsenal), o programa deve printar a seguinte mensagem e continuar esperando uma entrada válida:

    Para Genichiro:

    Genichiro não tem esse movimento em seu arsenal.

    Para Sekiro:

    O lobo não adquiriu esse movimento ainda.

🎴 Ações possíveis

As ações de Genichiro:
ataque, defesa, recuperação de postura, ataque kanji

As ações de Sekiro:
ataque, defesa, defesa perfeita, usar cabaça, desviar, contra ataque mikiri
✅ Casos detalhados
1️⃣ Se Genichiro usa ataque:

    Sekiro responde com ataque:
        Efeito: Sekiro: -25 Vitalidade | Genichiro: -10 Vitalidade, +15 Postura
        Deve printar:

            Clima de tensão! Os dois atacam numa luta implacável!

    Sekiro responde com defesa:
        Efeito: Sekiro: -10 Vitalidade, +20 Postura
        Deve printar:

            Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!

    Sekiro responde com defesa perfeita:
        Efeito: Genichiro: +25 Postura
        Deve printar:

            Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!

    Sekiro responde com usar cabaça:
        Se houver cabaças:
            Efeito: Sekiro: -1 Cabaça, -25 Vitalidade
            Deve printar:

                Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!

        Se não houver cabaças:
            Efeito: Sekiro: -25 Vitalidade
            Deve printar:

                Sekiro busca sua cabaça, mas ela está vazia!

                Enquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!

    Sekiro responde com desviar:
        Efeito: Nenhuma alteração
        Deve printar:

            O lobo desvia agilmente do ataque comum de Genichiro!

    Sekiro responde com contra ataque mikiri:
        Efeito: Genichiro: +10 Postura
        Deve printar:

            O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.

2️⃣ Se Genichiro usa defesa:

    Sekiro responde com ataque:
        Efeito: Genichiro: +5 Postura
        Deve printar:

            Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!

    Sekiro responde com defesa:
        Efeito: Nenhuma alteração
        Deve printar:

            Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.

    Sekiro responde com defesa perfeita:
        Efeito: Nenhuma alteração
        Deve printar:

            Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.

    Sekiro responde com usar cabaça:
        Se houver cabaças:
            Efeito: Sekiro: +25 Vitalidade, -1 Cabaça
            Deve printar:

                Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.

        Se não houver cabaças:
            Efeito: Nenhuma alteração
            Deve printar:

                Sekiro busca sua cabaça, mas ela está vazia!

                Genichiro mantém a guarda, enquanto o lobo percebe seu erro.

    Sekiro responde com desviar:
        Efeito: Nenhuma alteração
        Deve printar:

            O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.

    Sekiro responde com contra ataque mikiri:
        Efeito: Nenhuma alteração
        Deve printar:

            O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.

3️⃣ Se Genichiro usa recuperação de postura:

    Sekiro responde com ataque:
        Efeito: Genichiro: -10 Vitalidade, +15 Postura (postura não é recuperada)
        Deve printar:

            Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!

    Sekiro responde com defesa:
        Efeito: Postura de Genichiro zerada
        Deve printar:

            Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.

            Genichiro consegue recuperar sua postura, cuidado lobo!

    Sekiro responde com defesa perfeita:
        Efeito: Postura de Genichiro zerada
        Deve printar:

            Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.

            Genichiro consegue recuperar sua postura, cuidado lobo!

    Sekiro responde com usar cabaça:
        Se houver cabaças:
            Efeito: Sekiro: +25 Vitalidade, -1 Cabaça | Genichiro: postura zerada
            Deve printar:

                Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.

                Genichiro consegue recuperar sua postura, cuidado lobo!

        Se não houver cabaças:
            Efeito: Genichiro: postura zerada
            Deve printar:

                Sekiro busca sua cabaça, mas ela está vazia!

                Genichiro aproveita a hesitação do lobo para recuperar sua postura.

                Genichiro consegue recuperar sua postura, cuidado lobo!

    Sekiro responde com desviar:
        Efeito: Postura de Genichiro zerada
        Deve printar:

            O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.

            Genichiro consegue recuperar sua postura, cuidado lobo!

    Sekiro responde com contra ataque mikiri:
        Efeito: Postura de Genichiro zerada
        Deve printar:

            O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.

            Genichiro consegue recuperar sua postura, cuidado lobo!

4️⃣ Se Genichiro usa ataque kanji:

    Sekiro responde com contra ataque mikiri:
        Efeito: Genichiro: +25 Postura
        Deve printar:

            O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!

    Sekiro responde com desviar:
        Efeito: Nenhuma alteração
        Deve printar:

            O lobo desvia do ataque especial de Genichiro com muita agilidade!

    Sekiro responde com usar cabaça:
        Se houver cabaças:
            Efeito: Sekiro: -1 Cabaça, -50 Vitalidade, +20 Postura
            Deve printar:

                O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!

        Se não houver cabaças:
            Efeito: Sekiro: -50 Vitalidade, +20 Postura
            Deve printar:

                O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!

                Para piorar, Sekiro nem sequer tinha uma cabaça para usar!

    Sekiro responde com qualquer outra ação:
        Efeito: Sekiro: -50 Vitalidade, +20 Postura
        Deve printar:

            O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!

🏆 Casos especiais
✅ Caso 1: Sekiro derrota Genichiro

Se Genichiro ficar vulnerável:

    Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!

Sekiro pode escolher:

    ataque:

        Sekiro executa um Golpe Mortal em Genichiro!

        ====================================

        Vitória de Sekiro: Golpe Mortal!

    hesitar:

        O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!

E Genichiro recupera status conforme descrito.

    Se Genichiro ficou vulnerável porque teve a postura quebrada:
        Genichiro recupera +50 de postura.
        Se a Vitalidade dele estava abaixo de 50, ele recupera até chegar a 50.
        (Ex.: estava com 30 → vai para 50).
        Se já tinha 50 ou mais, mantém o valor.
    Se Genichiro ficou vulnerável porque a Vitalidade chegou a 0:
        Genichiro recupera +50 de vitalidade.
        Fica com 50 de postura, independentemente do valor que tinha antes.

❌ Caso 2: Genichiro derrota Sekiro

Se Vitalidade de Sekiro chegar a 0:

    Sekiro cai de joelhos, derrotado...

    ====================================

    Vitória de Genichiro: Morte.

Se a Postura de Sekiro for quebrada:

    A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!

    ====================================

    Vitória de Genichiro: Morte.

Obs: Não existem casos de empate.

Examples

Case: 1

Input

ataque
ataque
ataque
defesa perfeita
ataque
defesa
ataque kanji
contra ataque mikiri
defesa
ataque
recuperação de postura
ataque
recuperação de postura
usar cabaça
ataque kanji
contra ataque mikiri
ataque
contra ataque mikiri
pulo
ataque kanji
contra ataque mikiri
ataque
defesa perfeita
ataque
defesa perfeita
ataque

Output

O duelo começa! Suas decisões determinarão o vencedor.
--- Turno 1 ---
Clima de tensão! Os dois atacam numa luta implacável!
--- Turno 2 ---
Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!
--- Turno 3 ---
Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!
--- Turno 4 ---
O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!
--- Turno 5 ---
Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!
--- Turno 6 ---
Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!
--- Turno 7 ---
Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.
Genichiro consegue recuperar sua postura, cuidado lobo!
--- Turno 8 ---
O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!
--- Turno 9 ---
O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.
--- Turno 10 ---
Genichiro não tem esse movimento em seu arsenal.
O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!
--- Turno 11 ---
Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!
--- Turno 12 ---
Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!
--- Turno 13 ---
Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!
Sekiro executa um Golpe Mortal em Genichiro!
====================================
Vitória de Sekiro: Golpe Mortal!

Case: 2

Input

ataque
defesa
ataque kanji
defesa
defesa
ataque
ataque kanji
ataque

Output

O duelo começa! Suas decisões determinarão o vencedor.
--- Turno 1 ---
Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!
--- Turno 2 ---
O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!
--- Turno 3 ---
Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!
--- Turno 4 ---
O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!
Sekiro cai de joelhos, derrotado...
====================================
Vitória de Genichiro: Morte.