import random


class Calculadora:

    def __init__(self, forç, car, const,  inte, dex, sab, prof):
        self.forç = forç
        self.car = car
        self.const = const
        self.inte = inte
        self.dex = dex
        self.sab = sab
        self.prof = prof

    def somaForça(self):
        dadinhoForç = random.randint(1, 20)
        finalFor = dadinhoForç + self.prof + self.forç
        if finalFor < 0:
            return 0
        else:
            return finalFor

    def somaCar(self):
        dadinhoCar = random.randint(1, 20)
        finalCar = dadinhoCar + self.prof + self.car
        if finalCar < 0:
            return 0
        else:
            return finalCar

    def somaConst(self):
        dadinhoConst = random.randint(1, 20)
        finalConst = dadinhoConst + self.prof + self.const
        if finalConst < 0:
            return 0
        else:
            return finalConst

    def somaInte(self):
        dadinhoInte = random.randint(1, 20)
        finalInte = dadinhoInte + self.prof + self.inte
        if finalInte < 0:
            return 0
        else:
            return finalInte

    def somaDex(self):
        dadinhoDex = random.randint(1, 20)
        finalDex = dadinhoDex + self.prof + self.dex
        if finalDex < 0:
            return 0
        else:
            return finalDex

    def somaSab(self):
        dadinhoSab = random.randint(1, 20)
        finalSab = dadinhoSab + self.prof + self.sab
        if finalSab < 0:
            return 0
        else:
            return finalSab
