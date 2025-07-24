# Eres un numero divisible?

# Escribe un programa en Python que solicite al usuario ingresar un número y determine e imprima si ese número es divisible por 7 o no. Si el número ingresado es divisible por 7, el programa deberá imprimir "Es divisible por 7". En caso contrario, deberá imprimir "No es divisible por 7".

numero= int(input("ingresa un numero para saber si es divisible por 7: "))
resto = numero % 7
if resto == 0:
    print("es divisible por 7")
else:
    print("no es divisible")