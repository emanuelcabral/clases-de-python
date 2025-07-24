#adivina el numero

# Escribe un programa que genere un número aleatorio entre 1 y 100, y pida al usuario que lo adivine. El programa debe continuar pidiendo al usuario que adivine el número hasta que lo adivine correctamente.

import random
numero_secreto = random.randint(1, 100)
adivina = int(input("Adivina el número entre 1 y 100: "))
while adivina != numero_secreto:
    if adivina < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    adivina = int(input("Intenta de nuevo: "))
print("¡Felicidades! Adivinaste el número.")