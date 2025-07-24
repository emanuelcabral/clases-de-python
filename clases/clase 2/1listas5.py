#hay una diferencia entre listas y string, los strings son inmutables, 
#pero, las listas son mutables, esto significa que si podemos reasignar sus ítems haciendo referencia con el índice

pares =  [0, 2, 4, 5, 8, 10]
pares[3] = 6
print(pares)
# [0, 2, 4, 6, 8, 10]
