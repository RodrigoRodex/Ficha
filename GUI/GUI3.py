from tkinter import Button, Entry, Label, Tk
from tkinter.constants import DISABLED
import random


def volta(input):
    #   isdigit conta -, +, *, /, então não da pra colocar nas Entrys
    if input.isdigit():
        print(input)
        return True

    elif input == "":
        print(input)
        return True

    else:
        print(input)
        return False


Janela = Tk()

reg = Janela.register(volta)
largura_App = 400
altura_App = 350

largura_Da_Tela = Janela.winfo_screenwidth()
altura_Da_Tela = Janela.winfo_screenheight()

posX = largura_Da_Tela/2 - largura_App/2
posY = altura_Da_Tela/2 - altura_App/2

Janela.title("Titulo")
Janela.geometry("%dx%d+%d+%d" % (largura_App, altura_App, posX, posY))

En_For = Entry(Janela)
En_Car = Entry(Janela)
En_Const = Entry(Janela)
En_Inte = Entry(Janela)
En_Dex = Entry(Janela)
En_Sab = Entry(Janela)

Text_For = "Contar a Força"
Text_Car = "Contar o Carisma"
Text_Const = "Contar a Constituição"
Text_Inte = "Contar a Inteligência"
Text_Dex = "Contar a Destreza"
Text_Sab = "Contar a Sabedoria"


def Força():
    En_For.config(state=DISABLED)
    num = random.randint(1, 20)
    Entrada_For = int(En_For.get())
    Soma = (num + Entrada_For)
    Label(Janela,
          text=Soma).grid(row=1, column=4)


def Carisma():
    En_Car.config(state=DISABLED)
    num = random.randint(1, 20)
    Entrada_Car = int(En_Car.get())
    Soma = (num + Entrada_Car)
    Label(Janela,
          text=Soma).grid(row=2, column=4)


def Constituição():
    En_Const.config(state=DISABLED)
    num = random.randint(1, 20)
    Entrada_Const = int(En_Const.get())
    Soma = (num + Entrada_Const)
    Label(Janela,
          text=Soma).grid(row=3, column=4)


def Inteligência():
    En_Inte.config(state=DISABLED)
    num = random.randint(1, 20)
    Entrada_Inte = int(En_Inte.get())
    Soma = (num + Entrada_Inte)
    Label(Janela,
          text=Soma).grid(row=4, column=4)


def Destreza():
    En_Dex.config(state=DISABLED)
    num = random.randint(1, 20)
    Entrada_Dex = int(En_Dex.get())
    Soma = (num + Entrada_Dex)
    Label(Janela,
          text=Soma).grid(row=5, column=4)


def Sabedoria():
    En_Sab.config(state=DISABLED)
    num = random.randint(1, 20)
    Entrada_Sab = int(En_Sab.get())
    Soma = (num + Entrada_Sab)
    Label(Janela,
          text=Soma).grid(row=6, column=4)


Atributos = [("Força:", En_For, 1, 1, 1, 2),
             ("Carisma:", En_Car, 2, 1, 2, 2),
             ("Constituição:", En_Const, 3, 1, 3, 2),
             ("Inteligência:", En_Inte, 4, 1, 4, 2),
             ("Destreza:", En_Dex, 5, 1, 5, 2),
             ("Sabedoria:", En_Sab, 6, 1, 6, 2)]

valores = [(1, 3, Text_For, Força),
           (2, 3, Text_Car, Carisma),
           (3, 3, Text_Const, Constituição),
           (4, 3, Text_Inte, Inteligência),
           (5, 3, Text_Dex, Destreza),
           (6, 3, Text_Sab, Sabedoria)]

for name, En_name, r_val, c_val, r_val2, c_val2 in Atributos:
    Label(Janela,
          text=name,
          padx=20).grid(row=r_val, column=c_val)
    En_name.config(validate="key",
                   validatecommand=(reg, '%P'))
    En_name.grid(row=r_val2, column=c_val2)

for r_val3, c_val3, Texto, fun in valores:
    Button(Janela,
           text=Texto,
           command=fun).grid(row=r_val3, column=c_val3)

Janela.mainloop()
