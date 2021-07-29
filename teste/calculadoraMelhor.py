class Calculadora2:
    #   classe vai para defs
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        #   print antes do return, acho que tudo antes dele
        print("doido né")
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b
