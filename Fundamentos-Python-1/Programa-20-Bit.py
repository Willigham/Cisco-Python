# Operadores bit a bit
a = 4  # 0100 em binário
b = 1  # 0001 em binário

# AND bit a bit
print(a & b)  # 0 (0000 em binário)

# OR bit a bit
print(a | b)  # 5 (0101 em binário)

# NOT bit a bit
print(~a)     # -5 (inverte todos os bits)

# XOR bit a bit
print(a ^ b)  # 5 (0101 em binário)

# Deslocamento à esquerda
print(a << 1) # 8 (1000 em binário)

# Deslocamento à direita
print(a >> 1) # 2 (0010 em binário)
