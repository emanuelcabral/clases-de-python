# Esta función encuentra todos los elementos no comunes entre dos set,
# es decir, nos devuelve un set de ítems diferentes entre cada set. 

# Se escribe como: set1.difference(set2)

# Nota: Acá devuelve 1 y 2 por qué le pregunta básicamente “que tengo de diferente al set2?”

set1 = {1,2,3}
print(set1)

set2 = {3,4,5}
print(set2)

print(set1.difference(set2))
# {1,2}
