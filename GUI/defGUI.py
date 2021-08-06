import random
from tkinter import Label
from tkinter.constants import DISABLED


class Classe:

    def __init__(self, window, En_For, En_Car,
                 En_Const, En_Inte, En_Dex, En_Sab):
        self.window = window
        self.En_For = En_For
        self.En_Car = En_Car
        self.En_Const = En_Const
        self.En_Inte = En_Inte
        self.En_Dex = En_Dex
        self.En_Sab = En_Sab

    def Força(self):
        self.En_For.config(state=DISABLED)
        num = random.randint(1, 20)
        Entrada_For = int(self.En_For.get())
        Soma = (num + Entrada_For)
        Label(self.window,
              text=Soma).grid(row=1, column=4)

    def Carisma(self):
        self.En_Car.config(state=DISABLED)
        num = random.randint(1, 20)
        Entrada_Car = int(self.En_Car.get())
        Soma = (num + Entrada_Car)
        Label(self.window,
              text=Soma).grid(row=2, column=4)

    def Constituição(self):
        self.En_Const.config(state=DISABLED)
        num = random.randint(1, 20)
        Entrada_Const = int(self.En_Const.get())
        Soma = (num + Entrada_Const)
        Label(self.window,
              text=Soma).grid(row=3, column=4)

    def Inteligência(self):
        self.En_Inte.config(state=DISABLED)
        num = random.randint(1, 20)
        Entrada_Inte = int(self.En_Inte.get())
        Soma = (num + Entrada_Inte)
        Label(self.window,
              text=Soma).grid(row=4, column=4)

    def Destreza(self):
        self.En_Dex.config(state=DISABLED)
        num = random.randint(1, 20)
        Entrada_Dex = int(self.En_Dex.get())
        Soma = (num + Entrada_Dex)
        Label(self.window,
              text=Soma).grid(row=5, column=4)

    def Sabedoria(self):
        self.En_Sab.config(state=DISABLED)
        num = random.randint(1, 20)
        Entrada_Sab = int(self.En_Sab.get())
        Soma = (num + Entrada_Sab)
        Label(self.window,
              text=Soma).grid(row=6, column=4)
