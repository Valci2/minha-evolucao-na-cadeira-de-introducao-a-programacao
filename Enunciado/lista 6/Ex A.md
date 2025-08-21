📜 Introdução Histórica

No ano de 2002, a Seleção Brasileira protagonizou um dos momentos mais memoráveis do futebol mundial: conquistou seu quinto título da Copa do Mundo, o tão sonhado Penta!
Sob o comando do técnico Luiz Felipe Scolari (Felipão) e com craques como Ronaldo, Ronaldinho, Cafu e Marcos, o Brasil brilhou nos gramados da Ásia e entrou para a história do futebol.

Heróis do Penta - Seleção Brasileira de 2002

Mas imagine agora um cenário alternativo...
🕰️ Viagem no Tempo e Desafio Tecnológico

Você é estudante do Centro de Informática da UFPE (CIn-UFPE) e está participando de um experimento tecnológico da FIFA voltado à preservação digital de dados históricos do futebol.
Durante os testes, um acidente nos servidores provocou uma anomalia: você foi transportado para o ano de 2002, exatamente no dia da final da Copa do Mundo!

Por motivos de segurança, a escalação da Seleção Brasileira foi criptografada digitalmente, e cabe a você recuperar as informações originais antes que a partida comece.
🔐 Processo de Criptografia

Os nomes originais da escalação da Seleção Brasileira foram criptografados através de uma sequência de transformações utilizando um conjunto personalizado de caracteres ASCII.

O processo de criptografia segue estas etapas:

    Converter o nome original em uma lista de caracteres.
    Aplicar um deslocamento (shift) de +3 posições em cada caractere da lista, segundo o conjunto ASCII personalizado.
    Inverter a lista resultante.
    Dividir a lista invertida ao meio em duas partes: primeira metade e segunda metade.
        Se o tamanho da lista for impar, a maior parte será a segunda.
    Aplicar um deslocamento (shift) de -1 posição em cada caractere da segunda metade.
    Concatenar a primeira metade com a segunda metade modificada.
    Juntar os caracteres para formar a string criptografada final.

ascii_chars = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
]

Obs.1: Todos os nomes originais e criptografados usarão apenas caracteres da lista ascii_chars. Não haverá acentos ou outros símbolos. Obs.2: Os deslocamentos na lista são circulares. Ao passar do último caractere ("~"), a contagem continua a partir do primeiro (" "), e o mesmo vale para a direção oposta.

Exemplo de Criptografia para "Ronaldo":

Original: Ronaldo

Shift +3: U r q d o g r

Inverter: r g o d q r U

Dividir (7 chars -> 3 e 4): rgo e dqrU

Shift -1 na segunda metade: dqrU -> cpqT

Concatenar: rgo + cpqT

Final: rgocpqT
🎯 Objetivo da Missão

Sua missão como agente honorário do tempo e estudante do CIn é realizar a descriptografia correta da escalação para que a Seleção Brasileira possa entrar em campo.

Input

    A primeira linha contém um número inteiro N (1 ≤ N ≤ 25), representando a quantidade de nomes criptografados a serem descriptografados.
    As próximas N linhas contêm uma string criptografada, representando o nome de um jogador ou do técnico na escalação.

Obs1.: Cada nome foi criptografado conforme o processo descrito, utilizando o conjunto ASCII fornecido.

Obs2.: É OBRIGATORIO o uso de dicionário para armazenar os nomes criptografados e descriptografados

Output

O programa deve imprimir suas saídas em três fases distintas:

    FASE 1: RELATÓRIO DE DESCRIPTOGRAFIA
        Para cada nome processado, exiba na ordem em que foram lidos, separado por uma linha de 50 hifens.

            Criptografada: {entrada_original}

            Descriptografada: {nome_descriptografado}

            --------------------------------------------------

    FASE 2: MENSAGENS DE STATUS
        Após imprimir o relatório completo, itere sobre os nomes descriptografados (já armazenados) e imprima a mensagem de status correspondente para cada um, na ordem em que foram lidos.
            Ronaldo:

                Ronaldo Fenômeno detectado! Autor dos gols na final!

            Ronaldinho:

                Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...

            Cafu:

                Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!

            Marcos:

                Marcos está na área! O paredão do Brasil em 2002!

            Luiz Felipe Scolari:

                Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!

            Outros:

                {jogador} está confirmado na escalação!

    FASE 3: SUMÁRIO FINAL
        Imprima uma linha em branco
        E finalmente, analise a lista completa de nomes e imprima um sumário:
            Se houver menos de 11 JOGADORES:

                !!!!!!!!!! Escalação incompleta! !!!!!!!!!!

                Só foram encontrados {X} jogadores. Faltam jogadores para completar o time.

            Mas caso haja 11 ou mais JOGADORES:

                ++++++++++ Escalação Confirmada ++++++++++

                Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002

            E então a lista formatada apenas por jogadores:

                ==================================================

                ->{jogador1}

                ->{jogador2}

                ...

                ==================================================

            Se o técnico não for encontrado:

                !!!!!!!!!! Técnico não encontrado! !!!!!!!!!!

                Como vamos jogar sem treinar? Como vamos ganhar o penta?

            Se o técnico for encontrado:

                ========== Técnico ==========

                Luiz Felipe Scolari (Felipão)

            Se houver 11 ou mais jogadores E o técnico:

                ===== Tudo pronto! Rumo ao Penta! =====

                Escalação completa com técnico confirmado.

                Que comece o espetáculo, Brasil rumo ao penta!

