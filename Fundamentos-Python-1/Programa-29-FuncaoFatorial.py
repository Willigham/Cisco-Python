# Função que calcula o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Testando a função
print(fatorial(4))  # Deve retornar 24