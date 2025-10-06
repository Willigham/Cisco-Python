# O primeiro deles é um método chamado de keys(), possuído por cada dicionário. O método retorna um objeto iterável que consiste em todas as chaves reunidas no dicionário. Ter um grupo de chaves permite acessar todo o dicionário de forma fácil e prática.
dicionario = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for key in dicionario.keys():
    print(key, "->", dicionario[key])
 