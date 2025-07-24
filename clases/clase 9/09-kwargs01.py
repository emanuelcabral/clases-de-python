#Podemos ver que es posible iterar los argumentos de entrada con items(), y podemos acceder a la clave key (o nombre) y el valor o value de cada argumento.


def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s

resultado = suma(a=3, b=10, c=3)
#salida
#a = 3
#b = 10
#c = 3
print(resultado)
#16

# **kwargs seria como una caja donde puedes meter muchos argumentos con nombre (como un diccionario)