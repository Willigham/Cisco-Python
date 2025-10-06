# Função para calcular a soma de dois números
def soma(a, b):
    return a + b

# Função para calcular a subtração de dois números
def subtracao(a, b):
    return a - b

# Função para calcular a multiplicação de dois números
def multiplicacao(a, b):
    return a * b

# Função para calcular a divisão de dois números
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."
    
# Função principal para executar o programa
def main():
    print("Calculadora Simples")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    print(f"Soma: {soma(num1, num2)}")
    print(f"Subtração: {subtracao(num1, num2)}")
    print(f"Multiplicação: {multiplicacao(num1, num2)}")
    print(f"Divisão: {divisao(num1, num2)}")