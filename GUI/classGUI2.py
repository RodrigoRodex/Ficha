import random
from tkinter import Label
from tkinter.constants import DISABLED


class funções:

    def __init__(self,
                 root,
                 ForMenu,
                 CarMenu,
                 ConstMenu,
                 InteMenu,
                 DexMenu,
                 SabMenu,
                 ProVar,
                 ForVar,
                 CarVar,
                 ConstVar,
                 InteVar,
                 DexVar,
                 SabVar):
        self.Janela = root
        self.Força = ForMenu
        self.Carisma = CarMenu
        self.Constituição = ConstMenu
        self.Inteligência = InteMenu
        self.Destreza = DexMenu
        self.Sabedoria = SabMenu
        #  ta dando erro, option menu object has no attribute get
        self.ProVar = ProVar
        self.ForVar = ForVar
        self.CarVar = CarVar
        self.ConstVar = ConstVar
        self.InteVar = InteVar
        self.DexVar = DexVar
        self.SabVar = SabVar

    def função1(self):
        self.Força.config(state=DISABLED)
        num1 = int(self.ForVar.get())
        RNum1 = random.randint(1, 20)
        Prof = int(self.ProVar.get())
        Math1 = num1 + RNum1 + Prof
        print(Math1, num1, RNum1, Prof)
        if Math1 <= 0:
            MLF = Label(self.Janela, text=1)
            MLF.grid(row=2, column=2)
        else:
            MLF = Label(self.Janela, text=Math1)
            MLF.grid(row=2, column=2)

    def função2(self):
        self.Carisma.config(state=DISABLED)
        num2 = int(self.CarVar.get())
        RNum2 = random.randint(1, 20)
        Prof = int(self.ProVar.get())
        Math2 = num2 + RNum2 + Prof
        if Math2 <= 0:
            MLF2 = Label(self.Janela, text=1)
            MLF2.grid(row=3, column=2)
        else:
            MLF2 = Label(self.Janela, text=Math2)
            MLF2.grid(row=3, column=2)

    def função3(self):
        self.Constituição.config(state=DISABLED)
        num3 = int(self.ConstVar.get())
        RNum3 = random.randint(1, 20)
        Prof = int(self.ProVar.get())
        Math3 = num3 + RNum3 + Prof
        if Math3 <= 0:
            MLF3 = Label(self.Janela, text=1)
            MLF3.grid(row=4, column=2)
        else:
            MLF3 = Label(self.Janela, text=Math3)
            MLF3.grid(row=4, column=2)

    def função4(self):
        self.Inteligência.config(state=DISABLED)
        num4 = int(self.InteVar.get())
        RNum4 = random.randint(1, 20)
        Prof = int(self.ProVar.get())
        Math4 = num4 + RNum4 + Prof
        if Math4 <= 0:
            MLF4 = Label(self.Janela, text=1)
            MLF4.grid(row=5, column=2)
        else:
            MLF4 = Label(self.Janela, text=Math4)
            MLF4.grid(row=5, column=2)

    def função5(self):
        self.Destreza.config(state=DISABLED)
        num5 = int(self.DexVar.get())
        RNum5 = random.randint(1, 20)
        Prof = int(self.ProVar.get())
        Math5 = num5 + RNum5 + Prof
        if Math5 <= 0:
            MLF5 = Label(self.Janela, text=1)
            MLF5.grid(row=6, column=2)
        else:
            MLF5 = Label(self.Janela, text=Math5)
            MLF5.grid(row=6, column=2)

    def função6(self):
        self.Sabedoria.config(state=DISABLED)
        num6 = int(self.SabVar.get())
        RNum6 = random.randint(1, 20)
        Prof = int(self.ProVar.get())
        Math6 = num6 + RNum6 + Prof
        if Math6 <= 0:
            MLF6 = Label(self.Janela, text=1)
            MLF6.grid(row=7, column=2)
        else:
            MLF6 = Label(self.Janela, text=Math6)
            MLF6.grid(row=7, column=2)
