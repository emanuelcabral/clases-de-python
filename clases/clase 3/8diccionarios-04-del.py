# Del elimina el ítem del dict, sin modificar el resto del dict, 
# si el elemento pasado como argumento a del() no está dentro del dict es simplemente ignorado.

# Se escribe como del mi_dict[“clave”].


numeros =  {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
print(numeros)

#Se elimina el item dos llamando por su key
del numeros['dos']
print(numeros)
# {'uno': 1, 'tres': 3, 'cuatro': 4}

#si eliminamos una llave inexistente nos arroja un error.
# del numeros['cinco']
# print(numeros)