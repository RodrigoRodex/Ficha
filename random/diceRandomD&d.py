import random

charToken = {
    "for": 5,
    "int": 3,
    "const": 2,
    "dex": 4,
    "wis": -1,
    "car": -2
}
while True:

    twentySidedDie = random.randint(1, 20)
    numChar = charToken.get(input("Qual atributo você quer?:"))
    char = numChar + twentySidedDie

    if (twentySidedDie == 20):
        print('WOWWW Crítico!!!!')

    elif (char > 15):

        print('Passou no teste', char)

    elif (char <= 0):

        print('Zero ou menor', 1)

    else:

        print('Não passou', char)
