# Usando uma variável counter para sair do loop
counter = 5
while counter != 0: # "while counter:" também funciona
    print("Counter vale:", counter)
    counter -= 1
print("Acabou!")

# Usando uma variável boolean para sair do loop
done = False
while not done:
    print("Looping...")
    done = True
print("Acabou!")

# Usando break para sair do loop
while True:
    print("Looping...")
    break

# Contando até 100
i = 0
while i < 100:
    print(i)
    i += 1
    