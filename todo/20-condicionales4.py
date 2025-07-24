año= int(input("ingresa el año que te encuentras para determinar si es bisiesto: "))
resto = año % 4
if resto == 0:
    print("es un año bisiesto")
else:
    print("no es año bisiesto")