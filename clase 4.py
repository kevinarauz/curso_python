# uso for
for i in range(11):
    print(i)

for i in range(1, 6):
    print(i)

i = 0
while i < 6:

    if i == 3:
        #break
        print(f"Encontre el valor: {i}")
        i += 1
        continue

    print(f"El valor de i es: {i}")
    i += 1

# Aleatorio

import random

numero = random.randint(1, 5)

print(numero)

text = "Estoy aprendiendo Python"
letra = random.choice(text)
print(letra)

#Arreglos
caja = [1, "Pyhton", 2, "Golang", True, 12.5]

print(caja)

caja.append("Java")
print(caja)

caja.insert(1, "Hello")
print(caja)

#pop
caja.pop(4)
print(caja)

#remove
caja.remove(12.5)
print(caja)

print(caja[2])

caja[4] = False
print(caja)

index = caja.index("Hello")
print(index)

for i in caja:
    print(f"Elementos de la lista: {i}")

# tuplas {} - inmutable
tup = {1, 2, 3, 4, 5}
print(tup)

for i in tup:
    print(f"Elementos de la lista tupla: {i}")

