from tkinter import Button, OptionMenu, StringVar
from tkinter.constants import ACTIVE, DISABLED
from classFicha import funções2

#   ----------------------------------------------------------------------  #
#   Variaveis
#   classes
classes = ("Bárbaro", "Bardo", "Clérigo",
           "Druida", "Guerreiro", "Monge",
           "Paladino", "Patrulheiro", "Ladino",
           "Feiticeiro", "Bruxo", "Mago", "Artífice",
           "Caçador do Sangue")

#   pericias
Peri = ("Acrobacia", "Arcanismo", "Atletismo", "Atuação", "Blefar",
        "Furtividade", "Historia", "Intimidação", "Intuição",
        "Investigação", "Adestrar animais", "Medicina", "Natureza",
        "Percepção", "Persuasão", "Prestidigitação", "Religião",
        "Sobrevivência")

#   lista de sim e não de cada classe, para pericias
listaClas = [("Bárbaro", DISABLED, DISABLED, ACTIVE, DISABLED,
              DISABLED, DISABLED, DISABLED, ACTIVE, DISABLED, DISABLED,
              ACTIVE, DISABLED, ACTIVE, ACTIVE, DISABLED, DISABLED,
              DISABLED, ACTIVE),
             ("Bardo", ACTIVE, ACTIVE, ACTIVE, ACTIVE, ACTIVE,
             ACTIVE, ACTIVE, ACTIVE, ACTIVE, ACTIVE, ACTIVE, ACTIVE, ACTIVE,
             ACTIVE, ACTIVE, ACTIVE, ACTIVE, ACTIVE),
             ("Clérigo", DISABLED, DISABLED, DISABLED, DISABLED,
              DISABLED, DISABLED, ACTIVE, DISABLED, ACTIVE, DISABLED, DISABLED,
              ACTIVE, DISABLED, DISABLED, ACTIVE, DISABLED, ACTIVE, DISABLED),
             ("Druida", DISABLED, ACTIVE, DISABLED, DISABLED, DISABLED,
              DISABLED, DISABLED, DISABLED, ACTIVE, DISABLED, ACTIVE, ACTIVE,
              ACTIVE, ACTIVE, DISABLED, DISABLED, ACTIVE, ACTIVE),
             ("Guerreiro", ACTIVE, DISABLED, ACTIVE, DISABLED,
              DISABLED, DISABLED, ACTIVE, ACTIVE, ACTIVE, DISABLED,
              ACTIVE, DISABLED, DISABLED, ACTIVE, DISABLED, DISABLED,
              DISABLED, ACTIVE),
             ("Monge", ACTIVE, DISABLED, ACTIVE, DISABLED, DISABLED,
              ACTIVE, ACTIVE, DISABLED, ACTIVE, DISABLED, DISABLED, DISABLED,
              DISABLED, DISABLED, DISABLED, DISABLED, ACTIVE, DISABLED),
             ("Paladino", DISABLED, DISABLED, ACTIVE, DISABLED,
              DISABLED, DISABLED, DISABLED, ACTIVE, ACTIVE, DISABLED,
              DISABLED, ACTIVE, DISABLED, DISABLED, ACTIVE, DISABLED,
              ACTIVE, DISABLED),
             ("Patrulheiro", ACTIVE, DISABLED, ACTIVE, DISABLED,
              DISABLED, ACTIVE, DISABLED, DISABLED, ACTIVE, ACTIVE, ACTIVE,
              DISABLED, ACTIVE, ACTIVE, DISABLED, DISABLED, DISABLED, ACTIVE),
             ("Ladino", ACTIVE, DISABLED, ACTIVE, ACTIVE, ACTIVE,
              ACTIVE, DISABLED, ACTIVE, ACTIVE, ACTIVE, DISABLED, DISABLED,
              DISABLED, ACTIVE, ACTIVE, ACTIVE, DISABLED, DISABLED),
             ("Feiticeiro", DISABLED, ACTIVE, DISABLED, DISABLED,
             ACTIVE, DISABLED, DISABLED, ACTIVE, ACTIVE, DISABLED, DISABLED,
             DISABLED, DISABLED, DISABLED, ACTIVE, DISABLED, ACTIVE, DISABLED),
             ("Bruxo", DISABLED, ACTIVE, DISABLED, DISABLED, ACTIVE,
             DISABLED, ACTIVE, ACTIVE, DISABLED, ACTIVE, DISABLED, DISABLED,
             ACTIVE, DISABLED, DISABLED, DISABLED, ACTIVE, DISABLED),
             ("Mago", DISABLED, ACTIVE, DISABLED, DISABLED, DISABLED,
              DISABLED, ACTIVE, DISABLED, ACTIVE, ACTIVE, DISABLED, ACTIVE,
              DISABLED, DISABLED, DISABLED, DISABLED, ACTIVE, DISABLED),
             ("Caçador do Sangue", ACTIVE, ACTIVE, ACTIVE, DISABLED,
              DISABLED, DISABLED, ACTIVE, DISABLED, DISABLED, ACTIVE,
              DISABLED, DISABLED, DISABLED, ACTIVE, DISABLED, DISABLED,
              ACTIVE, ACTIVE)]

