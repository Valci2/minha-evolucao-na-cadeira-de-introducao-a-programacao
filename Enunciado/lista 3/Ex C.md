A Terra está sob a ameaça de Thanos, e apenas os Vingadores podem nos salvar. Com Thanos reunindo forças para um novo ataque devastador, a equipe precisa se preparar com precisão e estratégia.

Antes da batalha começar, é necessário organizar o armamento: cada item disponível na base dos Vingadores deve ser cuidadosamente listado. No entanto, com o caos do combate iminente, o acesso a alguns equipamentos pode ser incerto… ou até esquecido.

Você, aluno do CIn, foi encarregado de fazer um programa que coordene a distribuição dos itens durante a batalha, garantindo que cada arma usada esteja realmente disponível — e que não seja reutilizada indevidamente!

A missão é clara: quando um Vingador requisitar um item, você deverá verificar se ele está disponível e ainda não foi usado. Se estiver tudo certo, a arma será liberada com sucesso. Se o item solicitado não estiver disponível, os Vingadores sofrerão um golpe do Thanos. E se a arma solicitada já tiver sido usada, eles também sofrerão um golpe, pois não puderam atacar naquele momento, colocando a vitória e o universo em risco.

Ao final do combate, o número de golpes sofridos pelos Vingadores determinará o desfecho da batalha:

    Se nenhum golpe for sofrido, a vitória é total, com direito a festa e frases icônicas dos heróis.
    Se apenas um golpe for sofrido, foi por pouco — vitória apertada! (MAS ELE AINDA GANHAMMMMM🎉🥳😝)
    Se dois ou mais itens faltarem, ou seja, eles sofrerem 2 golpes ou mais. Thanos venceu… e os Vingadores terão que recuar e ver o universo como eles conhecem desaparecer....

Sua missão para ajudar esses heróis é gerenciar esse sistema de controle e registrar corretamente as armas usadas, as armas faltantes e, claro, a moral da equipe ao final da batalha.
Regras do sistema:

    Cada arma só pode ser usada uma vez.
    Se a arma estiver disponível e ainda não tiver sido usada, ela é considerada usada com sucesso.
    Se a arma já tiver sido usada, ela não pode ser reutilizada e será contabilizado +1 golpe do Thanos.
    Se o item nunca esteve na lista de disponíveis, ou seja, não está disponível (não foi inserida no arsenal), é contabilizado +1 golpe do Thanos.

Ao final, o sistema imprime:

    A quantidade total de armas que os vingadores conseguiram usar corretamente.
    Uma mensagem indicando vitória total, vitória apertada ou derrota, dependendo da quantidade de golpes.

Input

Primeiramente, você receberá um número inteiro N representando a quantidade de armas disponíveis na base dos Vingadores:

    N (int)

Em seguida, nas próximas N linhas, serão recebidos os nomes das armas disponíveis (uma por linha).

Depois, por uma quantidade indeterminada de vezes, receba as solicitações de armas (nomes das armas), uma por linha, até que a palavra "fim" seja digitada.
📥 Exemplo de Input:
Primeira parte do problema (recebendo as armas que estão disponíveis):

    4

    Mjolnir

    Escudo do Capitão

    Armadura do Homem de Ferro

    Arco do Gavião

Segunda parte do problema (recebendo as armas que tentarão ser usadas na batalha):

    Mjolnir

    Arco do Gavião

    Mjolnir

    Espada do Ronin

    fim

Output
✅ Se a arma está disponível e ainda não foi usada, deverá ser printado isso:

    {nome_arma} usado(a) com sucesso!

♻️ Se a arma já foi usada, deverá ser printado isso:

    {nome_arma} já foi usado(a)!

❌ Se a arma não está disponível, ou seja, não foi inserida no arsenal, deverá ser printado isso:

    {nome_arma} não está disponível!

🔚 Ao final, após entrada "fim" deverá ser printado isso:

    Batalha encerrada! Os Vingadores utilizaram {quantidade_armas} arma(s).

