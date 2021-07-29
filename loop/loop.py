cond = True
while cond:
    temperature = (input('What is the temperature? '))
    #   sem or na condição
    if temperature == "sim":
        print('Wear shorts.')
    elif temperature == "não":
        cond = False
