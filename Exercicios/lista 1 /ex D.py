# coleta dos os dados necessarios

nome = ' ' # nome, variavel que vai armazenar o maior gasto
mesada = int(input()) # mesada em dolares
cotacao = mesada * float(input()) # cotacao em reais

# coleta os gastos em real
gasto_ração = int(input())
gasto_aluguel = int(input())
gasto_onibus = int(input())

if gasto_ração != gasto_aluguel and gasto_ração != gasto_onibus and gasto_aluguel != gasto_onibus: # aqui verifica se todos os gatos são diferentes

    total_real = gasto_ração + gasto_aluguel + gasto_onibus # caso sim, soma os gastos em real

    # casos dos gastos em real

    if cotacao > total_real:
        print('Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!')
    elif cotacao == total_real:
        print('Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!')
    else:
        print('Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!')

    # varifica qual gasto é maior

    if gasto_ração > gasto_onibus and gasto_ração > gasto_aluguel:
        print('A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!')
        nome = 'Ração'
    elif gasto_aluguel > gasto_onibus and gasto_aluguel > gasto_ração:
        print('Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!')
        nome = 'Aluguel'
    else:
        print('Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!')
        nome = 'Ônibus'

    # relatorio dos gastos

    print(f'MESADA (dólares): {mesada:.2f} dólares\nMESADA (reais): {cotacao:.2f} reais\nMAIOR GASTO: {nome}')