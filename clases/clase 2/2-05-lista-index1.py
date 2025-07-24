# Las listas pueden utilizar la función index. 
# Esta función busca un elemento y nos dice en qué índice se encuentra.

números = [1, 2, 1, 3, 1, 4, 1, 5, 1]
print(números.index(5))
# 7

#Si selecciono el valor de 1 que se encuentra mas de una vez en la lista, solo muestra la primera ubicacion.
print(números.index(1))
#0
#Si se llama nuevamente el resultado sera el mismo.
print(números.index(2))
#1

#Es útil para verificar la existencia de elementos
# Si el elemento no está presente en la lista, index() genera un error ValueError.