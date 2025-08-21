nome = str(input()) # recebe o nome do aluno

ac1 = int(input()) # as variaveis que recebem as notas
ac2 = int(input()) # ac abreviação de acertos
ac3 = int(input())
ac4 = int(input()) 
ac5 = int(input()) 
ac6 = int(input()) 
    
nota1 = ac1 # a nota é a mesma que a quantidade de acertos
nota2 = ac2
nota3 = ac3
nota4 = ac4 * (10 / 6) # aqui os acertos são multiplicados por 10/6 para calcula-lo de media com os 6 acertos
nota5 = ac5 * (10 / 6)
nota6 = ac6 * (10 / 6)

media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6 # calcula a média

print(f'A média de {nome} é {media:.1f}') # mostra a media e o nome do estudante

# Analizar desempenho do estudante

progresso_constante = True # inicia uma variavel para verificar se o aluno teve progresso constante que começa sendo verdadeira
if nota2 < nota1:
    progresso_constante = False # caso a nota 2 seja menor que a nota 1, o progresso constante é falso, e assim por diante.
if nota3 < nota2:
    progresso_constante = False
if nota4 < nota3:
    progresso_constante = False
if nota5 < nota4:
    progresso_constante = False
if nota6 < nota5:
    progresso_constante = False

if progresso_constante:
    print('Progresso constante! Parabéns pelo esforço!') # caso o aluno tenha tido progresso constante, imprime a mensagem
else:
    print('Alerta! Queda no rendimento.') # caso não tenha tido progresso constante, imprime a mensagem de alerta

# Verificar se o aluno não respondeu pelo menos 2 listas de exercícios

listas_nao_feitas = 0 # variavel de contagem
if ac1 == 0:
    listas_nao_feitas += 1 # adiciona 1 a contagem sempre que o aluno não respondeu a lista
if ac2 == 0:
    listas_nao_feitas += 1
if ac3 == 0:
    listas_nao_feitas += 1
if ac4 == 0:
    listas_nao_feitas += 1
if ac5 == 0:
    listas_nao_feitas += 1
if ac6 == 0:
    listas_nao_feitas += 1

if listas_nao_feitas >= 2: # caso mais de uma lista não tenha sido feita, imprime a mensagem de alerta
    print("Alerta! Múltiplas listas não respondidas.")

# Analizar o a média
if media >= 8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
elif media >= 7 and media <= 7.9:
    print("Parabéns pelo bom desempenho!")
else:
    print("Alerta! Desempenho abaixo do esperado.")