#Sin embargo, hay que tener en cuenta que la función termina al devolver un valor, 
#es decir, lo que escribamos después no se ejecutará:


def saludar_con_nombre(nombre):
    saludando = print('Hola {}! ¿Cómo estás?'.format(nombre))
    return saludando
    print("Hola Mundo")


# ¡Es similar a un break!

saludar_con_nombre("Juan")

# Si modificamos el return debajo del ultimo print se mostraran todos los prints y no solo uno.