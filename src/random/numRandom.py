import random

diceRandom = random.randrange(1, 20)

charToken = {
    "for": 5,
    "int": 3,
    "dex": 4,
    "wis": -1,
    "car": -2
}

numRandomChar = random.choice(list(charToken.values()))
char = numRandomChar+diceRandom

if (diceRandom == 20):
    print("WOWWWW!!!!! CRÍTICO")

elif (char >= 15):

    print('passou no teste')
    print(char)

elif (char <= 0):

    print(1)
    print("zero ou menor")

else:

    print('não passou')
    print(char)
