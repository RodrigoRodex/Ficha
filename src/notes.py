from random import randint
import random
var = (1)  # tuple
var1 = {1}  # set
var2 = [1]  # list
var3 = {
    "chave": 1  # dict
}

# Python program showing

username = input("Enter username:")
print("Username is: " + username)

while True:
    numChar = input("Qual atributo você quer?:")
    print("Qual você quer?:")
    number1 = random.randrange(1, 6)
    number2 = random.randrange(1, 6)

    if number1 or number2 == 3:
        print("sim")

    elif number2 or number2 > 2:
        print("é")

    elif number1 or number2 < 5:
        print("talvez")
    break
char = 4
total = 2
times_run = 0
while times_run <= total:
    gen1 = random.randint(1, 6)
    if char >= gen1:
        print("ok")
        times_run += 1

print("legal", 3)

repeat = True
while repeat:
    print("You rolled", randint(1, 6))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()

#   input chamando def
functions = {}
functions['dado20'] = dado20
functions['dado6'] = dado6
functions['dado8'] = dado8

while True:

    name = input('Qual o nome do dado?:\n')
    if name in functions:
        functions[name]()
    else:
        print('Dado não valido, inrira outro: ')
        for key in functions.keys():
            print('  - ' + key)

