import random
from tkinter import Label
from tkinter.constants import DISABLED
from tkinter import StringVar, OptionMenu

#   ----------------------------------------------------------------------  #
#   Variaveis pra usar na classe
#   Lvl pra ver qual o lvl que a pessoa escolheu e entregar a proficiência
Lvl_Baixo = (1, 2, 3, 4)
Lvl_Medio = (5, 6, 7, 8)
Lvl_Alto = (9, 10, 11, 12)
Lvl_Muito_Alto = (13, 14, 15, 16)
LVl_Divindade = (17, 18, 19, 20)

#   para conferir se o atributo foi escolhido
options = ("-4", "-3", "-2", "-1", "0", "1", "2", "3", "4")

#   conferir se foi escolhido
lvl = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
       "11", "12", "13", "14", "15", "16", "17", "18",
       "19", "20")

#   conferir se foi escolhido
classes = ("Bárbaro", "Bardo", "Clérigo",
           "Druida", "Guerreiro", "Monge",
           "Paladino", "Patrulheiro", "Ladino",
           "Feiticeiro", "Bruxo", "Mago",
           "Caçador do Sangue")

#   conferir qual tipo de classe foi pega
classFor = ("Bárbaro", "Guerreiro", "Monge", "Patrulheiro")
classCar = ("Bardo", "Bruxo", "Clérigo", "Feiticeiro", "Paladino")
classConst = ("Bárbaro", "Feiticeiro", "Guerreiro")
classInte = ("Druida", "Ladino", "Mago")
classDex = ("Bardo", "Ladino", "Monge", "Patrulheiro")
classSab = ("Paladino", "Mago", "Clérigo", "Bruxo", "Druida", "Feiticeiro")

#   conferir a raça escolhida
raças = ("Anão", "Elfo", "Halfling",
         "Humano", "Draconato", "Gnomo",
         "Meio Orc", "Meio Elfo", "Tiefling")

#   conferir a sub raça
SCA = ("Anão da Colina", "Anão da Montanha")
SCE = ("Alto Elfo", "Elfo da Floresta", "Drow")
SCH = ("Pés Leves", "Robustos")
SCG = ("Gnomo das Florestas", "Gnomo das Rochas")
#   ----------------------------------------------------------------------  #


