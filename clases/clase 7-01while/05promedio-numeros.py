# Promedio de números

# Escribe un programa que pida al usuario números enteros y calcule su promedio. El programa debe dejar de pedir números cuando el usuario introduzca un número negativo.

suma = 0
contador = 0
numero = int(input("Introduce un número (número negativo para terminar): "))
while numero >= 0:
    suma += numero
    contador += 1
    numero = int(input("Introduce un número (número negativo para terminar): "))
if contador > 0:
    promedio = suma / contador
    print("El promedio es:", promedio)
else:
    print("No se introdujeron números positivos.")