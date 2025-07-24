
# Esta función comprueba si el set es distinto a otro set, 
# es decir, si no hay ningún ítem en común entre ellos. 
# Se escribe como: set1.isdisjoint(set2)


# Nota: Devuelve False porque set1 y set2 comparten el 3

set1 = {1,2,3}
print(set1)

set2 = {3,4,5}
print(set2)

print(set1.isdisjoint(set2))
# False - el set no es distinto ya que comparten el 3

####################################

set3 = {1,2,3}
print(set3)

set4 = {4,5,6}
print(set4)

print(set3.isdisjoint(set4))
# True - el set es distinto ya que no hay ningun item que compartan
