#sumar numeros

# Escribe un programa que pida al usuario números enteros y los vaya sumando hasta que el usuario introduzca el número 0.

suma = 0
numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Introduce un número (0 para terminar): "))
print("La suma total es:", suma)