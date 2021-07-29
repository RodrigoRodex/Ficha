from calculadoraMelhor import Calculadora2
#   essa função pega o que ta em calculadoraMelhor e manda pra botões2
sinais = {}
sinais['-'] = 'menos'
sinais['+'] = 'mais'
sinais['*'] = 'vezes'
sinais['/'] = 'divizão'

condPlus = {}
condPlus['Sim'] = True
condPlus['Não'] = False


def matemática():

    a = int(input('da um número ai seu corno:'))
    b = int(input('Agora outro número, corno:'))

    for key in sinais.keys():
        print('  -> ' + key)
    c = input('Qual o sinal:')
    #   sem o c informando qual o número, você pode
    #   escolher números diferentes pra contas diferentes

    Calculo = Calculadora2(a, b)

    if '+' in c:
        print(Calculo.soma())

    if '-' in c:
        print(Calculo.subtrair())

    if '*' in c:
        print(Calculo.multiplicar())

    if '/' in c:
        print(Calculo.divide())

    for chave in condPlus.keys():
        print('  -> ' + chave)
    plus = (input('De novo? '))

    if plus in condPlus:

        if plus == "Sim":
            cond = True

        elif plus == "Não":
            cond = False
    else:
        print('Não entendi, repete')
