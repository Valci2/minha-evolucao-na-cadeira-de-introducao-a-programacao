Com o clima de InterCIn fervendo nas veias, um grupo de amigos, assíduos frequentadores do DA, se encontravam praticando o bom e velho PingPong. No meio da partida, iniciou-se uma discussão: qual é a melhor empunhadura do tênis de mesa? Para resolver essa discussão, eles resolveram fazer um pesquisa com os alunos que passavam pelo corredor. Agora eles precisam da sua ajuda para contabilizar os votos e determinar qual é empunhadura favorita da galera!

Seu programa deve receber os votos coletados pelos amigos e contabilizá-los para montar um ranking entre as 3 possíveis empunhaduras: “Clássica”, “Caneta” ou “Classineta”.

OBS.: NÃO haverá casos de empate no ranking.

Input

Inicialmente, você receberá como entrada um número inteiro, que representa a quantidade de pessoas que participarão da votação.

    qtd_pessoas (int)

Em seguida, para cada pessoa, você receberá o voto do entrevistado, que pode ser “Clássica”, “Caneta” ou “Classineta”.

    voto

Output

Após calcular o ranking final, você deve imprimir a mensagem

    Estamos calculando... tão rápido quanto dar Run no Dikastis...

Em seguida, será impresso o ranking final no seguinte formato:

    1º lugar: {primeiro_lugar} ({pts_primeiro} votos)

    2º lugar: {segundo_lugar} ({pts_segundo} votos)

    3º lugar: {terceiro_lugar} ({pts_terceiro} votos)

Por fim, caso a primeira colocada seja “Clássica” e sua diferença de votos para a segunda colocada seja de pelo menos 5 votos , você deve imprimir

    Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!

Examples

Case: 1

Input

12
Clássica
Caneta
Clássica
Clássica
Classineta
Clássica
Classineta
Clássica
Clássica
Clássica
Clássica
Clássica

Output

Estamos calculando... tão rápido quanto dar Run no Dikastis...
1º lugar: Clássica (9 votos)
2º lugar: Classineta (2 votos)
3º lugar: Caneta (1 votos)
Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!

Case: 2

Input

6
Classineta
Clássica
Clássica
Caneta
Classineta
Classineta

Output

Estamos calculando... tão rápido quanto dar Run no Dikastis...
1º lugar: Classineta (3 votos)
2º lugar: Clássica (2 votos)
3º lugar: Caneta (1 votos)