# Funções e escopos

# Exemplo de escopo de variável
# Variável local
def my_function():
    var = 2 
    print("Eu conheço aquela variável?", var)
 
# variável global
var = 1 
my_function()
print(var) 