class funções2:

    #   informações que vão ser utilizadas dentro da classe
    def __init__(self,
                 Janela,
                 Var,
                 ProVar,
                 ForVar,
                 CarVar,
                 InteVar,
                 ConstVar,
                 DexVar,
                 SabVar,
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
                 RadVar18):
        self.Janela = Janela
        self.Var = Var
        self.ProVar = ProVar
        self.ForVar = ForVar
        self.CarVar = CarVar
        self.InteVar = InteVar
        self.ConstVar = ConstVar
        self.DexVar = DexVar
        self.SabVar = SabVar
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

    #   função da classe
    def teste(self):
        #   verificando a Proficiência está em lvl
        if self.ProVar.get() in lvl:
            #   verificando qual é a escolhida/ps: talvez tenha como
            #   diminuir essa parte fazendo um for in
            if self.Var.get() == "Acrobacia":
                #   se a escolhida for igual, vai conferir se ela é True
                #   se ela foi selecionada
                if self.RadVar1.get() is True:
                    #   se ela tiver sido selecionada, vai pegar o atributo
                    #   e ver se ele foi escolhido
                    if self.DexVar.get() in options:
                        #   Se ele tiver sido escolhido
                        #   vai pegar o atributo, transformar em int
                        numP = int(self.DexVar.get())
                        #   Vai gerar um número aleatório de 1 a 20(Toda vez
                        #   que o botão for clicado)
                        RPNum1 = random.randint(1, 20)
                        #   Vai pegar a proficiência e transformar em int
                        Prof = int(self.ProVar.get())
                        #   vai verificar qual foi o lvl e transformar
                        #   na proficiência
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        #   somando
                        MathP1 = numP + RPNum1 + ProLvl
                        #   verificando para não dar um número menor ou
                        #   igual a zero
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    #   Se o atributo não estiver lá, vai retornar nada
                    else:
                        return None
                #   Se a pericia não tiver sido selicionada
                else:
                    #   Verificando o atributo, mesmo procedimento de antes
                    if self.DexVar.get() in options:
                        numP = int(self.DexVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
            #   Se não tiver sido a primeira pericia, vai testar nas outras
            elif self.Var.get() == "Arcanismo":
                if self.RadVar2.get() is True:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Atletismo":
                if self.RadVar3.get() is True:
                    if self.ForVar.get() in options:
                        numP = int(self.ForVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.ForVar.get() in options:
                        numP = int(self.ForVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Atuação":
                if self.RadVar4.get() is True:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Blefar":
                if self.RadVar5.get() is True:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Furtividade":
                if self.RadVar6.get() is True:
                    if self.DexVar.get() in options:
                        numP = int(self.DexVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.DexVar.get() in options:
                        numP = int(self.DexVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Historia":
                if self.RadVar7.get() is True:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Intimidação":
                if self.RadVar8.get() is True:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Intuição":
                if self.RadVar9.get() is True:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Investigação":
                if self.RadVar10.get() is True:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Adestrar animais":
                if self.RadVar11.get() is True:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Medicina":
                if self.RadVar12.get() is True:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Natureza":
                if self.RadVar13.get() is True:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Percepção":
                if self.RadVar14.get() is True:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Persuasão":
                if self.RadVar15.get() is True:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.CarVar.get() in options:
                        numP = int(self.CarVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Prestidigitação":
                if self.RadVar16.get() is True:
                    if self.DexVar.get() in options:
                        numP = int(self.DexVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.DexVar.get() in options:
                        numP = int(self.DexVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Religião":
                if self.RadVar17.get() is True:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.InteVar.get() in options:
                        numP = int(self.InteVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None

            elif self.Var.get() == "Sobrevivência":
                if self.RadVar18.get() is True:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        MathP1 = numP + RPNum1 + ProLvl
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
                else:
                    if self.SabVar.get() in options:
                        numP = int(self.SabVar.get())
                        RPNum1 = random.randint(1, 20)
                        MathP1 = numP + RPNum1
                        if MathP1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=6, column=5)
                        else:
                            MLF = Label(self.Janela, text=MathP1)
                            MLF.grid(row=6, column=5)
                    else:
                        return None
        else:
            return None


class funções:

    #   colacando as informações que essa classe vai precisar
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
                 SabVar,
                 ClaVar,
                 RaVar):
        self.Janela = root
        self.Força = ForMenu
        self.Carisma = CarMenu
        self.Constituição = ConstMenu
        self.Inteligência = InteMenu
        self.Destreza = DexMenu
        self.Sabedoria = SabMenu
        self.ProVar = ProVar
        self.ForVar = ForVar
        self.CarVar = CarVar
        self.ConstVar = ConstVar
        self.InteVar = InteVar
        self.DexVar = DexVar
        self.SabVar = SabVar
        self.ClaVar = ClaVar
        self.RaVar = RaVar
        #   fazendo uma Var em self
        self.SubClaVar = StringVar(self.Janela)
        self.SubClaVar.set("Sub-Raça")

    def ConFor(self):
        #   verificando se a raça foi escolhida
        if self.RaVar.get() in raças:
            #   Verificando se a classe foi escolhida
            if self.ClaVar.get() in classes:
                #   Verificando se a classe é de força
                if self.ClaVar.get() in classFor:
                    #   Se ela for, vai verificar se o lvl foi escolhido
                    if self.ProVar.get() in lvl:
                        #   se sim, vai verificar se tem atributo Força
                        if self.ForVar.get() in options:
                            #   vai bloquear a mudança do atributo força
                            self.Força.config(state=DISABLED)
                            #   pegar o atributo e transformar em int
                            num1 = int(self.ForVar.get())
                            #   vai verificar se tem sub-raça e qual
                            if self.SubClaVar.get() == "Anão da Montanha":
                                #   somando se a que tiver for essa
                                num1 += 2
                            elif self.RaVar.get() == ("Draconato" or
                                                      "Meio-Orc"):
                                num1 += 2
                            elif self.RaVar.get() == "Humano":
                                num1 += 1
                            #   gerando um número aleatório
                            RNum1 = random.randint(1, 20)
                            #   pegando o lvl e transoformando em proficiência
                            Prof = int(self.ProVar.get())
                            if Prof in Lvl_Baixo:
                                ProLvl = 2
                            elif Prof in Lvl_Medio:
                                ProLvl = 3
                            elif Prof in Lvl_Alto:
                                ProLvl = 4
                            elif Prof in Lvl_Muito_Alto:
                                ProLvl = 5
                            elif Prof in LVl_Divindade:
                                ProLvl = 6
                            #   somando
                            Math1 = num1 + RNum1 + ProLvl
                            #   print pra testar se a conta ta saindo certo
                            print(Math1, num1, RNum1, ProLvl)
                            #   verificando se o número é menor ou igual a zero
                            if Math1 <= 0:
                                MLF = Label(self.Janela, text=1)
                                MLF.grid(row=3, column=2)
                            else:
                                MLF = Label(self.Janela, text=Math1)
                                MLF.grid(row=3, column=2)
                        #   Se o atributo tiver sido escolhido, vai retornar
                        #   nada
                        else:
                            return None
                    #   Se o lvl não tiver sido escolhido, vai retornar nada
                    else:
                        return None
                #   Se a classe não for uma classe for Força
                else:
                    #   Mesmo procedimento de antes
                    if self.ForVar.get() in options:
                        self.Força.config(state=DISABLED)
                        num1 = int(self.ForVar.get())
                        if self.SubClaVar.get() == "Anão da Montanha":
                            num1 += 2
                        elif self.RaVar.get() == ("Draconato" or
                                                  "Meio-Orc"):
                            num1 += 2
                        elif self.RaVar.get() == "Humano":
                            num1 += 1
                        RNum1 = random.randint(1, 20)
                        Math1 = num1 + RNum1
                        print(Math1, num1, RNum1)
                        if Math1 <= 0:
                            MLF = Label(self.Janela, text=1)
                            MLF.grid(row=3, column=2)
                        else:
                            MLF = Label(self.Janela, text=Math1)
                            MLF.grid(row=3, column=2)
                    else:
                        return None
            #   Se a classe não tiver sido escolhida
            else:
                return None
        #   Se a raça não tiver sido escolhida
        else:
            return None

    def ConCar(self):
        if self.RaVar.get() in raças:
            if self.ClaVar.get() in classes:
                if self.ClaVar.get() in classCar:
                    if self.ProVar.get() in lvl:
                        if self.CarVar.get() in options:
                            self.Carisma.config(state=DISABLED)
                            num2 = int(self.CarVar.get())
                            if self.RaVar.get() == ("Draconato" or
                                                    "Humano"):
                                num2 += 1
                            elif self.RaVar.get() == ("Tiefling" or
                                                      "Meio Elfo"):
                                num2 += 2
                            elif self.SubClaVar.get() == ("Drow" or
                                                          "Pés Leves"):
                                num2 += 1
                            RNum2 = random.randint(1, 20)
                            Prof = int(self.ProVar.get())
                            if Prof in Lvl_Baixo:
                                ProLvl = 2
                            elif Prof in Lvl_Medio:
                                ProLvl = 3
                            elif Prof in Lvl_Alto:
                                ProLvl = 4
                            elif Prof in Lvl_Muito_Alto:
                                ProLvl = 5
                            elif Prof in LVl_Divindade:
                                ProLvl = 6
                            Math2 = num2 + RNum2 + ProLvl
                            print(Math2, num2, RNum2, ProLvl)
                            if Math2 <= 0:
                                MLF2 = Label(self.Janela, text=1)
                                MLF2.grid(row=4, column=2)
                            else:
                                MLF2 = Label(self.Janela, text=Math2)
                                MLF2.grid(row=4, column=2)
                        else:
                            return None
                    else:
                        return None
                else:
                    if self.CarVar.get() in options:
                        self.Carisma.config(state=DISABLED)
                        num2 = int(self.CarVar.get())
                        if self.RaVar.get() == ("Draconato" or
                                                "Humano"):
                            num2 += 1
                        elif self.RaVar.get() == ("Tiefling" or
                                                  "Meio Elfo"):
                            num2 += 2
                        elif self.SubClaVar.get() == ("Drow" or
                                                      "Pés Leves"):
                            num2 += 1
                        RNum2 = random.randint(1, 20)
                        Math2 = num2 + RNum2
                        print(Math2, num2, RNum2)
                        if Math2 <= 0:
                            MLF2 = Label(self.Janela, text=1)
                            MLF2.grid(row=4, column=2)
                        else:
                            MLF2 = Label(self.Janela, text=Math2)
                            MLF2.grid(row=4, column=2)
                    else:
                        return None
            else:
                return None
        else:
            return None

    def ConConst(self):
        if self.ClaVar.get() in classes:
            if self.ClaVar.get() in classConst:
                if self.ProVar.get() in lvl:
                    if self.ConstVar.get() in options:
                        self.Constituição.config(state=DISABLED)
                        num3 = int(self.ConstVar.get())
                        if self.RaVar.get() == "Anão":
                            num3 += 2
                        elif self.RaVar.get() == ("Humano" or
                                                  "Meio-Orc"):
                            num3 += 1
                        elif self.SubClaVar.get() == ("Robustos" or
                                                      "Gnomo das Rochas"):
                            num3 += 1
                        RNum3 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        Math3 = num3 + RNum3 + ProLvl
                        print(Math3, num3, RNum3, ProLvl)
                        if Math3 <= 0:
                            MLF3 = Label(self.Janela, text=1)
                            MLF3.grid(row=5, column=2)
                        else:
                            MLF3 = Label(self.Janela, text=Math3)
                            MLF3.grid(row=5, column=2)
                    else:
                        return None
                else:
                    return None
            else:
                if self.ConstVar.get() in options:
                    self.Constituição.config(state=DISABLED)
                    num3 = int(self.ConstVar.get())
                    if self.RaVar.get() == "Anão":
                        num3 += 2
                    elif self.RaVar.get() == ("Humano" or
                                              "Meio-Orc"):
                        num3 += 1
                    elif self.SubClaVar.get() == ("Robustos" or
                                                  "Gnomo das Rochas"):
                        num3 += 1
                    RNum3 = random.randint(1, 20)
                    Math3 = num3 + RNum3
                    print(Math3, num3, RNum3)
                    if Math3 <= 0:
                        MLF3 = Label(self.Janela, text=1)
                        MLF3.grid(row=5, column=2)
                    else:
                        MLF3 = Label(self.Janela, text=Math3)
                        MLF3.grid(row=5, column=2)
                else:
                    return None
        else:
            return None

    def ConInte(self):
        if self.ClaVar.get() in classes:
            if self.ClaVar.get() in classInte:
                if self.ProVar.get() in lvl:
                    if self.InteVar.get() in options:
                        self.Inteligência.config(state=DISABLED)
                        num4 = int(self.InteVar.get())
                        if self.RaVar.get() == ("Humano" or
                                                "Tiefling"):
                            num4 += 1
                        elif self.RaVar.get() == ("Gnomo"):
                            num4 += 2
                        elif self.SubClaVar.get() == "Alto Elfo":
                            num4 += 1
                        RNum4 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        Math4 = num4 + RNum4 + ProLvl
                        print(Math4, num4, RNum4, ProLvl)
                        if Math4 <= 0:
                            MLF4 = Label(self.Janela, text=1)
                            MLF4.grid(row=6, column=2)
                        else:
                            MLF4 = Label(self.Janela, text=Math4)
                            MLF4.grid(row=6, column=2)
                    else:
                        return None
                else:
                    return None
            else:
                if self.InteVar.get() in options:
                    self.Inteligência.config(state=DISABLED)
                    num4 = int(self.InteVar.get())
                    if self.RaVar.get() == ("Humano" or
                                            "Tiefling"):
                        num4 += 1
                    elif self.RaVar.get() == ("Gnomo"):
                        num4 += 2
                    elif self.SubClaVar.get() == "Alto Elfo":
                        num4 += 1
                    RNum4 = random.randint(1, 20)
                    Math4 = num4 + RNum4
                    print(Math4, num4, RNum4)
                    if Math4 <= 0:
                        MLF4 = Label(self.Janela, text=1)
                        MLF4.grid(row=6, column=2)
                    else:
                        MLF4 = Label(self.Janela, text=Math4)
                        MLF4.grid(row=6, column=2)
                else:
                    return None
        else:
            return None

    def ConDex(self):
        if self.ClaVar.get() in classes:
            if self.ClaVar.get() in classDex:
                if self.ProVar.get() in lvl:
                    if self.DexVar.get() in options:
                        self.Destreza.config(state=DISABLED)
                        num5 = int(self.DexVar.get())
                        if self.RaVar.get() == ("Elfo" or
                                                "Halfling"):
                            num5 += 2
                        elif self.RaVar.get() == "Humano":
                            num5 += 1
                        elif self.SubClaVar.get() == "Gnomo das Florestas":
                            num5 += 1
                        RNum5 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        Math5 = num5 + RNum5 + ProLvl
                        print(Math5, num5, RNum5, ProLvl)
                        if Math5 <= 0:
                            MLF5 = Label(self.Janela, text=1)
                            MLF5.grid(row=7, column=2)
                        else:
                            MLF5 = Label(self.Janela, text=Math5)
                            MLF5.grid(row=7, column=2)
                    else:
                        return None
                else:
                    return None
            else:
                if self.DexVar.get() in options:
                    self.Destreza.config(state=DISABLED)
                    num5 = int(self.DexVar.get())
                    if self.RaVar.get() == ("Elfo" or
                                            "Halfling"):
                        num5 += 2
                    elif self.RaVar.get() == "Humano":
                        num5 += 1
                    elif self.SubClaVar.get() == "Gnomo das Florestas":
                        num5 += 1
                    RNum5 = random.randint(1, 20)
                    Math5 = num5 + RNum5
                    print(Math5, num5, RNum5)
                    if Math5 <= 0:
                        MLF5 = Label(self.Janela, text=1)
                        MLF5.grid(row=7, column=2)
                    else:
                        MLF5 = Label(self.Janela, text=Math5)
                        MLF5.grid(row=7, column=2)
                else:
                    return None
        else:
            return None

    def ConSab(self):
        if self.ClaVar.get() in classes:
            if self.ClaVar.get() in classSab:
                if self.ProVar.get() in lvl:
                    if self.SabVar.get() in options:
                        self.Sabedoria.config(state=DISABLED)
                        num6 = int(self.SabVar.get())
                        if self.RaVar.get() == "Humano":
                            num6 += 1
                        elif self.SubClaVar.get() == ("Anão da Colina" or
                                                      "Elfo da Floresta"):
                            num6 += 1
                        RNum6 = random.randint(1, 20)
                        Prof = int(self.ProVar.get())
                        if Prof in Lvl_Baixo:
                            ProLvl = 2
                        elif Prof in Lvl_Medio:
                            ProLvl = 3
                        elif Prof in Lvl_Alto:
                            ProLvl = 4
                        elif Prof in Lvl_Muito_Alto:
                            ProLvl = 5
                        elif Prof in LVl_Divindade:
                            ProLvl = 6
                        Math6 = num6 + RNum6 + ProLvl
                        print(Math6, num6, RNum6, ProLvl)
                        if Math6 <= 0:
                            MLF6 = Label(self.Janela, text=1)
                            MLF6.grid(row=8, column=2)
                        else:
                            MLF6 = Label(self.Janela, text=Math6)
                            MLF6.grid(row=8, column=2)
                    else:
                        return None
                else:
                    return None
            else:
                if self.SabVar.get() in options:
                    self.Sabedoria.config(state=DISABLED)
                    num6 = int(self.SabVar.get())
                    if self.RaVar.get() == "Humano":
                        num6 += 1
                    elif self.SubClaVar.get() == ("Anão da Colina" or
                                                  "Elfo da Floresta"):
                        num6 += 1
                    RNum6 = random.randint(1, 20)
                    Math6 = num6 + RNum6
                    print(Math6, num6, RNum6)
                    if Math6 <= 0:
                        MLF6 = Label(self.Janela, text=1)
                        MLF6.grid(row=8, column=2)
                    else:
                        MLF6 = Label(self.Janela, text=Math6)
                        MLF6.grid(row=8, column=2)
                else:
                    return None
        else:
            return None

    def subclafun(self, value):
        #   vai verificar se a classe escolhida tem sub-raça
        #   se tiver, vai mostrar as opções
        if self.RaVar.get() == "Anão":
            SubClaMen = OptionMenu(self.Janela, self.SubClaVar, *SCA)
            SubClaMen.grid(row=3, column=5)
        elif self.RaVar.get() == "Elfo":
            SubClaMen = OptionMenu(self.Janela, self.SubClaVar, *SCE)
            SubClaMen.grid(row=3, column=5)
        elif self.RaVar.get() == "Halfling":
            SubClaMen = OptionMenu(self.Janela, self.SubClaVar, *SCH)
            SubClaMen.grid(row=3, column=5)
        elif self.RaVar.get() == "Gnomo":
            SubClaMen = OptionMenu(self.Janela, self.SubClaVar, *SCG)
            SubClaMen.grid(row=3, column=5)
