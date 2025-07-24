#Es año bisiesto o no?

# Escribe un programa en Python que solicite al usuario ingresar un año y determine e imprima si ese año es bisiesto o no. Si el año ingresado es divisible por 4 pero no por 100, o es divisible por 400, el programa deberá imprimir "Es un año bisiesto". En caso contrario, deberá imprimir "No es un año bisiesto". 

año= int(input("ingresa el año que te encuentras para determinar si es bisiesto: "))
resto = año % 4
if resto == 0:
    print("es un año bisiesto")
else:
    print("no es año bisiesto")