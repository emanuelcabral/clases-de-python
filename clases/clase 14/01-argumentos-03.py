import sys

# Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales

if len(sys.argv) == 3:  # Verifica si se han pasado exactamente 3 argumentos desde la línea de comandos
    texto = sys.argv[1]  # Se asigna el segundo argumento (texto a imprimir) a la variable texto
    repeticiones = int(sys.argv[2])  # Se convierte el tercer argumento (número de repeticiones) a entero y se asigna a la variable repeticiones
    for r in range(repeticiones):  # Bucle que itera repeticiones veces
        print(texto)  # Imprime el texto tantas veces como indique repeticiones
else:
    print("Error - Introduce los argumentos correctamente")  # Se imprime un mensaje de error si no se pasan exactamente 3 argumentos
    print('Ejemplo: escribir_lineas.py "Texto" 5')  # Se muestra un ejemplo de cómo deberían pasarse los argumentos


# Error - Introduce los argumentos correctamente
# Ejemplo: escribir_lineas.py "Texto" 5

# ejemplo con esto nos repite 4 veces la palabra hola
# clases/clase-14/01-argumentos-03.py "hola" 4