#Lo que hacemos para indicar que se reciben valores es crear dos variables separadas por una coma. 
#Cuando nosotros llamemos a la función, automáticamente, se le asignarán a estas variables los números que enviemos, siguiendo el mismo orden:

def suma(numero1, numero2):
    return numero1 + numero2

r = suma(7, 5) # se asigna la funcion suma a la variable r
# En este caso 7 será la variable numero1 y 5 será la variable numero2

#que sucede si invertimos los valores?
#que sucede cambiamos la operacion a resta e invertimos los valores?

print(r) # se lanza el print con la varible r