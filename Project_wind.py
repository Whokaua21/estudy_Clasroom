# Cadastro do usuario 
from tkinter import Tk, mainloop,ttk,messagebox,Checkbutton,IntVar
from tkinter import *
from Color import *

#Janela do cadastro
Windos_tk = Tk()
Windos_tk.title('Cadastro')
Windos_tk.geometry('310x300')
Windos_tk.resizable(width=False,height=False)

#Dividindo a tela
Frame_up = Frame(
    Windos_tk,
    width=310,
    height=50,
    bg=cor1,
    relief='flat'
)
Frame_up.grid(row=0,column=0,padx=0,sticky=NSEW)

#Frame de baixo
Frame_donw = Frame(
    Windos_tk,
    width=310,
    height=250,
    bg= cor1,
    relief='flat'
)
Frame_donw.grid(row=1,column=0,pady=0,sticky=NSEW)
#Colocando elementos np Frame_up
l_nome = Label(
    Frame_up,
    text='Login',
    font=('Ivy 25'),
    bg=cor1,
    fg=cor4
)
l_nome.place(x=5,y=5)

l_row = Label(
    Frame_up,
    text='',
    width=275,
    font=('Ivy 25'),
    bg=cor2,
    fg=cor4,
)
l_row.place(x=10,y=45)

l_usurio = Label(
    Frame_donw,
    text='Usuario *',
    font=('ivy 14'),
    bg=cor1,
    fg=cor4,
)
l_usurio.place(x=10,y=20)
#Entrada de texto

e_nome = Entry(
    Frame_donw,
    width=25,
    justify='left',
    font=('',15),
    highlightthickness=1,
    relief='solid'
)
e_nome.place(x=14,y=50)

#Senha do casdastro
l_senha = Label(
    Frame_donw,
    text='Senha*',
    font=('Ivy 14'),
    bg=cor1,
    fg=cor4,
)
l_senha.place(x=10,y=95)

e_senha = Entry(
    Frame_donw,
    show='*',
    width=25,
    justify='left',
    font=('',15),
    highlightthickness=1,
    relief='solid'
)
e_senha.place(x=14,y=130)
def Checar_usuario():
    nome_digit = e_nome.get()
    Senha_digit = e_senha.get()
    
    if nome_digit in credencias.keys():
        Senha_Armazem = credencias[nome_digit]
        if Senha_digit == Senha_Armazem:
            messagebox.showinfo(title='Bem vindo',message='Logado com suceso')
        else:
            messagebox.showerror(title='Erro',message='Usuario ou senha')
    else:
            messagebox.showerror(title='Erro',message='Usuario ou senha errado')
#Botao de cadastro
def Cadastra_usuo():
    nome_digit = e_nome.get()
    Senha_digit = e_senha.get()
    
    if nome_digit in credencias.keys():
        messagebox.showerror(title='Erro',message='Usuario ja cadastrado')
    else:
        messagebox.showinfo(title='Cadastrado',message='Usuario ja cadastrado')
        credencias[nome_digit] = Senha_digit
        with open('credencias.txt','w') as file:
             file.write(f'{credencias}')

b_cadastro = Button(
    Frame_donw,
    text='Cadastrar',
    width=39,
    height=2,
    font=('ivy 8 bold'),
    bg=cor2,
    fg=cor1,
    relief='raised',
    command=Cadastra_usuo
)
b_cadastro.place(x=15,y=165)


b_cadastro = Button(
    Frame_donw,
    text='Logar',
    width=39,
    height=2,
    font=('ivy 8 bold'),
    bg=cor2,
    fg=cor1,
    relief='raised',
    command=Checar_usuario
)
b_cadastro.place(x=15,y=205)

credencias = {'Admin':'0000'}

if __name__ == '__main__':
    mainloop()