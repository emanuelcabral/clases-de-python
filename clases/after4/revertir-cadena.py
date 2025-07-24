# Revertir una cadena:

# Consigna: Escribe un programa que revierta la cadena "Python" y muestre el resultado.

cadena = "Python"
cadena_revertida = ""
for caracter in cadena:
    cadena_revertida = caracter + cadena_revertida
print("Cadena revertida:", cadena_revertida)