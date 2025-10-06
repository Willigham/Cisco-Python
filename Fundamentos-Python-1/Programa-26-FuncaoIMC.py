# Função que calcula o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Exemplo de uso da função
peso = 70  # em kg
altura = 1.75  # em metros
imc = calcular_imc(peso, altura)
print("O IMC é:", imc)

# Função que classifica o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
classificacao = classificar_imc(imc)
print("Classificação do IMC:", classificacao)