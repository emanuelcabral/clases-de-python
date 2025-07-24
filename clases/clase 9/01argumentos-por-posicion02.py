#Si tomamos el siguiente ejemplo sabremos que la resta nos dará 3:

def resta(a, b):
    return a - b
resultado = resta(15, 12)
print(resultado)

#Pero, si modificamos el orden de los argumentos nos dará otro resultado:

resultado = resta(12, 15)
print(resultado)
