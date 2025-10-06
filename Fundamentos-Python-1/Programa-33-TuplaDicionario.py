# Tuplas e dicionários podem trabalhar juntos
minha_tupla = ("gato", "cachorro", "cavalo")
meu_dicionario = {
    "gato": "chat",
    "cachorro": "chien",
    "cavalo": "cheval"
}
for animal in minha_tupla:
    print(f"O {animal} em francês é {meu_dicionario[animal]}")
    
# Saída:
# O gato em francês é chat
# O cachorro em francês é chien
# O cavalo em francês é cheval