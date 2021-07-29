import random

char = 3
repeat = ()

while repeat:

    diceRandom1 = random.randrange(1, 6)
    diceRandom2 = random.randrange(1, 6)

    if(diceRandom1 == char):
        print("WOWWWW!!!!! CRÍTICO")

    if (diceRandom1 > char):
        print("parabéns", diceRandom1, sep=', ')

    if(diceRandom1 < char):
        print("não", diceRandom1, sep=', ')

    if (diceRandom2 == char):
        print("WOWWWW!!!!! CRÍTICO")

    if(diceRandom2 > char):
        print("parabéns", diceRandom2, sep=', ')

    if(diceRandom2 < char):
        print("não", diceRandom1, sep=', ')

    x = (input('você quer rodar o dado de novo?:'))
    y = bool(x)
    repeat = y
