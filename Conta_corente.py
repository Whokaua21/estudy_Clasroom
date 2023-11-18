from random import *
Id_usu = randint(1000,35000)
class Corrente_bank():
    def __init__(self,Indentif:str,name_usu:str,Saldo:float,Saque:float,Senha:int) -> None:
        self.desc = Indentif
        self.nam = name_usu
        self.saldo = Saldo
        self.sacar = Saque
        self.senha = Senha
    
    def Saque_din(self,Dinheiro):
        Sacar_men = self.sacar - Dinheiro
    
    def Verificaçao(self):
        try:
            print(f'Nome do Usuario:{self.nam}')
            print(f'Indentificaçao:{self.desc}')
            print(f'Senha:****')
            print(f'ID:{Id_usu}')
        except:
            print('Nenhuma conta criada')
        try:
            print(f'Saldo:{self.saldo}')
        except:
            print('Saldo:0')


class Poupança(Corrente_bank):
    def __init__(self, Indentif:str, name_usu:str, Saldo:float,Juros:float,Senha:int) -> None:
        super().__init__(Indentif, name_usu, Saldo,Senha)
        self.Juros = Juros
    def Juros(self,Gerente_juros):
        Porcento = self.saldo / 100 * Gerente_juros

