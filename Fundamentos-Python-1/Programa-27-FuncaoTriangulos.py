# Função que calcula a área de um triângulo
# A função terá três parâmetros - um para cada lado.
# Ele retornará True se os lados puderem construir um triângulo, e False caso contrário. Nesse caso, triangulo é um bom nome para essa função.
def triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        return True
    else:
        return False

# Testando a função
print(triangulo(3, 4, 5))  # Deve retornar True
print(triangulo(1, 2, 3))  # Deve retornar False