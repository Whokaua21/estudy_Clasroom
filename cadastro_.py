from Poo_fifa import *
Jogadores = {}
Tecnico = {}
Auxiliar = {}
Prepador = {}
Cont = 0
import os
def Cadastro():
    while True:
           
            print(':CADASTRO DE TIMES FIFA:')
            ask_type = int(input('''[1]Jogadores
[2]Comissao Tecnica
[3]Sair
->'''))
            os.system('cls')
        
            match ask_type:
                case 1:
                    
                    while True:
                        try:
                            print('Cadastro jogador')
                            Name = str(input('Nome do Jogador:'))
                            Time = str(input('Nome do time:'))
                            Camis = int(input('Numero da camisa:'))
                            os.system('Cls')
                            print(f'''Jogador Cadastrado
                            
Nome:{Name}
Time:{Time}
Camisa:{Camis}''')
                            Jogadores[Name] = [Time,Camis]
                            os.system('cls')
                            print(Jogadores)
                            break
                        except:
                            
                            print('Informaçao inadequada')
                case 2:
                    while True:
                        print(':Cadastro da comissão:')
                        ask_type = int(input('''[1]Tecnico
[2]Auxiliar
[3]Preparo Fisico '''))
                        if ask_type == 1:
                            Name = input('Nome do Tecnico:')
                            Time = input('Time Comandado:')
                            Esq_tati = int(input('Esquema tatico do tecnico:'))
                            os.system('Cls')
                            Tecnico[Name] = [Time,Esq_tati]
                            print(f'''Nome do Tecnico:{Name}
Time Liderado:{Time}
Esquema tatica:{Esq_tati}''')
                            Fifa_C.Coletiva()

                        elif ask_type == 2:
                            Name = input('Nome do Auxiliar:')
                            Time = input('Time Auxiliado:')
                            Esq_tati = int(input('Esquema tatico do auxiliar:'))
                            os.system('Cls')
                            print(f'''Nome:{Name}
Time auxiliado:{Time}
Esquema Tatico:{Esq_tati}''')
                            Auxiliar[Name] = [Time,Esq_tati]
                            auxiliar.Coletiva()

                        elif ask_type == 3:
                            Name = input('Nome do preparador:')
                            Time = input('Time do preparador:')
                            Elenco = input('Elenco do Preparador:')
                            os.system('Cls')
                            Prepador[Name] = [Time,Elenco]
                            print(f'''Nome:{Name}
Time do preparador:{Time}
Elenco:{Elenco}''')
                            Preparar.Coletiva()
                        else:   
                            os.system('Cls')
                            print('Nao existe essa escolha:')
                            continue      
             
        

Cadastro()