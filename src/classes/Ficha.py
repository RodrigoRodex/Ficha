from pessoas import Calculadora

#   cada while é responsavel por perguntar um modificador
#   se o que for escrito em For, resultar em ValueError
#   vai pedir apenas números inteiros
#   se em For, o resultador for um número
#   vai gerar um break, que vai parar o while de For

Lvl_Baixo = (1, 2, 3, 4)
Lvl_Medio = (5, 6, 7, 8)
Lvl_Alto = (9, 10, 11, 12)
Lvl_Muito_Alto = (13, 14, 15, 16)
LVl_Divindade = (17, 18, 19, 20)

while True:
    for itens in Lvl_Baixo:
        print(itens)
    try:
        Lvl = int(input('\nQual o seu nível?'))
        if Lvl in Lvl_Baixo:
            Prof = 2
        elif Lvl in Lvl_Medio:
            Prof = 3
        elif Lvl in Lvl_Alto:
            Prof = 4
        elif Lvl in Lvl_Muito_Alto:
            Prof = 5
        elif Lvl in LVl_Divindade:
            Prof = 6
        elif Lvl not in Lvl_Baixo or Lvl_Medio:

            break
        break
    except ValueError:
        print('Apenas números, por favor')

while True:
    try:
        For = int(input('Qual a Força?'))
        break
    except ValueError:
        print('Apenas números inteiros, por favor\n')
        #   \n está gerando duas linhas, é para gerar apenas uma

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
#   o 2 é a proficiencia
c = Calculadora(For, Car, Const, Inte, Dex, Sab, Prof)


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


#   teste de resistência
Resistencia = {}
Resistencia['força'] = força
Resistencia['carisma'] = carisma
Resistencia['constituição'] = constituição
Resistencia['inteligência'] = inteligencia
Resistencia['destreza'] = destreza
Resistencia['sabedoria'] = sabedoria
"""
#   teste de pericias
Pericias = {}
Pericias['Acrobacia'] = Acrobacia
Pericias['Adestrar'] = Adestrar
Pericias['Arcanismo'] = Arcanismo
Pericias['Atletismo'] = Atletismo
Pericias['Atuação'] = Atuação
Pericias['Enganação'] = Enganação
Pericias['Furtividade'] = Furtividade
Pericias['História'] = Historia
Pericias['Intimidação'] = intimidação
Pericias['Intuição'] = Intuição
Pericias['Investigação'] = Investigação
Pericias['Medicina'] = Medicina
Pericias['Natureza'] = Natureza
Pericias['Percepção'] = Percepção
Pericias['Persuação'] = Percepção
Pericias['Prestidigitação'] = Prestidigitação
Pericias['Religião'] = Religião
Pericias['Sobrevivência'] = Sobrevivência

"""
while True:
    for key in Resistencia.keys():
        print('  - ' + key)
    nome = input('O que você quer?:\n')
    if nome in Resistencia:
        Resistencia[nome]()
    else:
        print('Não achei: ')
