#Veamos aquí como *args puede ser iterado, ya que en realidad es una tupla. 
#Por lo tanto iterando la tupla podemos acceder a todos los argumentos de entrada, y en nuestro caso sumarlos y devolverlos.


def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

print(suma(1,3,4,2))
#salida 10


print(suma(1,1))
#salida 2

# *args seria como una caja donde puedes meter muchos argumentos sin nombre (como una lista)