Examples

Case: 1

Input

12
vrftcO
xicE
rlewN
urlqxM"gwsqT
qrvokofG
vroudF#qvtgdqT
dyolV#rvtgdnkI
qrvugdgnM
rkqlgncpqT
rgocxkT
rgocpqT
ludorfV#hrkngH"|kwN

Output

Criptografada: vrftcO
Descriptografada: Marcos
--------------------------------------------------
Criptografada: xicE
Descriptografada: Cafu
--------------------------------------------------
Criptografada: rlewN
Descriptografada: Lucio
--------------------------------------------------
Criptografada: urlqxM"gwsqT
Descriptografada: Roque Junior
--------------------------------------------------
Criptografada: qrvokofG
Descriptografada: Edmilson
--------------------------------------------------
Criptografada: vroudF#qvtgdqT
Descriptografada: Roberto Carlos
--------------------------------------------------
Criptografada: dyolV#rvtgdnkI
Descriptografada: Gilberto Silva
--------------------------------------------------
Criptografada: qrvugdgnM
Descriptografada: Kleberson
--------------------------------------------------
Criptografada: rkqlgncpqT
Descriptografada: Ronaldinho
--------------------------------------------------
Criptografada: rgocxkT
Descriptografada: Rivaldo
--------------------------------------------------
Criptografada: rgocpqT
Descriptografada: Ronaldo
--------------------------------------------------
Criptografada: ludorfV#hrkngH"|kwN
Descriptografada: Luiz Felipe Scolari
--------------------------------------------------
Marcos está na área! O paredão do Brasil em 2002!
Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!
Lucio está confirmado na escalação!
Roque Junior está confirmado na escalação!
Edmilson está confirmado na escalação!
Roberto Carlos está confirmado na escalação!
Gilberto Silva está confirmado na escalação!
Kleberson está confirmado na escalação!
Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...
Rivaldo está confirmado na escalação!
Ronaldo Fenômeno detectado! Autor dos gols na final!
Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!

++++++++++ Escalação Confirmada ++++++++++
Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002
==================================================
->Marcos
->Cafu
->Lucio
->Roque Junior
->Edmilson
->Roberto Carlos
->Gilberto Silva
->Kleberson
->Ronaldinho
->Rivaldo
->Ronaldo
==================================================
========== Técnico ==========
Luiz Felipe Scolari (Felipão)
===== Tudo pronto! Rumo ao Penta! =====
Escalação completa com técnico confirmado.
Que comece o espetáculo, Brasil rumo ao penta!

Case: 2

Input

9
ludorfV#hrkngH"|kwN
rkqlgncpqT
dulhuuhH"cvuwI
dwhudflS"ngktdcI
rdulgdkT
dncM
lwwhnngD
oddujrP#qfpcptgH
qrvokpwG

Output

Criptografada: ludorfV#hrkngH"|kwN
Descriptografada: Luiz Felipe Scolari
--------------------------------------------------
Criptografada: rkqlgncpqT
Descriptografada: Ronaldinho
--------------------------------------------------
Criptografada: dulhuuhH"cvuwI
Descriptografada: Gusta Ferreira
--------------------------------------------------
Criptografada: dwhudflS"ngktdcI
Descriptografada: Gabriel Picareta
--------------------------------------------------
Criptografada: rdulgdkT
Descriptografada: Ribeirao
--------------------------------------------------
Criptografada: dncM
Descriptografada: Kaka
--------------------------------------------------
Criptografada: lwwhnngD
Descriptografada: Belletti
--------------------------------------------------
Criptografada: oddujrP#qfpcptgH
Descriptografada: Fernando Mograal
--------------------------------------------------
Criptografada: qrvokpwG
Descriptografada: Eunilson
--------------------------------------------------
Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!
Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...
Gusta Ferreira está confirmado na escalação!
Gabriel Picareta está confirmado na escalação!
Ribeirao está confirmado na escalação!
Kaka está confirmado na escalação!
Belletti está confirmado na escalação!
Fernando Mograal está confirmado na escalação!
Eunilson está confirmado na escalação!

!!!!!!!!!! Escalação incompleta! !!!!!!!!!!
Só foram encontrados 8 jogadores. Faltam jogadores para completar o time.
========== Técnico ==========
Luiz Felipe Scolari (Felipão)