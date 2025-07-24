# Similar al difference, pero esta función nos guarda los ítems distintos en el set originales, es decir, le asigna como nuevo valor los ítems diferentes. 
# Se escribe como: set1.difference_update(set2)



set1 = {1,2,3}
print(set1)
# {1,2,3}

set2 = {3,4,5}
print(set2)
# {3,4,5}

set1.difference_update(set2)
print(set1)
# {1,2}

print("estos son los valores que almacena set1 y luego set2")
print(set1) # Nota: Ahora set1 vale {1,2} porque es la diferencia que tenía con set2
# {1, 2}
print(set2)
# {3, 4, 5}
