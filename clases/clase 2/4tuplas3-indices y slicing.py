# Como las listas, las tuplas funcionan exactamente igual con el índice y el slicing.

#tuplas - indice

datos = (1, "2", [3, "4"], (5, "6"))
print(datos[1])
# '2'
más_datos = datos[-1]
print(más_datos)
# (5, '6')

#tuplas - slicing

print(datos[2:])
# ([3, '4'], (5, '6'))
