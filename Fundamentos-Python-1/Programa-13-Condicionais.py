# Condições e execução condicional
# Execução condicional: o comando if
a = 5
if a == 5:
    print("A variável 'a' é igual a 5.")

# Execução condicional: o comando if-else
if a == 5:
    print("A variável 'a' é igual a 5.")
else:
    print("A variável 'a' não é igual a 5.")

# Execução condicional: o comando if-elif-else
if a < 5:
    print("A variável 'a' é menor que 5.")
elif a > 5:
    print("A variável 'a' é maior que 5.")
else:
    print("A variável 'a' é igual a 5.")

# Comandos if-else aninhados
if a >= 0:
    if a == 0:
        print("A variável 'a' é zero.")
    else:
        print("A variável 'a' é um número positivo.")
else:
    print("A variável 'a' é um número negativo.")