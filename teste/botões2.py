from defs import matemática
#   Aqui é onde roda o while, pra deixar mais separadinho
#   e é onde tem se é ou não para repetir
condPlus = {}
condPlus['Sim'] = True
condPlus['Não'] = False

cond = True

while cond:

    matemática()

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
