#Las listas pueden utilizar la función count. 
#Esta función cuenta el número de veces que se repite un elemento en una lista.

números = [1, 2, 1, 3, 1, 4, 1]
print(números.count(1))
# 4

# Si el elemento no está presente en la lista, count() devuelve cero.

números = [1, 2, 1, 3, 1, 4, 1, "hola"]
print(números.count("hola"))