# Esta función es muy similar al issubset, la diferencia es que esta comprueba si el set es contenedor de otro set, es decir, si contiene todos los ítems de otro set. 


# Se escribe como: set1.issuperset(set2)


set5 = {1,2,3}
print(set5)

set6 = {1,2}
print(set6)

print(set5.issuperset(set6))
# True - Es verdadero porque contiene todos los items del set 6 (1 y 2)

##########################################################################

set5 = {1, 2, 3}
print(set5)

set6 = {1, 2, 4}  
print(set6)

print(set5.issuperset(set6))
# False - Es falso porque no contiene todos los items del set al agregarle el item 4 que no esta