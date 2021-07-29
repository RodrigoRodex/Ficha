from pessoas import Calculadora

#   cada while é responsavel por perguntar um modificador
#   se o que for escrito em For, resultar em ValueError
#   vai pedir apenas números inteiros
#   se em For, o resultador for um número
#   vai gerar um break, que vai parar o while de For

while True:
    try:
        For = int(input('Qual a Força?'))
        break
    except ValueError:
        print('Apenas números inteiros, por favor\n')
        #   \n ta com problema

while True:
    try:
        Car = int(input('\nQual o Carisma?'))
        break
    except ValueError:
        print('Apenas números inteiros, por favor\n')

while True:
    try:
        Const = int(input('\nQual a Constituição?'))
        break
    except ValueError:
        print('Apenas números inteiros, por favor\n')

while True:
    try:
        Inte = int(input('\nQual a Inteligência?'))
        break
    except ValueError:
        print('Apenas números inteiros, por favor\n')

while True:
    try:
        Dex = int(input('\nQual a Destreza?'))
        break
    except ValueError:
        print('Apenas números inteiros, por favor\n')

while True:
    try:
        Sab = int(input('\nQual a Sabedória?'))
        break
    except ValueError:
        print('Apenas números inteiros, por favor\n')

#   mudar as funções, usar os modificadores junto com a prof e o dado
#   adicionar novas funções, uma pra cada modificador
#   colocar dentro do while qual modificador eu quero
#   soma de modificadores

c = Calculadora(For, Car, Const, Inte, Dex, Sab, 2)


def força():
    print(c.somaForça(), 'Esse é o soma de força\n')


def carisma():
    print(c.somaCar(), 'Essa é a soma do Carisma\n')


def constituição():
    print(c.somaConst(), 'Essa é a soma da Constituição\n')


def inteligencia():
    print(c.somaInte(), 'Essa é a soma da Inteligência\n')


def destreza():
    print(c.somaDex(), 'Essa é a soma de destreza\n')


def sabedoria():
    print(c.somaSab(), 'Essa é a soma do carisma\n')


funções = {}
funções['força'] = força
funções['carisma'] = carisma
funções['constituição'] = constituição
funções['inteligência'] = inteligencia
funções['destreza'] = destreza
funções['sabedoria'] = sabedoria

while True:
    for key in funções.keys():
        print('  - ' + key)
    nome = input('O que você quer?:\n')
    if nome in funções:
        funções[nome]()
    else:
        print('Não achei: ')
