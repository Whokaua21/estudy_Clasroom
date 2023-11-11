import os
# P.O.O Class

# Sometime i  wrife in portugues because is easy

# P.o.o is a rule what help in Program
# He deal with that how  if all is object

# Now a Exeple:

# let´s go do

class Carro():
    # method contruct
    def __init__(self,marca,modelo,ano,peso,possui_4_portas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.peso = peso
        self.porta = possui_4_portas
    def buzina(self):
        print(f'{self.marca} - {self.modelo} esta fazendo Poooo')

Carro_meu = Carro('Vucan','Hilux',2011,2000,True)


# To print the object vou can use the 
# Variavel.functio
# use the (var : type) to a tip
# is if you use '''''' he input a subtitle is speak  how use
# Obs(you has what wrife that)
# that help much

# My Exercise
class Fature():
    def __init__(self,item:str,preço:int,quant:int) -> None:
        '''Here salve the informat of item buy

        '''
        self.item = item
        self.preço = preço
        self.quant = quant
    def Fatura(self):
        Fatura = self.preço * self.quant
        return Fatura
item_str = input('Nome do item:')
preço_int = int(input('Preço do item:'))
quant_int = int(input('Quantos pegou:'))
os.system('cls')
Compre_class = Fature(item_str,preço_int,quant_int)

print(f'Nome do item:{Compre_class.item}')
print(f'Preço do item:{Compre_class.preço}')
print(f'Quantidade:{Compre_class.quant}')
print(f'Sua fatura foi de {Compre_class.Fatura()}')
# My exercise: was did a class what save item ,preço,quantidade is fatura
# the calcule of fatura is in other class 
# later print all