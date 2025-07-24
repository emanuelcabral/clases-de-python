#Contar los números impares en una lista

# Consigna: Escribe un programa que cuente cuántos números impares hay en la lista [2, 3, 5, 7, 8, 10, 13, 17] y muestre el resultado.

lista = [2, 3, 5, 7, 8, 10, 13, 17]
contador_impares = 0
for numero in lista:
    if numero % 2 != 0:
        contador_impares += 1
print("Cantidad de números impares:", contador_impares)