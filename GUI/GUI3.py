from class_GUi import Num_Entry
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

largura_App = 250
altura_App = 150

largura_Da_Tela = window.winfo_screenwidth()
altura_Da_Tela = window.winfo_screenheight()

posX = largura_Da_Tela/2 - largura_App/2
posY = altura_Da_Tela/2 - altura_App/2

window.title("Titulo")
window.geometry("%dx%d+%d+%d" % (largura_App, altura_App, posX, posY))
#   isso faz o GUI aparecer no meio da tela

#   procurar como colocar uma lista e escolher o número
Label(window, text="Força:").grid(row=0, sticky=W)
En = Entry(window)
En.grid(row=0, column=1)
#   o resto das labels estão no GUI1


reg = window.register(callback)
En.config(validate="key",
          validatecommand=(reg, '%P'))

For_enntry = int(En.get())

Num = Num_Entry(For_enntry)


def comando():
    #   En.config(state=DISABLED)
    #   o disable serve pra travar e não deixar a pessoa mudar o
    #   número das habilidades
    num = random.randint(1, 20)


Button(window, text="Contar", command=Num.soma).grid(row=1, column=1)

window.mainloop()
