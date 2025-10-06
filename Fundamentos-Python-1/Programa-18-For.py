# Usando um loop for
for i in range(10):
    print("o valor de i é atualmente:", i)

# Usando um loop for com um valor inicial diferente
for i in range(2, 8):
    print("O valor de i é atualmente", i)

# Usando um loop for com um passo diferente
for i in range(2, 8, 3):
    print("O valor de i é atualmente", i)


# Calculando potências de 2
power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2