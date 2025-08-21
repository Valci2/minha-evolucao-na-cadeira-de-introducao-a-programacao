def batalha(vida_lobo, postura_lobo, vida_genichiro ,postura_genichiro, cabaca_curativa, turnos=1):
    '''Faz uma simulação da batalha entre o lobo e genichiro
    
    argumentos:
        vida_lobo (int): vida do lobo
        postura_lobo (int): postura total do lobo
        vida_genichiro (int): a vida do genichiro
        postura_genichiro (int): postura de genichiro
        cabaca_curativa (int): quantidade de cabaças que ele pode usar
        turnos (int): quantidade de turnos

    retorna:
        nada
    '''
    # casos de parada
    # se a vida do lobo for menor que 0, ele perde e o programa para
    if vida_lobo <= 0:
        print('Sekiro cai de joelhos, derrotado...')
        print('====================================')
        print('Vitória de Genichiro: Morte.')
    
    # se a postura do lobo for maior que 100, ele perde e o programa para
    elif postura_lobo >= 100:
        print('A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!')
        print('====================================')
        print('Vitória de Genichiro: Morte.')
    
    # caso a vida de genichiro ou a postura dele seja maior que 100, ele vai ir para o turno de decisão
    elif vida_genichiro <= 0 or postura_genichiro >= 100:

        # printa o turno
        print(f'--- Turno {turnos} ---')
        print('Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!')

        # input das ações possiveis
        acao = input()

        # se a ação for ataque, o programa para
        if acao == 'ataque':
            print('Sekiro executa um Golpe Mortal em Genichiro!')
            print('====================================\nVitória de Sekiro: Golpe Mortal!')
    
        # se ele hesitar, o programa continua
        elif acao == 'hesitar':
            
            print('O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!')
            
            # caso a postura dele seja maior que 100 a postura dele volta para o 50
            if postura_genichiro >= 100:
                postura_genichiro = 50

                if vida_genichiro < 50:
                    vida_genichiro = 50
            
            elif vida_genichiro <= 0:
                postura_genichiro = 50
                vida_genichiro = 50

            return batalha(vida_lobo, postura_lobo, vida_genichiro, postura_genichiro, cabaca_curativa, turnos + 1)
    
    else:
    
        print(f'--- Turno {turnos} ---')

        # acoes validas dos personagens
        acoes_de_genichiro = ['ataque', 'defesa', 'recuperação de postura', 'ataque kanji']
        acoes_de_lobo = ['ataque', 'defesa', 'defesa perfeita', 'usar cabaça', 'desviar', 'contra ataque mikiri']

        # loop o input até que o input de genichiro ate que ele esteja dentro de uma ação valida
        acao_de_genichiro = input()
        while acao_de_genichiro not in acoes_de_genichiro:
            print('Genichiro não tem esse movimento em seu arsenal.')
            acao_de_genichiro = input()
        
        # loop o input até que o input de lobo ate que ele esteja dentro de uma ação valida
        acao_de_lobo = input()
        while acao_de_lobo not in acoes_de_lobo:
            print('O lobo não adquiriu esse movimento ainda.')
            acao_de_lobo = input()

        # caso o genichiro use o ataque
        if acao_de_genichiro == 'ataque':
        
            if acao_de_lobo == 'ataque':
                print('Clima de tensão! Os dois atacam numa luta implacável!')
                vida_lobo -= 25
                vida_genichiro -= 10
                postura_genichiro += 15
            elif acao_de_lobo == 'defesa':
                print('Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!')
                vida_lobo -= 10
                postura_lobo += 20
            elif acao_de_lobo == 'defesa perfeita':
                print('Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!')
                postura_genichiro += 25
            elif acao_de_lobo == 'usar cabaça' and cabaca_curativa == 0:
                print('Sekiro busca sua cabaça, mas ela está vazia!\nEnquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!')
            elif acao_de_lobo == 'usar cabaça':
                print('Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!')
                cabaca_curativa -= 1
                vida_lobo -= 25
            elif acao_de_lobo == 'desviar':
                print('O lobo desvia agilmente do ataque comum de Genichiro!')
            elif acao_de_lobo == 'contra ataque mikiri':
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.')
                postura_genichiro += 10
            
        # caso o genichiro use o defesa
        elif acao_de_genichiro == 'defesa':

            if acao_de_lobo == 'ataque':
                print('Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!')
                postura_genichiro += 5
            elif acao_de_lobo == 'defesa':
                print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.')
            elif acao_de_lobo == 'defesa perfeita':
                print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.')
            elif acao_de_lobo == 'usar cabaça' and cabaca_curativa == 0:
                print('Sekiro busca sua cabaça, mas ela está vazia!\nGenichiro mantém a guarda, enquanto o lobo percebe seu erro.')
            elif acao_de_lobo == 'usar cabaça':
                print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.')
                vida_lobo += 25
                cabaca_curativa -= 1
            elif acao_de_lobo == 'desviar':
                print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')
            elif acao_de_lobo == 'contra ataque mikiri':
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')

        # caso o genichiro use o recuperação de postura
        elif acao_de_genichiro == 'recuperação de postura':

            if acao_de_lobo == 'ataque':
                print('Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!')
                vida_genichiro -= 10
                postura_genichiro += 15
            elif acao_de_lobo == 'defesa':
                print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                postura_genichiro = 0
            elif acao_de_lobo == 'defesa perfeita':
                print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                postura_genichiro = 0
            elif acao_de_lobo == 'usar cabaça' and cabaca_curativa == 0:
                print('Sekiro busca sua cabaça, mas ela está vazia!\nGenichiro aproveita a hesitação do lobo para recuperar sua postura.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                postura_genichiro = 0
            elif acao_de_lobo == 'usar cabaça':
                print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                vida_lobo += 25
                cabaca_curativa -= 1
                postura_genichiro = 0
            elif acao_de_lobo == 'desviar':
                print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                postura_genichiro = 0
            elif acao_de_lobo == 'contra ataque mikiri':
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                postura_genichiro = 0

        # caso o genichiro use o ataque kanji
        elif acao_de_genichiro == 'ataque kanji':
                            
            if acao_de_lobo == 'usar cabaça' and cabaca_curativa == 0:
                print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!\nPara piorar, Sekiro nem sequer tinha uma cabaça para usar!')
                vida_lobo -= 50
                postura_lobo += 20
            elif acao_de_lobo == 'usar cabaça':
                print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
                cabaca_curativa -= 1
                vida_lobo -= 50
                postura_lobo += 20
            elif acao_de_lobo == 'desviar':
                print('O lobo desvia do ataque especial de Genichiro com muita agilidade!')
            elif acao_de_lobo == 'contra ataque mikiri':
                print('O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!')
                postura_genichiro += 25
            else:
                print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
                vida_lobo -= 50
                postura_lobo += 20

        # faz o retorno da função adicionando mais +1 na quantidade de rodadas        
        return batalha(vida_lobo, postura_lobo, vida_genichiro, postura_genichiro, cabaca_curativa, turnos + 1)

# começo do programa
print('O duelo começa! Suas decisões determinarão o vencedor.')

# loop da batalha
batalha(vida_lobo=100, postura_lobo=0, vida_genichiro=100, postura_genichiro=0, cabaca_curativa=2)