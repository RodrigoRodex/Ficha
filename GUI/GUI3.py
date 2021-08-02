#   from class_GUi import Num_Entry
from tkinter import Button, Entry, Label, Tk
from tkinter.constants import DISABLED, W
import random


def callback(input):
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


window = Tk()
reg = window.register(callback)

largura_App = 400
altura_App = 350

largura_Da_Tela = window.winfo_screenwidth()
altura_Da_Tela = window.winfo_screenheight()

posX = largura_Da_Tela/2 - largura_App/2
posY = altura_Da_Tela/2 - altura_App/2

window.title("Titulo")
window.geometry("%dx%d+%d+%d" % (largura_App, altura_App, posX, posY))
#   isso faz o GUI aparecer no meio da tela

#   procurar como colocar uma lista e escolher o número
Label(window, text="Força:").grid(row=0, sticky=W)
En_For = Entry(window)
En_For.grid(row=0, column=1)
En_For.config(validate="key",
              validatecommand=(reg, '%P'))


def Força():
    En_For.config(state=DISABLED)
    #   o disable serve pra travar e não deixar a pessoa mudar o
    #   número das habilidades
    num = random.randint(1, 20)
    For_enntry = int(En_For.get())
    Soma = (num + For_enntry)
    Label(window, text=Soma).grid(row=0, column=2)


Button(window,
       text="Contar a Força",
       command=Força).grid(row=1, column=1)


Label(window, text="Carisma:").grid(row=2, sticky=W)
En_Car = Entry(window)
En_Car.grid(row=2, column=1)
En_Car.config(validate="key",
              validatecommand=(reg, '%P'))


def Carisma():
    En_Car.config(state=DISABLED)
    num = random.randint(1, 20)
    Car_Entry = int(En_Car.get())
    Soma = (num + Car_Entry)
    Label(window, text=Soma).grid(row=2, column=2)


Button(window,
       text="Contar o Carisma",
       command=Carisma).grid(row=3, column=1)

Label(window, text="Constituição:").grid(row=4, sticky=W)
En_Const = Entry(window)
En_Const.grid(row=4, column=1)
En_Const.config(validate="key",
                validatecommand=(reg, '%P'))


def Constituição():
    En_Const.config(state=DISABLED)
    num = random.randint(1, 20)
    Const_Entry = int(En_Const.get())
    Soma = (num + Const_Entry)
    Label(window,
          text=Soma).grid(row=4, column=2)


Button(window,
       text="Contar o Constituiçao",
       command=Constituição).grid(row=5, column=1)

Label(window, text="Inteligência:").grid(row=6, sticky=W)
En_Inte = Entry(window)
En_Inte.grid(row=6, column=1)
En_Inte.config(validate="key",
               validatecommand=(reg, '%P'))


def Inteligência():
    En_Inte.config(state=DISABLED)
    num = random.randint(1, 20)
    Inte_Entry = int(En_Inte.get())
    Soma = (Inte_Entry + num)
    Label(window,
          text=Soma).grid(row=6, column=2)


Button(window,
       text="Contar a Inteligência",
       command=Inteligência).grid(row=7, column=1)

#   ta falhando por causa do callback???
Label(window, text="Destreza:").grid(row=9, sticky=W)
En_Dex = Entry(window)
En_Dex.grid(row=9, column=1)
En_Dex.config(validate="key",
              validatecommand=(reg, '%P'))


def Destreza():
    En_Dex.config(state=DISABLED)
    num = random.randint(1, 20)
    Dex_Entry = int(En_Dex.get())
    Soma = (Dex_Entry + num)
    Label(window,
          text=Soma).grid(row=9, column=2)


Button(window,
       text="Contar a Destreza",
       command=Destreza).grid(row=10, column=1)


Label(window, text="Sabedoria:").grid(row=11, sticky=W)
En_Sab = Entry(window)
En_Sab.grid(row=11, column=1)
En_Sab.config(validate="key",
              validatecommand=(reg, '%P'))


def Sabedoria():
    En_Sab.config(state=(DISABLED))
    num = random.randint(1, 20)
    Sab_Entry = int(En_Sab.get())
    Soma = (Sab_Entry + num)
    Label(window,
          text=Soma).grid(row=11, column=2)


Button(window,
       text="Contar Sabedoria",
       command=Sabedoria).grid(row=12, column=1)
window.mainloop()
