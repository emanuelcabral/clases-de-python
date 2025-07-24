# Desarrollando un Calculador de IMC

# Objetivo:
# El objetivo de este ejercicio es que desarrollen un programa en Python que calcule el Índice de Masa Corporal (IMC) de una persona y determine su categoría de peso según los estándares establecidos por la Organización Mundial de la Salud (OMS).

# Instrucciones:

# Función de cálculo de IMC: Crea una función en Python que calcule el Índice de Masa Corporal (IMC) de una persona. Esta función debe tener dos parámetros: el peso en kilogramos (flotante) y la altura en metros (flotante), ambos ingresados por el usuario.
# Fórmula del IMC: Explica en comentarios dentro de la función cómo se calcula el IMC utilizando la fórmula: IMC = peso / (altura * altura).
# Cálculo del peso ideal: Después de calcular el IMC, muestra también el peso ideal de la persona. Puedes utilizar la fórmula proporcionada: peso ideal = 21.745 * (altura * altura).
# Determinación de la categoría de peso: Basado en el valor del IMC calculado, determina en qué categoría de peso se encuentra la persona. Utiliza los rangos específicos que has definido en la consigna original.
# Salida del programa: Muestra al usuario el valor del IMC calculado, su categoría de peso según los rangos establecidos y su peso ideal.


# Rangos de IMC y Categorías de Peso:

    # Infrapeso: Delgadez Severa: IMC menor a 16.00
    # Infrapeso: Delgadez moderada: IMC mayor a 16.00 y menor a 17.00
    # Infrapeso: Delgadez aceptable: IMC mayor a 17.00 y menor a 18.50
    # Peso normal: IMC mayor a 18.50 y menor a 25.00
    # Sobrepeso: IMC mayor a 25.00 y menor a 30.00
    # Obeso: Tipo I: IMC mayor a 30.00 y menor a 35.00
    # Obeso: Tipo II: IMC mayor a 35.00 y menor a 40.00
    # Obeso: Tipo III: IMC mayor a 40.00

# Puntos adicionales recomendados:

# Agrega comentarios en el código para explicar cada paso y hacerlo más comprensible.
# Añade validación de datos para asegurarte de que el usuario ingrese valores válidos de peso y altura.
# Implementa la posibilidad de que el usuario pueda volver a calcular su IMC con nuevos valores sin necesidad de reiniciar el programa.
# Realiza pruebas con diferentes valores de peso y altura para asegurarte de que el programa funcione correctamente en diferentes casos.




###########################################################################
# #funciones con parametros calcular el IMC con tu peso ideal
###########################################################################

def imc(peso, altura):
    indice = peso / (altura * altura)
    print("#################################################")
    print("el valor del indice es: ", indice)
    pesoideal= 21.745*(altura*altura)

    if indice <16.00:
        print("Infrapeso: Delgadez Severa")
    elif indice > 16.00 and indice <16.99:
        print("Infrapeso: Delgadez moderada")
    elif indice > 17.00 and indice <18.49:
        print("Infrapeso: Delgadez aceptable")
    elif indice > 18.50 and indice <24.99:
        print("peso normal")
    elif indice > 25.00 and indice <29.99:
        print("sobrepeso")
    elif indice > 30.00 and indice <34.99:
        print("Obeso: Tipo I")
    elif indice > 35.00 and indice <39.99:
        print("Obeso: Tipo II")
    elif indice > 40.00:
        print("Obeso: Tipo III")
    else:
        print("algo salio mal")
    
    print("tu peso ideal seria: ", pesoideal)
    print("#################################################")

imc(float(input("ingresa tu peso en kg: ")), float(input("ingresa tu altura en metros: ")))