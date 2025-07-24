# Al igual que las listas, las tuplas pueden utilizar la función index. Esta función busca nuestro ítem y nos dice en qué índice se encuentra.

números = (1, 2, 1, 3, 1, 4, 1, 5)
índice = números.index(5)
print(índice)
# 7

# Si intentas buscar un valor fuera de la tupla, Python devolverá un error y que no se encontró el valor: Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: tuple.index(x): x not in tuple
