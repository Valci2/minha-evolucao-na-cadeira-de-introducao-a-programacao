Paris está mais uma vez em perigo! Durante uma ronda noturna, Ladybug e Cat Noir descobriram que alguém tentou invadir o Templo dos Miraculous, um local sagrado, protegido há gerações pelo Mestre Fu. Infelizmente, o vilão conseguiu escapar antes que os heróis o alcançassem.

Ladybug e Catnoir

Para impedir que o Hawk Moth consiga controlá-lo novamente, é essencial descobrir quem foi o akumatizado responsável pela tentativa de invasão. A pessoa em questão acredita ter estado em outro lugar no momento do crime, mas Ladybug suspeita que suas memórias tenham sido manipuladas pelo poder do Miraculous.

Agora, os heróis de Paris precisam saber quem foi akumatizado para proteger de uma nova tentativa de invasão do Hawk Moth. Cabe a você ajudá-la a descobrir quem está sob influência do mal!

Cada um afirma estar em um determinado lugar em certo horário. Use seus conhecimentos em programação para fazer uma análise cautelosa de quem está falando a verdade e quem está mentindo.
Locais de Paris e suas características:

    Torre Eiffel — Segurança: Média — Horário de Funcionamento: 09:00 às 23:00.
    Museu do Louvre — Segurança: Alta — Horário de Funcionamento: 08:00 às 18:00.
    Catacumbas de Paris — Segurança: Baixa — Horário de Funcionamento: 10:00 às 20:00.
    Biblioteca Nacional — Segurança: Média — Horário de Funcionamento: 07:00 às 22:00.
    Galeria Lafayette — Segurança: Alta — Horário de Funcionamento: 10:00 às 21:00.
    Parque dos Príncipes — Segurança: Baixa — Horário de Funcionamento: 06:00 às 23:00.
    Catedral de Notre-Dame — Segurança: Alta — Horário de Funcionamento: 08:00 às 18:30.
    Jardim de Luxemburgo — Segurança: Média — Horário de Funcionamento: 07:00 às 19:00.
    Padaria Dupain Cheng — Segurança: Baixa — Horário de Funcionamento: 04:00 às 20:00.

Obs.: Todos os horários estão no formato hh:mm (24h).

Input

Você receberá uma linha de input para cada suspeito, contendo:

    {nome} - {horário} - {local} - {testemunha}

    nome: nome do suspeito.
    horário: hora (no formato hh:mm) em que o suspeito afirma que esteve no local.
    local: o local onde o suspeito diz ter estado.
    testemunha: se há uma testemunha à favor do suspeito, pode ser "sim" ou "nenhuma".

Sempre haverão apenas 6 suspeitos.

Output

Diversos fatores podem indicar que um suspeito está sendo manipulado, mas devem ser avaliados em ordem de prioridade. Isso significa que, se uma acusação de prioridade mais alta for identificada, todas as outras de nível inferior devem ser desconsideradas.

Exemplo: se uma pessoa mencionou um local que não existe e outra estava em um local verdadeiro, mas fora do horário permitido, você deve imprimir apenas a acusação do local inexistente, pois possui maior prioridade.

A ordem de prioridade é:
1. Local não existente:

Se o local não está na lista oficial de locais de Paris:

    Caso haja apenas 1 local inválido:

    Esse lugar {local} nem existe! {nome} com certeza foi akumatizado!

    Caso haja mais de 1 local inválido:

    {local1}, {local2}, (...) nem existem! {nome1}, {nome2}, (...) estão mentindo!

2. Fora do horário de funcionamento:

Se o local está na lista, mas fora do horário permitido:

    Caso haja apenas 1 local fechado:

    {local} nem estava aberto às {hora}! {nome} recebeu memórias falsas!

    Caso haja mais de 1 local fechado:

    {local1}, {local2}, (...) estavam fechados nesse horário! {nome1}, {nome2}, (...) podem ter sido manipulados pelo Hawk Moth!

3. Segurança baixa com todos os álibis válidos:

Se todos os locais são válidos e horários corretos, verifica-se a segurança:

    Caso tenha apenas 1 suspeito em local de segurança baixa:

    {nome} estava em um local de segurança baixa... Ele pode ter mentido!

    Caso tenha mais de 1 suspeito em locais de segurança baixa:

    {nome1}, {nome2}, (...) estavam em locais de segurança baixa... Eles podem estar forjando um álibi!

4. Presença de testemunhas:

Se ainda não houve conclusão, analisa-se as testemunhas:

Serão procuradas pessoas que possam confirmar se o suspeito está falando a verdade. Por isso, quem não tem testemunha é mais suspeito.

    Caso haja apenas 1 suspeito sem testemunha:

    {nome} não teve testemunha para confirmar o álibi. É o mais suspeito até agora.

    Caso tenha mais de 1 suspeito sem testemunha e menos que 6:

    {nome1}, {nome2}, (...) não foram confirmados por ninguém. O Hawk Moth pode vir atrás deles de novo

    Caso ninguém tenha testemunha (ou seja, todos são suspeitos):

    Ninguém viu ninguém… estranho!!

5. Sem suspeitos:

Se mesmo após todos os critérios continuar sem suspeitos, imprima:

    Poxa vida, todos os àlibis parecem válidos… mas algo continua errado

IMPORTANTE:

Sempre que houver mais de um local ou mais de um nome a serem listados na saída, os itens devem ser apresentados em ordem alfabética, separados por vírgulas.

Obs.: Não haverá o uso do conectivo "e" entre locais ou suspeitos.

Examples

Case: 1

Input

Alya - 08:00 - Mirabilandia Paris - sim
Chloe - 08:15 - Torre Eiffel - sim
Kagami - 08:20 - Galeria Lafayette - sim
Luka - 08:25 - Biblioteca Nacional - sim
Max - 08:30 - Catedral de Notre-Dame - sim
Nino - 08:35 - Museu do Louvre - sim

Output

Esse lugar Mirabilandia Paris nem existe! Alya com certeza foi akumatizado!

Case: 2

Input

Luka - 16:20 - Torre Eiffel - sim
Kagami - 09:10 - Biblioteca Nacional - nenhuma
Max - 16:50 - Catedral de Notre-Dame - sim
Chloe - 13:37 - Torre Eiffel - sim
Alya - 12:00 - Museu do Louvre - sim
Nino - 14:40 - Jardim de Luxemburgo - sim

Output

Kagami não teve testemunha para confirmar o álibi. É o mais suspeito até agora.