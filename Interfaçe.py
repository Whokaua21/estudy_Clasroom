from Conta_corente import *
Save_data = Corrente_bank
while True:
    print('''------Gerenciador------''')
    print('Bem vindo ao gerenciador de banco e poupança\n')
    try:
        print('Qual você deseja mecher:')
        Choice_accont = int(input('''
[1] Conta-Corrente
[2]Poupança
->'''))
    except:
        print('O sistema detectou uma letra so pode numero aqui')
    match Choice_accont:
        case 1:
            print('------:Você escolheu Conta-Corrente:------')
            Genrenciar = int(input('''
[1]Criar uma conta
[2]Verificar conta
[3]Sacar
->'''))
            match Genrenciar:
                case 1:
                    print('------Criaçao de conta------')
                    Usu_cont = input('Nome do novo usuario:')
                    while True:
                        print('Senha de 4 digitos numericos')
                        pass_cont = str(input('Senha do usuario:').lower())
                        if pass_cont in 'qwertyuiopasdfghjklçzxcvbnm,.;ç~[]/=-0987654321':
                            print('Não pode ser letras ou simbolos')
                        elif len(pass_cont) == 4:
                            break
                        else:
                            print('Sua senha deve ter 4 digitos numericos:')
                    Verific = input('Escreva o nome de alguma coisa para te indentificar:')
                    Save_data = Corrente_bank(Verific,Usu_cont,'','',pass_cont)
                    print(Save_data.desc)
                    print(Save_data.nam)
                    print(Save_data.senha)
                case 2:
                    print('------Verificaçao de conta------')
                    try:
                        Save_data.Verificaçao()
                    except:
                        print('Nao tem nenhuma conta aqui')
                case 3:
                    print('------Sacamento------')
        case 2:
            ...
