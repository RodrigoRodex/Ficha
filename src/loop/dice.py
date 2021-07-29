import random

#   função do dado de 20 lados pega quantos dados você quer e transforma em X


def dado20():
    x = int(input("Quantos números você quer?:"))
#   X é quantas vezes eu quero o número aleatório numRandom se transforma em i
    numRandom = random.sample(range(1, 20), x)
    for i in numRandom:
        print(i)
#   i é printado um de cada vez, um loop


def dado6():
    x = int(input("Quantos números você quer?:"))
    numRandom = random.sample(range(1, 6), x)
    for i in numRandom:
        print(i)


def dado8():
    x = int(input("Quantos números você quer?:"))
    numRandom = random.sample(range(1, 8), x)
    for i in numRandom:
        print(i)


def dado10():
    x = int(input("Quantos números você quer?:"))
    numRandom = random.sample(range(1, 10), x)
    for i in numRandom:
        print(i)

#   cria um dict com o nome dados dentro de dados cria uma chave com o nome
#   de dado20 e a informação de dado20, no caso o def


dados = {}
dados['dado20'] = dado20
dados['dado6'] = dado6
dados['dado8'] = dado8
dados['dado10'] = dado10


#   loop permanente
while True:
    #   pergunta o nome do dado se o nome digitado estiver em dados vai abrir
    #   a informação, no caso a def se não achar o dado dentro do dict
    for key2 in dados.keys():
        print('  - ' + key2)
    name = input('Qual o nome do dado?:\n')
    if name in dados:
        dados[name]()
    else:
        print('Dado não valido, inrira outro: ')
        for key in dados.keys():
            print('  - ' + key)
#   vai printar todos as keys dentro do dict
#   apenas as keys e perguntar qual dado você quer