🏆 Se sofreram 0 golpes do Thanos, deverá ser printado isso:

    Vitória! Os Vingadores salvaram o UNIVERSO!

    (pule uma linha)

    Tony Stark:

    Salvar o mundo de novo? Vou precisar de um aumento.

    (pule uma linha)

    Thor:

    Espero que tenha cerveja depois disso!

    (pule uma linha)

    Homem-Aranha:

    Posso dizer que ajudei, né? Tipo… oficialmente?

    Dá pra postar isso no Insta dos Vingadores?

⚠️ Se sofreram 1 golpe do Thanos, deverá ser printado isso:

    Os Vingadores sofreram um golpe do Thanos!

    Vitória por pouco! Os Vingadores ganharam...

    (pule uma linha)

    Tony Stark:

    Quase que eu fico sem troco para o cafezinho.

    (pule uma linha)

    Thor:

    Esse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!

    (pule uma linha)

    Peter Quill (Star-Lord):

    Cara, quase perdi o ritmo do meu walkman!

💥 Se sofreram 2 ou mais golpes do Thanos, deverá ser printado isso:

    Os Vingadores sofreram {quantidade_golpes} golpes do Thanos!

    Derrota... Os Vingadores não conseguiram todas as armas necessárias.

    (pule uma linha)

    Tony Stark:

    Essa não foi das melhores ideias...

    (pule uma linha)

    Thor:

    Culpa do humano. Eu sabia que devíamos ter chamado o Hulk.

Examples

Case: 1

Input

4
Manopla do Infinito
Escudo de Vibranium
Machado Stormbreaker
Armadura Mark LXXXV
Manopla do Infinito
Escudo de Vibranium
Armadura Mark LXXXV
Machado Stormbreaker
fim

Output

Manopla do Infinito usado(a) com sucesso!
Escudo de Vibranium usado(a) com sucesso!
Armadura Mark LXXXV usado(a) com sucesso!
Machado Stormbreaker usado(a) com sucesso!
Batalha encerrada! Os Vingadores utilizaram 4 arma(s).
Vitória! Os Vingadores salvaram o UNIVERSO!

Tony Stark:
Salvar o mundo de novo? Vou precisar de um aumento.

Thor:
Espero que tenha cerveja depois disso!

Homem-Aranha:
Posso dizer que ajudei, né? Tipo… oficialmente?
Dá pra postar isso no Insta dos Vingadores?

Case: 2

Input

3
Arco do Gavião Arqueiro
Lança Wakandana
Discos da Vespa
Discos da Vespa
Arco do Gavião Arqueiro
Bumerangue do Capitão
fim

Output

Discos da Vespa usado(a) com sucesso!
Arco do Gavião Arqueiro usado(a) com sucesso!
Bumerangue do Capitão não está disponível!
Batalha encerrada! Os Vingadores utilizaram 2 arma(s).
Os Vingadores sofreram um golpe do Thanos!
Vitória por pouco! Os Vingadores ganharam...

Tony Stark:
Quase que eu fico sem troco para o cafezinho.

Thor:
Esse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!

Peter Quill (Star-Lord):
Cara, quase perdi o ritmo do meu walkman!

Case: 3

Input

5
Escudo do Capitão América
Martelo de Thor
Armadura do Homem de Ferro
Arco do Gavião Arqueiro
Chicote de Energia
Martelo de Thor
Chicote de Energia
Lança Wakandana
Escudo do Capitão América
Martelo de Thor
Espada de Asgard
Bumerangue do Capitão
Armadura do Homem de Ferro
fim

Output

Martelo de Thor usado(a) com sucesso!
Chicote de Energia usado(a) com sucesso!
Lança Wakandana não está disponível!
Escudo do Capitão América usado(a) com sucesso!
Martelo de Thor já foi usado(a)!
Espada de Asgard não está disponível!
Bumerangue do Capitão não está disponível!
Armadura do Homem de Ferro usado(a) com sucesso!
Batalha encerrada! Os Vingadores utilizaram 4 arma(s).
Os Vingadores sofreram 4 golpes do Thanos!
Derrota... Os Vingadores não conseguiram todas as armas necessárias.

Tony Stark:
Essa não foi das melhores ideias...

Thor:
Culpa do humano. Eu sabia que devíamos ter chamado o Hulk.