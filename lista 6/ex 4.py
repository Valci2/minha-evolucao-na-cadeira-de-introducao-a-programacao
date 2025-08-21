def print_certo(dicionario):
    '''Para printar certo cada coisa
    
    argumento:
        dicionario (dict): dicionario com os nome, nacionalidade e interesse

    retorno:
        booleano: false, caso o tecnico não tenha interesse
                  true, caso o tecnico tenha interesse
    '''

    if dicionario['interesse'] == 'sim':
        if dicionario['nacionalidade'] != 'brasileiro':

            print(f"{dicionario['nome']} será o quarto estrangeiro a treinar o Brasil. Que honra para o {dicionario['nacionalidade']}!")
            
            if dicionario['nome'] == 'Jorge Jesus':
                print('JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?')
            else:
                print(f"O técnico {dicionario['nacionalidade']} {dicionario['nome']} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!")
        
        else:
            
            if dicionario['nome'] == 'Felipão':
                print('FELIPÃO DE NOVO!? Vem mais um 7x1 por aí?')
            else:
                print(f"O técnico {dicionario['nacionalidade']} {dicionario['nome']} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!")
        return True
    
    else:
        print(f"O {dicionario['nome']} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!")
        return False

# ==================================================================================== #
# inicio do codigo

tecnicos = {}
quantidade_de_tecnicos = int(input())

# loop para cada um dos tecnicos 
for i in range(quantidade_de_tecnicos):

    e_argentino = False # flag para saber se o tecnico é argentino
    chave = 'tec' + str(i + 1) # muda o nome da chave de cada tecnico

    nome = input()
    if nome == 'Ancelotti':
        print('Será que Carleto irá continuar no cargo?')
    elif nome == 'Jorge Jesus':
        print('O mister finalmente retornará ao Brasil?')
    
    nacionalidade = input()
    # caso a nacionalidade seja argentino ele simplesmente para a leitura dos dados do argentino.
    if nacionalidade == 'argentino':
        print('Um hermano comandando a seleção? Sai fora!')
        e_argentino = True

    # caso não seja argentino ele continua a leitura dos dados
    if not e_argentino:
        if nacionalidade == 'alemão':
            print('Iremos mesmo perdoar o 7x1?')
        
        titulos_continentais = int(input())
        titulos_nacionais = int(input())
        aproveitamento = float(input())
        interesse = input()

        # calculo para pontuação geral
        pontuacao_total = (titulos_continentais * 100 + titulos_nacionais * 50) * aproveitamento
        
        if titulos_continentais == 0:
            pontuacao_total = pontuacao_total - (pontuacao_total * 50/100)

        if nacionalidade == 'brasileiro':
            pontuacao_total = pontuacao_total + (pontuacao_total * 10/100)
        elif nacionalidade == 'alemão':
            pontuacao_total = pontuacao_total - (pontuacao_total * 10/100)
        
        # cada tecnico vai ter uma chave diferente
        tecnicos[chave] = {
            'nome': nome,
            'nacionalidade': nacionalidade,
            'pontuacao': pontuacao_total,
            'interesse': interesse
        }

# armazena os melhores 3 tecnicos
melhor = segundo = terceiro = ''

for chave in tecnicos:
    if melhor == '' or tecnicos[chave]['pontuacao'] > tecnicos[melhor]['pontuacao']:
        terceiro = segundo
        segundo = melhor
        melhor = chave
    elif segundo == '' or tecnicos[chave]['pontuacao'] > tecnicos[segundo]['pontuacao']:
        terceiro = segundo
        segundo = chave
    elif terceiro == '' or tecnicos[chave]['pontuacao'] > tecnicos[terceiro]['pontuacao']:
        terceiro = chave

# printa os 3
print('Lista de treinadores - CBF')
print(f"1º {tecnicos[melhor]['nome']} - {tecnicos[melhor]['nacionalidade']} - {tecnicos[melhor]['pontuacao']:.2f} pontos")
print(f"2º {tecnicos[segundo]['nome']} - {tecnicos[segundo]['nacionalidade']} - {tecnicos[segundo]['pontuacao']:.2f} pontos")
print(f"3º {tecnicos[terceiro]['nome']} - {tecnicos[terceiro]['nacionalidade']} - {tecnicos[terceiro]['pontuacao']:.2f} pontos")

# caso ancelotti esteja no time ele para o programa
if (tecnicos[melhor]['nome'] == 'Ancelotti' and tecnicos[melhor]['interesse'] == 'sim') or \
    (tecnicos[segundo]['nome'] == 'Ancelotti' and tecnicos[segundo]['interesse'] == 'sim') or \
    (tecnicos[terceiro]['nome'] == 'Ancelotti' and tecnicos[terceiro]['interesse'] == 'sim'):
    print('Ancelotti será o quarto estrangeiro a treinar o Brasil. Que honra para o italiano!')
    print('Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!')

else:
    # caso não, ele analiza cada cenario
    analise = False
    analise = print_certo(tecnicos[melhor])
    if not analise:
        analise = print_certo(tecnicos[segundo])
        if not analise:
            analise = print_certo(tecnicos[terceiro])
            if not analise:
                print('Nenhum técnico aceitou a maior seleção do mundo!? Que humilhação, Sr. Samir Xaud!!!')