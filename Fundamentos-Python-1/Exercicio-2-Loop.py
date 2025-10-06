maior_valor = -999999999
 
# Insira o primeiro valor.
numero = int(input("Digite um número ou digite -1 para parar: "))
 
# Se o número não for igual a -1, continue.
while numero != -1:
    # O número é maior que o maior_número?
    if numero > maior_valor:
        # Sim, atualize o maior_número.
        maior_valor = numero
    # Insira o próximo número.
    numero = int(input("Digite um número ou digite -1 para parar: "))
 
# Imprima o maior número.
print("O maior número é:", maior_valor)