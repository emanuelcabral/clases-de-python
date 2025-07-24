# Consigna:
# Escribe un programa en Python que genere la tabla de multiplicar de un número ingresado por el usuario.

# Instrucciones:

# El usuario debe ingresar un número entero.
# El programa debe generar y mostrar la tabla de multiplicar de ese número desde 1 hasta 10.


def generar_tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número entero: "))
generar_tabla_multiplicar(numero)