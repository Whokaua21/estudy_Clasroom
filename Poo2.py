# Just to remenber how use 
# class Teste():
#     def __init__(self,Nome:str,Idade:int,Cidade:str) -> None:
#         self.idade = Idade
#         self.nome = Nome
#         self.Cidade = Cidade

# Indentidade = Teste('Kaua',16,'Salvador')

# print(Indentidade.Cidade)
# print(Indentidade.idade)
# print(Indentidade.nome)

# Exercise

# class Dog():
#     def __init__(self,nome:str,raça:str,peso:float) -> None:
#         self.Nam = nome
#         self.raça = raça
#         self.pes = peso
#     def Eat_Dog(self):
#         print(f'Raça do Cachorro:{self.raça}')
#         print(f'Nome do Cachorro:{self.Nam}')
#         print(f'Peso do Cachorro:{self.pes}\n')
#         return 'Crock,Crock,Crock'
# class Cat():
#     def __init__(self,nome,raça,peso) -> None:
#         super.__init__(nome,raça)
#         self.nam = nome
#         self.ras = raça
#         self.pes = peso
#     def All_cat(self):
#         print(f'Nome do gato:{self.nam}')
#         print(f'Peso do gato:{self.pes}')
#         print(f'Raça do gato:{self.ras}')
#         return 'O gato quebrou alguma coisa'
    
# class Impor(Dog):
#     def __init__(self,Nome,Raça,peso) -> None:
#         super.__init__(Nome,Raça,peso)


# Choise_ = int(input('''Voce tem gato ou cachorro:
# [1] Dog
# [2] Cat
# ->'''))
# match Choise_:
#     case 1:    
# for Repetir in range(2):
#             Raça_Dog = input('Raça do Cachorro:')
#             Name_Dog = input('Nome do cachorro:')
#             Peso_Dog = float(input('Peso do Cachorro:'))
#             print('------------')

#             Atributos_Dog = Dog(Name_Dog,Raça_Dog,Peso_Dog)

#             Atributos_Dog.Eat_Dog()
#     # case 2:
# for Repetir in range(2):
#             Raça_Cat = input('Raça do Gato:')
#             Name_Cat = input('Nome do Gato:')
#             Peso_Cat = float(input('Peso do Gato:'))
#             print('---------------------------')
#             Atributos_Cat = Cat(Name_Cat,Raça_Cat,Peso_Cat)
#             Atributos_Cat.All_cat()   
#-------------------------------------------------------------------------------------

# Now a new thing,Super class
# He is use to you take things of Class father in other class

