# En Python, podemos convertir una lista a una tupla haciendo uso de la función tuple() y a su vez, podemos hacer lo mismo, pero a la inversa, es decir, convertir una tupla a lista usando la función list().

#de tupla a lista
numeros = (1, 2, 3, 4)
numeros = list(numeros)
print(numeros)
# [1, 2, 3, 4]

#de lista a tupla
datos = [1, -5, 123.34, "Una cadena", "Otra cadena"]
datos = tuple(datos)
print(datos)
# (1, -5, 123.34, 'Una cadena', 'Otra cadena')
