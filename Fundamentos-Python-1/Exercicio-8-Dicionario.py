# Criando um dicionário
meu_dicionario = {
    "gato": "chat",
    "cachorro": "chien",
    "cavalo": "cheval"
}

meu_dicionario.update({"pato": "canard"})
print(meu_dicionario)

# removendo um item
del meu_dicionario["pato"]

# removendo o último item adicionado
meu_dicionario.popitem()

# removendo um item específico
meu_dicionario.pop("cavalo")

# limpando o dicionário
meu_dicionario.clear()

print(meu_dicionario)