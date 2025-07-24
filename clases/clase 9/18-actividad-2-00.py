# Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

# 🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.

#------------------------------------------------------------------------------------#

# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

# Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:
# 🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

# Comprueba el punto intermedio entre -12 y 24


#------------------------------------------------------------------------------------#

# Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()


#------------------------------------------------------------------#

# Función area_rectangulo()

def area_rectangulo(base, altura):
    return base * altura

# Cálculo del área de un rectángulo de 15 de base y 10 de altura
area = area_rectangulo(15, 10)
print(f"El área del rectángulo es: {area}")

#------------------------------------------------------------------#

# Función area_circulo()

import math

def area_circulo(radio):
    return math.pi * radio ** 2

# Cálculo del área de un círculo de 5 de radio
area = area_circulo(5)
print(f"El área del círculo es: {area}")

#------------------------------------------------------------------#

# Función relacion()
def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

# Comprobación de la relación entre los números
print(relacion(5, 10))  # Debería devolver -1
print(relacion(10, 5))  # Debería devolver 1
print(relacion(5, 5))   # Debería devolver 0

#------------------------------------------------------------------#

# Función intermedio()

def intermedio(num1, num2):
    return (num1 + num2) / 2

# Comprobación del punto intermedio entre -12 y 24
punto_intermedio = intermedio(-12, 24)
print(f"El punto intermedio es: {punto_intermedio}")

#------------------------------------------------------------------#

# Función recortar()

def recortar(numero, limite_inferior, limite_superior):
    if numero < limite_inferior:
        return limite_inferior
    elif numero > limite_superior:
        return limite_superior
    else:
        return numero

# Comprobación del resultado de recortar 15 entre los límites 0 y 10
resultado = recortar(15, 0, 10)
print(f"El resultado de recortar es: {resultado}")

#------------------------------------------------------------------#

# Función separar()

def separar(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    pares.sort()
    impares.sort()
    return pares, impares

# Comprobación de la función separar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar(lista)
print(f"Pares: {pares}")
print(f"Impares: {impares}")

#------------------------------------------------------------------#