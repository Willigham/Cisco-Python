# Leia três números.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
 
# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
maior_numero = max(n1, n2, n3)
 
# Imprimir o resultado.
print("O maior número é:", maior_numero)

# Alternativamente, você pode usar condicionais para encontrar o maior número:
if (n1 >= n2) and (n1 >= n3):
    maior_numero = n1
elif (n2 >= n1) and (n2 >= n3):
    maior_numero = n2
else:
    maior_numero = n3
print("O maior número é:", maior_numero)