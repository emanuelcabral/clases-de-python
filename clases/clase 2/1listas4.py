#Otro punto  en el que se parecen las listas a los strings, es que en ambos se puede concatenar, en este caso se concatenan listas.


datos = [1, -5, 123, 34, "Una cadena", "Otra cadena"]
print(datos)
datos += [0, "Otra cadena distinta", "Pepito", -873758, 123]
print(datos)
# [1, -5, 123, 34, 'Una cadena', 'Otra cadena', 0,'Otra cadena distinta', 'Pepito', -873758, 123]

##############################################################

numeros = [1, 2, 3, 4]
numeros += [5, 6, 7, 8]
print(numeros)
# [1, 2, 3, 4, 5, 6, 7, 8]
