
#Bucles While

# Descripción de la actividad. 

# Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente utilizando la función input (). 

# Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit(). El programa debe validar dicha acción. 

# Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida.

numeros = int(input("ingrese su numero: "))

while numeros != 0:
    print(numeros)
    otro_numero = input("ingrese otro numero o 'exit' para salir: ")

    if otro_numero == "exit":
        print("haz salido del programa")
        break

    numeros = int(numeros) + int(otro_numero)
    # numeros += otro_numero
