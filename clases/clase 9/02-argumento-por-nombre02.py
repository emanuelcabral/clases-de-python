#Recordemos que al utilizar argumentos por nombre, no importa el orden:

def resta(a, b, c):
    return a - b - c
resultado = resta(a=15, b=12, c=2)
print(resultado)

resultado = resta(c=2, a=15, b=12)
print(resultado)
