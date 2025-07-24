# Crea un juego en Python para adivinar un número del 1 al 100, siguiendo estos pasos:

# Importa el módulo random.
# Define una función jugar_adivina_numero.
# Genera un número aleatorio entre 1 y 100.
# Pide al usuario adivinar el número, indicando si es alto o bajo.
# Felicita al usuario cuando adivine correctamente y muestra el número de intentos.


import random # importa el módulo random, que contiene funciones para generar números aleatorios.

#import es una declaracion que permite incluir modulos o paquetes dentro o fuera de python
#random es un modulo que ya viene incluido dentro de la libreria interna de python
#cuando instalamos python se incluyen todos estos modulos y paquetes

def jugar_adivina_numero():
    numero_secreto = random.randint(1, 100)
    #se le asigna el modulo random para ser utilizado con la funcion randint 
    #randint (random interger) es quien toma el valor minimo y maximo de dos enteros
    intentos = 0
    while True:
        intentos += 1
        intento = int(input("Adivina el número (entre 1 y 100): "))
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

jugar_adivina_numero()