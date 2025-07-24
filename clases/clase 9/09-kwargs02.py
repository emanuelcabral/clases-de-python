#El uso de los **kwargs es muy útil si además de querer acceder al valor de las variables dentro de la función, quieres darles un nombre que de una información extra.
#Pensar como un diccionario.


def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s

resultado = suma(a=3, b=10, c=3, d=11)
#salida
#a = 3
#b = 10
#c = 3
print(resultado)
#16

# **kwargs seria como una caja donde puedes meter muchos argumentos con nombre (como un diccionario)