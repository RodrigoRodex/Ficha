import random
#   Pra puxar uma função
#   com as outras funções
#   você precisa de um
#   input perguntando qual
#   das funções você quer,
#   isso dentro da função maior


def numRandom():
    x = int(input("fala ai:"))
    numRandomSix = random.sample(range(1, 6), x)
    for i in numRandomSix:
        print(i)


def numRandom2():
    x1 = int(input("Fala ai:"))
    numRandomTwenty = random.sample(range(1, 20), x1)
    for h in numRandomTwenty:
        print(h)


def numRandom3():
    x2 = int(input("Fala ai:"))
    numRandomEight = random.sample(range(1, 8), x2)
    for j in numRandomEight:
        print(j)
