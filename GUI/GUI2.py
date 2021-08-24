import tkinter as tk
from tkinter import Button, StringVar, OptionMenu
from classGUI2 import funções
from tkinter.constants import DISABLED

Janela = tk.Tk()

largura_App = 400
altura_App = 350

largura_Da_Tela = Janela.winfo_screenwidth()
altura_Da_Tela = Janela.winfo_screenheight()

posX = largura_Da_Tela/2 - largura_App/2
posY = altura_Da_Tela/2 - altura_App/2
Janela.title("Titulo")
Janela.geometry("%dx%d+%d+%d" % (largura_App, altura_App, posX, posY))
#   ----------------------------------------------------------------------  #


options = (-4, -3, -2, -1, 0, 1, 2, 3, 4)

ProVar = StringVar(Janela)
ProVar.set("ProVar")

ForVar = StringVar(Janela)
ForVar.set("Força")

CarVar = StringVar(Janela)
CarVar.set("Carisma")

ConstVar = StringVar(Janela)
ConstVar.set("Constituição")

InteVar = StringVar(Janela)
InteVar.set("Inteligência")

DexVar = StringVar(Janela)
DexVar.set("Destreza")

SabVar = StringVar(Janela)
SabVar.set("Sabedoria")


def FunPro(value):
    Pro.config(state=DISABLED)


Pro = OptionMenu(Janela, ProVar, *options, command=FunPro)
Pro.grid(row=1, column=1)

Força = OptionMenu(Janela, ForVar, *options)
Força.grid(row=2, column=1)

Carisma = OptionMenu(Janela, CarVar, *options)
Carisma.grid(row=3, column=1)

Constituição = OptionMenu(Janela, ConstVar, *options)
Constituição.grid(row=4, column=1)

Inteligência = OptionMenu(Janela, InteVar, *options)
Inteligência.grid(row=5, column=1)

Destreza = OptionMenu(Janela, DexVar, *options)
Destreza.grid(row=6, column=1)

Sabedoria = OptionMenu(Janela, SabVar, *options)
Sabedoria.grid(row=7, column=1)

i = funções(Janela, Força, Carisma, Constituição, Inteligência,
            Destreza, Sabedoria, ProVar, ForVar, CarVar, ConstVar, InteVar,
            DexVar, SabVar)

Listas = [("Força", i.função1, 2, 3),
          ("Carisma", i.função2, 3, 3),
          ("Constituição", i.função3, 4, 3),
          ("Inteligência", i.função4, 5, 3),
          ("Destreza", i.função5, 6, 3),
          ("Sabedoria", i.função6, 7, 3)]

for Texto, função, RC, CC in Listas:
    Botão1 = Button(Janela, text=Texto, command=função)
    Botão1.grid(row=RC, column=CC)

#   --------------------------------------------------------------------    #
Janela.mainloop()
