O Campeonato Mundial de Tênis de Mesa 2025 está chegando, e desta vez a cidade de Doha será o palco das disputas entre os melhores jogadores do planeta. Entre os competidores, está o melhor atleta brasileiro da história no esporte: Hugo Calderano!!!

Mas, com tantas competições e treinos, Calderano está precisando de uma ajuda para se organizar antes de partir para o torneio. Para isso, ele convocou vocês alunos de IP no CIn. A missão é ajudar o nosso campeão a garantir que tudo esteja pronto para ele arrasar no campeonato!

Sua tarefa será criar um programa que contabilize 4 materiais que são essenciais para o campeonato: Uniformes para os jogos, Isotônicos para ajudar na recuperação, Raquetes reservas e Toalhas para se secar durante os sets.

Mas cuidado!!! O Sueco Truls Möregårdh, que eliminou Hugo Calderano nas semifinais das Olímpiadas de Paris 2024, está pronto para arruinar os planos do atleta brasileiro de novo! Dessa vez ele foi para o jogo sujo e quer sabotar os materiais de Hugo!

Input

Seu programa deverá receber uma quantidade indefinida de entradas:

    Entrada1

    Entrada2

    Entrada3

    (...)

    EntradaN

E vai parar de receber entradas após receber:

    FIM

As entradas podem ser alguns dos 4 materiais que vão ser contabilizados:

    Uniforme

    Isotônico

    Raquete

    Toalha

Ou a sabotagem de Truls Möregårdh, no seguinte modelo:

    Sabotagem

    (Material que será sabotado)

OBS.1: Cada vez que um material for contabilizado (sem tentativa de sabotagem), ele será adicionado ao contador.

OBS.2: Cada vez que um material for sabotado com sucesso, ele será diminuído ao contador.

OBS.3: A sabotagem só terá efeito se houver pelo menos uma unidade daquele material contabilizado anteriormente.

Output

Para cada material imprima a seguinte mensagem:

-Uniforme(se estiver sendo contabilizado):

    Tava faltando camisa! Agora temos {nº de uniformes contabilizados} uniforme(s)

-Uniforme(se estiver sendo sabotado):

    O sueco está roubando as camisas de Hugo!

-Isotônico(se estiver sendo contabilizado):

    Bora garantir a hidratação! Agora temos {nº de isotônicos contabilizados} isotônico(s)

-Isotônico(se estiver sendo sabotado):

    O sueco está sabotando a hidratação de Hugo!

-Raquete(se estiver sendo contabilizada):

    Mais uma raquete saindo! Agora temos {nº de raquetes contabilizados} raquete(s)

-Raquete(se estiver sendo sabotada):

    O sueco está roubando as raquetes de Hugo!

-Toalha(se estiver sendo contabilizada):

    Mais uma toalha saindo! Agora temos {nº de toalhas contabilizados} toalha(s)

-Toalha(se estiver sendo sabotada):

    O sueco está roubando as toalhas de Hugo!

Após o encerramento do programa, imprima um relatório final dos materiais:

    Bora ver o relatório final dos materiais!

    Uniforme: {nº de final de uniformes} unidade(s).

    Isotônico: {nº de final de isotônicos} unidade(s).

    Raquete: {nº de final de raquetes} unidade(s).

    Toalha: {nº de final de toalhas} unidade(s).

Caso o número total de materiais for zero e tiver ocorrido alguma sabotagem, imprima a seguinte mensagem:

    Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!

Caso o número total de materiais for zero, mas não houve sabotagem, imprima a seguinte mensagem:

    Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.

Se o número total de materiais for maior que zero, mas não ter pelo menos um de cada, imprima a seguinte mensagem:

    Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!

Caso contrário, imprima a seguinte mensagem:

    Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!

Dica: Testem entradas exemplos para que ocorra todos os casos apresentados e verificarem se existe algum problema em que não está visível.

Examples

Case: 1

Input

Uniforme
Uniforme
Isotônico
Toalha
Sabotagem
Uniforme
FIM

Output

Tava faltando camisa! Agora temos 1 uniforme(s)
Tava faltando camisa! Agora temos 2 uniforme(s)
Bora garantir a hidratação! Agora temos 1 isotônico(s)
Mais uma toalha saindo! Agora temos 1 toalha(s)
O sueco está roubando as camisas de Hugo!
Bora ver o relatório final dos materiais!
Uniforme: 1 unidade(s).
Isotônico: 1 unidade(s).
Raquete: 0 unidade(s).
Toalha: 1 unidade(s).
Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!