#   raças
raças = ("Anão", "Elfo", "Halfling",
         "Humano", "Draconato", "Gnomo",
         "Meio Orc", "Meio Elfo", "Tiefling")
#   ----------------------------------------------------------------------  #


class pericias:

    #   informações para essa classe
    def __init__(self,
                 root,
                 ClaVar,
                 RadVar1,
                 RadVar2,
                 RadVar3,
                 RadVar4,
                 RadVar5,
                 RadVar6,
                 RadVar7,
                 RadVar8,
                 RadVar9,
                 RadVar10,
                 RadVar11,
                 RadVar12,
                 RadVar13,
                 RadVar14,
                 RadVar15,
                 RadVar16,
                 RadVar17,
                 RadVar18,
                 RadRad1,
                 RadRad2,
                 RadRad3,
                 RadRad4,
                 RadRad5,
                 RadRad6,
                 RadRad7,
                 RadRad8,
                 RadRad9,
                 RadRad10,
                 RadRad11,
                 RadRad12,
                 RadRad13,
                 RadRad14,
                 RadRad15,
                 RadRad16,
                 RadRad17,
                 RadRad18,
                 ProVar,
                 ForVar,
                 CarVar,
                 InteVar,
                 ConstVar,
                 DexVar,
                 SabVar):
        self.Janela = root
        self.ClaVar = ClaVar
        self.RadVar1 = RadVar1
        self.RadVar2 = RadVar2
        self.RadVar3 = RadVar3
        self.RadVar4 = RadVar4
        self.RadVar5 = RadVar5
        self.RadVar6 = RadVar6
        self.RadVar7 = RadVar7
        self.RadVar8 = RadVar8
        self.RadVar9 = RadVar9
        self.RadVar10 = RadVar10
        self.RadVar11 = RadVar11
        self.RadVar12 = RadVar12
        self.RadVar13 = RadVar13
        self.RadVar14 = RadVar14
        self.RadVar15 = RadVar15
        self.RadVar16 = RadVar16
        self.RadVar17 = RadVar17
        self.RadVar18 = RadVar18
        self.RadRad1 = RadRad1
        self.RadRad2 = RadRad2
        self.RadRad3 = RadRad3
        self.RadRad4 = RadRad4
        self.RadRad5 = RadRad5
        self.RadRad6 = RadRad6
        self.RadRad7 = RadRad7
        self.RadRad8 = RadRad8
        self.RadRad9 = RadRad9
        self.RadRad10 = RadRad10
        self.RadRad11 = RadRad11
        self.RadRad12 = RadRad12
        self.RadRad13 = RadRad13
        self.RadRad14 = RadRad14
        self.RadRad15 = RadRad15
        self.RadRad16 = RadRad16
        self.RadRad17 = RadRad17
        self.RadRad18 = RadRad18
        self.ProVar = ProVar
        self.ForVar = ForVar
        self.CarVar = CarVar
        self.InteVar = InteVar
        self.ConstVar = ConstVar
        self.DexVar = DexVar
        self.SabVar = SabVar
        #   vari criadas em self
        self.Var = StringVar(self.Janela)
        self.Var.set("Pericias")
        self.Menus = [(self.RadVar1),
                      (self.RadVar2),
                      (self.RadVar3),
                      (self.RadVar4),
                      (self.RadVar5),
                      (self.RadVar6),
                      (self.RadVar7),
                      (self.RadVar8),
                      (self.RadVar9),
                      (self.RadVar10),
                      (self.RadVar11),
                      (self.RadVar12),
                      (self.RadVar13),
                      (self.RadVar14),
                      (self.RadVar15),
                      (self.RadVar16),
                      (self.RadVar17),
                      (self.RadVar18)]
        self.Varr = (self.RadVar1.get(), self.RadVar2.get(),
                     self.RadVar3.get(), self.RadVar4.get(),
                     self.RadVar5.get(), self.RadVar6.get(),
                     self.RadVar7.get(), self.RadVar8.get(),
                     self.RadVar9.get(), self.RadVar10.get(),
                     self.RadVar11.get(), self.RadVar12.get(),
                     self.RadVar13.get(), self.RadVar14.get(),
                     self.RadVar15.get(), self.RadVar16.get(),
                     self.RadVar17.get(), self.RadVar18.get())

    def cond(self):
        #   informações enviadas para outra classe
        a = funções2(self.Janela, self.Var, self.ProVar,
                     self.ForVar, self.CarVar, self.InteVar,
                     self.ConstVar, self.DexVar, self.SabVar,
                     self.RadVar1, self.RadVar2, self.RadVar3,
                     self.RadVar4, self.RadVar5, self.RadVar6,
                     self.RadVar7, self.RadVar8, self.RadVar9,
                     self.RadVar10, self.RadVar11, self.RadVar12,
                     self.RadVar13, self.RadVar14, self.RadVar15,
                     self.RadVar16, self.RadVar17, self.RadVar18)
        #   variavel para soma
        conta = 0
        #   for in para rodar para todos
        for Vari in self.Menus:
            #   verificar qual a classe
            if self.ClaVar.get() == "Bárbaro":
                #   verificar se a escolhida é True
                if Vari.get() is True:
                    #   se for True, soma 1 em conta
                    conta += 1
                    #   se conta bater certo número
                    if conta == 2:
                        #   cria um botão e um optionmenu
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        #   e bloqueia as que não foram escolhidas
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad8.config(state=DISABLED)
                        self.RadRad11.config(state=DISABLED)
                        self.RadRad13.config(state=DISABLED)
                        self.RadRad14.config(state=DISABLED)
                        self.RadRad18.config(state=DISABLED)
            elif self.ClaVar.get() == "Bardo":
                if Vari.get() is True:
                    conta += 1
                    if conta == 3:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad1.config(state=DISABLED)
                        self.RadRad2.config(state=DISABLED)
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad4.config(state=DISABLED)
                        self.RadRad5.config(state=DISABLED)
                        self.RadRad6.config(state=DISABLED)
                        self.RadRad7.config(state=DISABLED)
                        self.RadRad8.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad10.config(state=DISABLED)
                        self.RadRad11.config(state=DISABLED)
                        self.RadRad12.config(state=DISABLED)
                        self.RadRad13.config(state=DISABLED)
                        self.RadRad14.config(state=DISABLED)
                        self.RadRad15.config(state=DISABLED)
                        self.RadRad16.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
                        self.RadRad18.config(state=DISABLED)
            elif self.ClaVar.get() == "Clérigo":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad7.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad12.config(state=DISABLED)
                        self.RadRad15.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
            elif self.ClaVar.get() == "Druida":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad2.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad11.config(state=DISABLED)
                        self.RadRad12.config(state=DISABLED)
                        self.RadRad13.config(state=DISABLED)
                        self.RadRad14.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
                        self.RadRad18.config(state=DISABLED)
            elif self.ClaVar.get() == "Guerreiro":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad1.config(state=DISABLED)
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad7.config(state=DISABLED)
                        self.RadRad8.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad11.config(state=DISABLED)
                        self.RadRad14.config(state=DISABLED)
                        self.RadRad18.config(state=DISABLED)
            elif self.ClaVar.get() == "Monge":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad1.config(state=DISABLED)
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad6.config(state=DISABLED)
                        self.RadRad7.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
            elif self.ClaVar.get() == "Paladino":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad8.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad12.config(state=DISABLED)
                        self.RadRad15.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
            elif self.ClaVar.get() == "Patrulheiro":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad1.config(state=DISABLED)
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad6.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad10.config(state=DISABLED)
                        self.RadRad11.config(state=DISABLED)
                        self.RadRad13.config(state=DISABLED)
                        self.RadRad14.config(state=DISABLED)
                        self.RadRad18.config(state=DISABLED)
            elif self.ClaVar.get() == "Ladino":
                if Vari.get() is True:
                    conta += 1
                    if conta == 4:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad1.config(state=DISABLED)
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad4.config(state=DISABLED)
                        self.RadRad5.config(state=DISABLED)
                        self.RadRad6.config(state=DISABLED)
                        self.RadRad8.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad10.config(state=DISABLED)
                        self.RadRad14.config(state=DISABLED)
                        self.RadRad15.config(state=DISABLED)
                        self.RadRad16.config(state=DISABLED)
            elif self.ClaVar.get() == "Feiticeiro":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad2.config(state=DISABLED)
                        self.RadRad5.config(state=DISABLED)
                        self.RadRad8.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad15.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
            elif self.ClaVar.get() == "Bruxo":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad2.config(state=DISABLED)
                        self.RadRad5.config(state=DISABLED)
                        self.RadRad7.config(state=DISABLED)
                        self.RadRad8.config(state=DISABLED)
                        self.RadRad10.config(state=DISABLED)
                        self.RadRad13.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
            elif self.ClaVar.get() == "Mago":
                if Vari.get() is True:
                    conta += 1
                    if conta == 2:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad2.config(state=DISABLED)
                        self.RadRad7.config(state=DISABLED)
                        self.RadRad9.config(state=DISABLED)
                        self.RadRad10.config(state=DISABLED)
                        self.RadRad12.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
            elif self.ClaVar.get() == "Caçador do Sangue":
                if Vari.get() is True:
                    conta += 1
                    if conta == 3:
                        menu = OptionMenu(self.Janela, self.Var, *Peri)
                        menu.grid(row=4, column=5)
                        Bott = Button(self.Janela, text="Botão",
                                      command=a.teste)
                        Bott.grid(row=5, column=5)
                        self.RadRad1.config(state=DISABLED)
                        self.RadRad2.config(state=DISABLED)
                        self.RadRad3.config(state=DISABLED)
                        self.RadRad7.config(state=DISABLED)
                        self.RadRad10.config(state=DISABLED)
                        self.RadRad14.config(state=DISABLED)
                        self.RadRad17.config(state=DISABLED)
                        self.RadRad18.config(state=DISABLED)

    def fun(self, value):
        #   for in para armazenar a classe, e os sims e nãos de cada pericia
        #   de cada classe
        for (Classe, ST1, ST2, ST3, ST4, ST5, ST6, ST7, ST8, ST9, ST10,
             ST11, ST12, ST13, ST14, ST15, ST16, ST17, ST18) in listaClas:
            #  se a classe escolhida for igual a alguma classe, vai usar
            #  os sims e nãos daquela classe
            if self.ClaVar.get() == Classe:
                self.RadRad1.config(state=ST1)
                self.RadRad2.config(state=ST2)
                self.RadRad3.config(state=ST3)
                self.RadRad4.config(state=ST4)
                self.RadRad5.config(state=ST5)
                self.RadRad6.config(state=ST6)
                self.RadRad7.config(state=ST7)
                self.RadRad8.config(state=ST8)
                self.RadRad9.config(state=ST9)
                self.RadRad10.config(state=ST10)
                self.RadRad11.config(state=ST11)
                self.RadRad12.config(state=ST12)
                self.RadRad13.config(state=ST13)
                self.RadRad14.config(state=ST14)
                self.RadRad15.config(state=ST15)
                self.RadRad16.config(state=ST16)
                self.RadRad17.config(state=ST17)
                self.RadRad18.config(state=ST18)
