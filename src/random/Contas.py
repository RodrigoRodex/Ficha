import random
Va = True
while Va:
    Rad = random.randint(-1000, 1000)
    Rad2 = random.randint(-1000, 1000)
    soma = Rad + Rad2
    print("Número um", Rad)
    print("Número dois", Rad2)
    questão1 = int(input("Some: "))
    if questão1 == soma:
        print("Correto!")
    else:
        print("Errado")
        print(soma)
    Rad3 = random.randint(-1000, 1000)
    Rad4 = random.randint(-1000, 1000)
    soma2 = Rad3 - Rad4
    print("Número um", Rad3)
    print("Número dois", Rad4)
    questão2 = int(input("Subtraia: "))
    if questão2 == soma2:
        print("Correto!")
    else:
        print("Errado")
        print(soma2)
    Rad5 = random.randint(-1000, 1000)
    Rad6 = random.randint(-1000, 1000)
    soma3 = Rad5 * Rad6
    print("Número um", Rad5)
    print("Número dois", Rad6)
    questão3 = int(input("Multiplique: "))
    if questão3 == soma3:
        print("Correto!")
    else:
        print("Errado")
        print(soma3)
    Rad7 = random.randint(-1000, 1000)
    Rad8 = random.randint(-1000, 1000)
    soma4 = Rad7 / Rad8
    print("Número um", Rad7)
    print("Número dois", Rad8)
    questão4 = int(input("Divida: "))
    if questão4 == soma4:
        print("Correto!")
    else:
        print("Errado")
        print(soma4)
    Extra = input("Quer parar?")
    if Extra == "Sim" or "sim" or "s" or "S":
        Va = False
    else:
        Va = True
