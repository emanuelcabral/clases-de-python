# Esta función comprueba si el set es subset de otro set, es decir, 
# si todos sus ítems están en el otro conjunto. 

# Se escribe como: set1.issubset(set2)



set3 = {-1,99}
print(set3)

set4 = {1,2,3,4,5}
print(set4)

print(set3.issubset(set4))
# False
# Nota: Devuelve False porque set3 no está todo dentro de set4

print("#################################################")
######################################

#como seria un true?

set33 = {1, 2}
print(set33)

set44 = {1, 2, 3, 4, 5}
print(set44)

print(set33.issubset(set44))
# True - Devuelve verdadero porque 1 y 2 estan dentro del set