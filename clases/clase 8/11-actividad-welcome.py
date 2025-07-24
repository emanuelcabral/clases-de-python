#Escribir una función a la que se le pase una cadena del nombre de una ciudad <ciudad> y muestre por pantalla el saludo ¡hola bienvenidx a <nombre>!.


# def bienvenidx(ciudad):
#     print('¡Hola bienvenidx a ' + ciudad +'!')
#     # return

# bienvenidx('Ciudad de Mexico')


def bienvenidx(ciudad):
    mensaje = "¡Hola bienvenidx a " + ciudad + "!"
    return mensaje

print(bienvenidx('Ciudad de Mexico'))