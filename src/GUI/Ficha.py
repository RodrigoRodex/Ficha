import tkinter as tk
from tkinter import Button, Label, StringVar, OptionMenu, Entry
from tkinter import Radiobutton, BooleanVar
from classFicha import funções
from periciaisGUi3 import pericias
from tkinter.constants import DISABLED

#   ----------------------------------------------------------------------  #
#   Como a Janela vai ficar
Janela = tk.Tk()

largura_App = 600
altura_App = 550

largura_Da_Tela = Janela.winfo_screenwidth()
altura_Da_Tela = Janela.winfo_screenheight()

posX = largura_Da_Tela/2 - largura_App/2
posY = altura_Da_Tela/2 - altura_App/2
Janela.title("Titulo")
Janela.geometry("%dx%d+%d+%d" % (largura_App, altura_App, posX, posY))
#   essa conta faz o GUI ficar exatamente no meio da tela
#   ----------------------------------------------------------------------  #

#   ----------------------------------------------------------------------  #
#   valores dos atributos
options = ("4", "3", "2", "1", "0", "-1", "-2", "-3", "-4")

lvl = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
       "11", "12", "13", "14", "15", "16", "17", "18",
       "19", "20")

classes = ("Bárbaro", "Bardo", "Clérigo",
           "Druida", "Guerreiro", "Monge",
           "Paladino", "Patrulheiro", "Ladino",
           "Feiticeiro", "Bruxo", "Mago",
           "Caçador do Sangue")

raças = ("Anão", "Elfo", "Halfling",
         "Humano", "Draconato", "Gnomo",
         "Meio Orc", "Meio Elfo", "Tiefling")


#   função pra bloquear o lvl quando ele for escolhido
def FunPro(value):
    Pro.config(state=DISABLED)


#   As Vars dos RadioButtons e dos OptionsMenus
#   Classe e Raça
ClaVar = StringVar(Janela)
ClaVar.set("Classe")
RaVar = StringVar(Janela)
RaVar.set("Raça")

#   proficiência e atributos
ProVar = StringVar(Janela)
ForVar = StringVar(Janela)
CarVar = StringVar(Janela)
ConstVar = StringVar(Janela)
InteVar = StringVar(Janela)
DexVar = StringVar(Janela)
SabVar = StringVar(Janela)

#   Pericias
RadVar1 = BooleanVar(Janela)
RadVar2 = BooleanVar(Janela)
RadVar3 = BooleanVar(Janela)
RadVar4 = BooleanVar(Janela)
RadVar5 = BooleanVar(Janela)
RadVar6 = BooleanVar(Janela)
RadVar7 = BooleanVar(Janela)
RadVar8 = BooleanVar(Janela)
RadVar9 = BooleanVar(Janela)
RadVar10 = BooleanVar(Janela)
RadVar11 = BooleanVar(Janela)
RadVar12 = BooleanVar(Janela)
RadVar13 = BooleanVar(Janela)
RadVar14 = BooleanVar(Janela)
RadVar15 = BooleanVar(Janela)
RadVar16 = BooleanVar(Janela)
RadVar17 = BooleanVar(Janela)
RadVar18 = BooleanVar(Janela)

#   RadioButton de cada Pericia
RadRad1 = Radiobutton(Janela,
                      text="Acrobacia",
                      variable=RadVar1,
                      value=True)
RadRad1.grid(row=11, column=1)
RadRad2 = Radiobutton(Janela,
                      text="Arcanismo",
                      variable=RadVar2,
                      value=True)
RadRad2.grid(row=12, column=1)
RadRad3 = Radiobutton(Janela,
                      text="Atletismo",
                      variable=RadVar3,
                      value=True)
RadRad3.grid(row=13, column=1)
RadRad4 = Radiobutton(Janela,
                      text="Atuação",
                      variable=RadVar4,
                      value=True)
RadRad4.grid(row=14, column=1)
RadRad5 = Radiobutton(Janela,
                      text="Blefar",
                      variable=RadVar5,
                      value=True)
RadRad5.grid(row=15, column=1)
RadRad6 = Radiobutton(Janela,
                      text="Furtividade",
                      variable=RadVar6,
                      value=True)
RadRad6.grid(row=16, column=1)
RadRad7 = Radiobutton(Janela,
                      text="História",
                      variable=RadVar7,
                      value=True)
RadRad7.grid(row=11, column=2)
RadRad8 = Radiobutton(Janela,
                      text="Intimidação",
                      variable=RadVar8,
                      value=True)
RadRad8.grid(row=12, column=2)
RadRad9 = Radiobutton(Janela,
                      text="Intuição",
                      variable=RadVar9,
                      value=True)
RadRad9.grid(row=13, column=2)
RadRad10 = Radiobutton(Janela,
                       text="Investigação",
                       variable=RadVar10,
                       value=True)
RadRad10.grid(row=14, column=2)
RadRad11 = Radiobutton(Janela,
                       text="Adestrar Animais",
                       variable=RadVar11,
                       value=True)
RadRad11.grid(row=15, column=2)
RadRad12 = Radiobutton(Janela,
                       text="Medicina",
                       variable=RadVar12,
                       value=True)
RadRad12.grid(row=16, column=2)
RadRad13 = Radiobutton(Janela,
                       text="Natureza",
                       variable=RadVar13,
                       value=True)
RadRad13.grid(row=11, column=3)
RadRad14 = Radiobutton(Janela,
                       text="Percepção",
                       variable=RadVar14,
                       value=True)
RadRad14.grid(row=12, column=3)
RadRad15 = Radiobutton(Janela,
                       text="Persuasão",
                       variable=RadVar15,
                       value=True)
