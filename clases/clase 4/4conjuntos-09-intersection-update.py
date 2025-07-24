# Es exactamente igual al intersection, pero esta función actualiza el set original, 
# es decir, le asigna como nuevo valor los ítems en común. 
# Se escribe como: set1.intersection_update(set2)

# Nota: Ahora set1 vale los ítems en común con set2

set1 = {1,2,3}
print(set1)

set2 = {3,4,5}
print(set2)

set1.intersection_update(set2)
print(set1) # Nota: Ahora set1 vale los ítems en común con set2
# {3}
print(set2) # queda igual
