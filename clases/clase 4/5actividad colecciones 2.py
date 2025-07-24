# Analizar e interpretar los siguientes conjuntos en Python

# ¡Importante! 
# Ejecuta el código para analizar cada una de las salidas! 

# Ejemplo 1:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.union(my_set_2)
print(my_new_set)
# {1, 2, 3, 4, 5}
#se puede apreciar la union entre estos dos conjuntos por medio de la funcion union

# Ejemplo 2:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.intersection(my_set_2)
print(my_new_set)
# {3}
#Se puede apreciar que nos devuelve el valor de 3 ya que es el valor comun entre ambos sets

# Ejemplo 3:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.difference(my_set_2)
print(my_new_set)
# {1, 2}
#Se puede apreciar que nos devuelve 1 y 2 porque son los valores distintos entre ambos sets
#cual es la diferencia del set 1 con el set dos y le indica que no posee el 1 y 2
