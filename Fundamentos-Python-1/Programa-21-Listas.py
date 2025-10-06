# Listas em Python
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)

# Acessando elementos
print(minha_lista[0])  # Primeiro elemento
print(minha_lista[2])  # Terceiro elemento

# Adicionando elementos
minha_lista.append(6)
print(minha_lista)

# Removendo elementos
minha_lista.remove(2)
print(minha_lista)

# Iterando sobre a lista
for numero in minha_lista:
    print("Número:", numero)

# Comprimento da lista
print("Comprimento da lista:", len(minha_lista))

# Listas podem conter diferentes tipos de dados
outra_lista = [1, "dois", 3.0, True]
print(outra_lista)

# Listas aninhadas
lista_aninhada = [1, [2, 3], [4, 5]]
print(lista_aninhada)

# Acessando elementos em listas aninhadas
print(lista_aninhada[1][0])  # Acessa o elemento 2
print(lista_aninhada[2][1])  # Acessa o elemento 5
# Modificando elementos
minha_lista[0] = 10
print(minha_lista)
# Ordenando uma lista
minha_lista.sort()
print(minha_lista)

# Revertendo uma lista
minha_lista.reverse()
print(minha_lista)

# Limpando uma lista
minha_lista.clear()
print(minha_lista)

# Verificando se um elemento está na lista
print(3 in minha_lista)


