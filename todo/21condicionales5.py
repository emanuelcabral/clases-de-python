numero= int(input("ingresa un numero para saber si es divisible por 7: "))
resto = numero % 7
if resto == 0:
    print("es divisible por 7")
else:
    print("no es divisible")