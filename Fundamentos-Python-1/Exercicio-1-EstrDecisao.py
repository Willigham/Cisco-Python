# uma única declaração if, por exemplo:
x = 10
if x == 10:
    print("A variável 'x' é igual a 10.")

# uma série de declarações if, por exemplo:
if x == 10:
    print("A variável 'x' é igual a 10.")
if x > 5:
    print("A variável 'x' é maior que 5.")
if x < 15:
    print("A variável 'x' é menor que 15.")

# uma declaração if-else, por exemplo:
if x == 10:
    print("A variável 'x' é igual a 10.")
else:
    print("A variável 'x' não é igual a 10.")

# A declaração if-elif-else, por exemplo:
if x == 10:
    print("A variável 'x' é igual a 10.")
elif x > 10:
    print("A variável 'x' é maior que 10.")
else:
    print("A variável 'x' é menor que 10.")

# Instruções condicional aninhadas, por exemplo:
if x > 5:
    print("A variável 'x' é maior que 5.")
    if x > 10:
        print("A variável 'x' é maior que 10.")
    else:
        print("A variável 'x' não é maior que 10.")
else:
    print("A variável 'x' não é maior que 5.")