RadRad15.grid(row=13, column=3)
RadRad16 = Radiobutton(Janela,
                       text="Prestidigitação",
                       variable=RadVar16,
                       value=True)
RadRad16.grid(row=14, column=3)
RadRad17 = Radiobutton(Janela,
                       text="Religião",
                       variable=RadVar17,
                       value=True)
RadRad17.grid(row=15, column=3)
RadRad18 = Radiobutton(Janela,
                       text="Sobrevivência",
                       variable=RadVar18,
                       value=True)
RadRad18.grid(row=16, column=3)

#   deixar todas setadas como bloqueadas antes de escolher a classe

if ClaVar.get() not in classes:
    RadRad1.config(state=DISABLED)
    RadRad2.config(state=DISABLED)
    RadRad3.config(state=DISABLED)
    RadRad4.config(state=DISABLED)
    RadRad5.config(state=DISABLED)
    RadRad6.config(state=DISABLED)
    RadRad7.config(state=DISABLED)
    RadRad8.config(state=DISABLED)
    RadRad9.config(state=DISABLED)
    RadRad10.config(state=DISABLED)
    RadRad11.config(state=DISABLED)
    RadRad12.config(state=DISABLED)
    RadRad13.config(state=DISABLED)
    RadRad14.config(state=DISABLED)
    RadRad15.config(state=DISABLED)
    RadRad16.config(state=DISABLED)
    RadRad17.config(state=DISABLED)
    RadRad18.config(state=DISABLED)

#   enviando as informações para a Classe
p = pericias(Janela, ClaVar, RadVar1, RadVar2, RadVar3, RadVar4,
             RadVar5, RadVar6, RadVar7, RadVar8, RadVar9, RadVar10,
             RadVar11, RadVar12, RadVar13, RadVar14, RadVar15,
             RadVar16, RadVar17, RadVar18, RadRad1, RadRad2, RadRad3, RadRad4,
             RadRad5, RadRad6, RadRad7, RadRad8, RadRad9, RadRad10,
             RadRad11, RadRad12, RadRad13, RadRad14, RadRad15, RadRad16,
             RadRad17, RadRad18, ProVar, ForVar, CarVar, InteVar,
             ConstVar, DexVar, SabVar)

#   configurando todas as pericias com a função da Classe pericias
RadRad1.config(command=p.cond)
RadRad2.config(command=p.cond)
RadRad3.config(command=p.cond)
RadRad4.config(command=p.cond)
RadRad5.config(command=p.cond)
RadRad6.config(command=p.cond)
RadRad7.config(command=p.cond)
RadRad8.config(command=p.cond)
RadRad9.config(command=p.cond)
RadRad10.config(command=p.cond)
RadRad11.config(command=p.cond)
RadRad12.config(command=p.cond)
RadRad13.config(command=p.cond)
RadRad14.config(command=p.cond)
RadRad15.config(command=p.cond)
RadRad16.config(command=p.cond)
RadRad17.config(command=p.cond)
RadRad18.config(command=p.cond)

#   nome do personagem, classe e raça
NameEntry = Entry(Janela)
NameEntry.grid(row=1, column=4)

#   lembrar de colocar uma função para travar a escolha depois de escolher
ClaMenu = OptionMenu(Janela, ClaVar, *classes, command=p.fun)
ClaMenu.grid(row=1, column=5)

#   proficiência
ProVar.set("Nível")
Pro = OptionMenu(Janela, ProVar, *lvl, command=FunPro)
Pro.grid(row=1, column=1)

#   labels
Label(Janela, text="Atributos").grid(row=2, column=1)
Label(Janela, text="Pericias").grid(row=10, column=1)

#   atributos
ForVar.set("Força")
Força = OptionMenu(Janela, ForVar, *options)
Força.grid(row=3, column=1)

CarVar.set("Carisma")
Carisma = OptionMenu(Janela, CarVar, *options)
Carisma.grid(row=4, column=1)

ConstVar.set("Constituição")
Constituição = OptionMenu(Janela, ConstVar, *options)
Constituição.grid(row=5, column=1)

InteVar.set("Inteligência")
Inteligência = OptionMenu(Janela, InteVar, *options)
Inteligência.grid(row=6, column=1)

DexVar.set("Destreza")
Destreza = OptionMenu(Janela, DexVar, *options)
Destreza.grid(row=7, column=1)

SabVar.set("Sabedoria")
Sabedoria = OptionMenu(Janela, SabVar, *options)
Sabedoria.grid(row=8, column=1)

#   informações para a classe funções
i = funções(Janela, Força, Carisma, Constituição, Inteligência,
            Destreza, Sabedoria, ProVar, ForVar, CarVar, ConstVar, InteVar,
            DexVar, SabVar, ClaVar, RaVar)
#   OptionMenu de raça, com a função de funções
RaMenu = OptionMenu(Janela, RaVar, *raças, command=i.subclafun)
RaMenu.grid(row=2, column=5)

#   lista pro for in
Listas = [("Força", i.ConFor, 3, 3),
          ("Carisma", i.ConCar, 4, 3),
          ("Constituição", i.ConConst, 5, 3),
          ("Inteligência", i.ConInte, 6, 3),
          ("Destreza", i.ConDex, 7, 3),
          ("Sabedoria", i.ConSab, 8, 3)]

#   botões para calcular os atributos
for Texto, função, RC, CC in Listas:
    Botão1 = Button(Janela, text=Texto, command=função)
    Botão1.grid(row=RC, column=CC)

#   --------------------------------------------------------------------    #
Janela.mainloop()
