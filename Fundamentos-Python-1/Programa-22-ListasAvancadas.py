# Listas avançadas em Python
# Compreensão de listas
quadrados = [x**2 for x in range(10)]
print(quadrados)

# Filtrando com compreensão de listas
pares = [x for x in range(20) if x % 2 == 0]
print(pares)

# Listas de listas (matrizes)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

# Acessando elementos em matrizes
print(matriz[0][1])  # Acessa o elemento 2
print(matriz[2][0])  # Acessa o elemento 7


