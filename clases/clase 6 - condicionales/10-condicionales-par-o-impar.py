# número par o impar

# Escribe un programa en Python que solicite al usuario ingresar un número entero y determine si el número es par o impar. Si el número es par, el programa debe imprimir "El número es par". En caso contrario, debe imprimir "El número es impar".

numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")