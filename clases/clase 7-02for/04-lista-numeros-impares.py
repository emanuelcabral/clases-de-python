# Generar una lista de números pares:

# Consigna: Escribe un programa que genere una lista con los números pares del 2 al 20.

pares = []
for i in range(0, 21, 2):
    pares.append(i)
print(pares)