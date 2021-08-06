from tkinter import Button, Entry, Label, Tk
from defGUI import Classe


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

c = Classe(Janela, En_For, En_Car,
           En_Const, En_Inte, En_Dex, En_Sab)
reg = Janela.register(volta)

Text_For = "Contar a Força"
Text_Car = "Contar o Carisma"
Text_Const = "Contar a Constituição"
Text_Inte = "Contar a Inteligência"
Text_Dex = "Contar a Destreza"
Text_Sab = "Contar a Sabedoria"


Atributos = [("Força:", En_For, 1, 1, 1, 2),
             ("Carisma:", En_Car, 2, 1, 2, 2),
             ("Constituição:", En_Const, 3, 1, 3, 2),
             ("Inteligência:", En_Inte, 4, 1, 4, 2),
             ("Destreza:", En_Dex, 5, 1, 5, 2),
             ("Sabedoria:", En_Sab, 6, 1, 6, 2)]

valores = [(1, 3, Text_For, c.Força),
           (2, 3, Text_Car, c.Carisma),
           (3, 3, Text_Const, c.Constituição),
           (4, 3, Text_Inte, c.Inteligência),
           (5, 3, Text_Dex, c.Destreza),
           (6, 3, Text_Sab, c.Sabedoria)]

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
