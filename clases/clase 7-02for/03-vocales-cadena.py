# Imprimir las vocales de una cadena:

# Consigna: Escribe un programa que imprima todas las vocales presentes en la cadena "Programación en Python".

cadena = "Programación en Python"
vocales = "aeiouAEIOU"
for caracter in cadena:
    if caracter in vocales:
        print(caracter)