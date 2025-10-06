# Função que calcula o n-ésimo número de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testando a função
for n in range(1, 10):
    print(n, "->", fibonacci(n))    