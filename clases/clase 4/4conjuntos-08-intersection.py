# Esta función devuelve un set con todos los elementos comunes entre dos set, 
# es decir, nos devuelve un set de ítems iguales entre cada set. 

# Se escribe como: set1.intersection(set2)



set1 = {1,2,3}
print(set1)
#{1,2,3}

set2 = {3,4,5}
print(set2)
#{3,4,5}

print(set1.intersection(set2))
# {3}

#si no hay interseccion nos devuelve set()

print(set2.intersection(set1))
# {3}