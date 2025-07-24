# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.


#------------------------------------------------------------------#

# Función area_circulo()

import math

def area_circulo(radio):
    return math.pi * radio ** 2

# Cálculo del área de un círculo de 5 de radio
area = area_circulo(5)
print(f"El área del círculo es: {area}")

#------------------------------------------------------------------#
