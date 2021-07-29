import random

char = 3
repeat = True

while repeat:

    diceRandom1 = random.randrange(1, 6)
    diceRandom2 = random.randrange(1, 6)

    if(diceRandom1 == char):
        print("WOWWWW!!!!! CRÍTICO")

    elif(diceRandom1 > char):
        print("Parabéns", diceRandom1, sep=', ')

    elif(diceRandom1 < char):
        print("não", diceRandom1, sep=', ')

    if(diceRandom2 == char):
        print("WOWWWW!!!!! CRÍTICO")

    elif(diceRandom2 > char):
        print("Parabéns", diceRandom2, sep=', ')

    elif(diceRandom2 < char):
        print("não", diceRandom2, sep=', ')

#   Cuzão, demorou uns dias pra eu enteder essa merda e era mó simples
    x = input('Quer rodas os números mais uma vez?:')
    if x == "não" or "Não":
        repeat = False
    elif x == "sim" or "Sim":
        repeat = True
