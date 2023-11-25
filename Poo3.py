# P.o.o lesson 3

# but one lesson of p.o.o

# Polimofismo : You can to change the fuction from class
# you heve what creat a class is late use super()
# To the polimofismo be use  the class need have same name

# Exercice

# class Car():
#     def __init__(self,Name_V,Motor,have_wheel) -> None:
#         # Car
#         self.Name = Name_V
#         self.Motor = Motor
#         self.wheel = have_wheel
#     def Buzina(self):
#         return 'Biiiii'
    

# class Barc(Car):
#     def __init__(self,Name_V,Motor,have_wheel) -> None:
#         super().__init__(Name_V,Motor,have_wheel)
#     def Buzina(self):
#         return 'Foooom'
        

# class airPlane(Car):
#     def __init__(self,Name_V,Motor,have_wheel) -> None:
#         super().__init__(Name_V,Motor,have_wheel)

#     def Buzina(self):
#         return ' Tem Buzina?'
    
# print('Qual e o Veiculo que deseja informar\n[1]CArro\n[2]Barco\n[3]Avião')
# Speak_to = int(input('->'))
# if Speak_to == 1:
#     name = input('Nome do veiculo:')
#     Motor = input('Nome do motor:')
#     wheel = input('Pinel:')
#     Carinho = Car(name,Motor,wheel)
#     Carinho.Buzina()
# elif Speak_to == 2:
#     name = input('Nome do veiculo:')
#     Motor = input('Nome do motor:')
#     wheel = input('Pinel:')
#     Barquinho = Barc(name,Motor,wheel)
#     Barquinho.Buzina()
# elif Speak_to == 3:
#     name = input('Nome do veiculo:')
#     Motor = input('Nome do motor:')
#     wheel = input('Pinel:')
#     Avinho = airPlane(name,Motor,wheel)
#     Avinho.Buzina()
#________________________________________________________________________________________ 
# See later that is a capusola of things
# class Funcionario:
#     def __init__(self, nome, cargo, valor_hora_trabalhada):
#         self.nome = nome
#         self.cargo = cargo
#         self.valor_hora_trabalhada = valor_hora_trabalhada
#         self.__horas_trabalhadas = 0
#         self.__salario = 0
    
#     def registrar_hora_trabalhada(self):
#         self.__horas_trabalhadas += 1
#         print("Hora registrada.")

#     def mostrar_horas_trabalhadas(self):
#         return self.__horas_trabalhadas

#     def calcular_salario(self):
#         self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
    
#     @property
#     def salario(self):
#         return self.__salario
    
#     @salario.setter
#     def salario(self, novo_salario):
#         raise ValueError("Impossível alterar o salário diretamente.")

# renan = Funcionario('Renan','Desenvolvedor',500)

# renan.salario = 35000
# print(renan.salario)


class Show_new():
    def __init__(self,Name_user,Name_show) -> None:
        self.Vip = Ingres_vip = 90
        self.Normal = Ingres_Normal = 10
        self.Cabin = Ingres_Cabin = 60
        self.Name = Name_user
        self.Show = Name_show
    

print(':Ingreços para o show:')
informat = input('Nome do Usuario:')
Name_show = input('Nome do Show:')
type_ingres = input('''Seu ingreso  e Camarote,Normal ou VIP?
[V]Vip - 90$
[C]Camarot - 30$
[N]Normal - 10$
->
''').upper()

class_Infort = Show_new(informat,Name_show)
