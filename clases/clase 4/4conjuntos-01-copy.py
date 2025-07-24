# Esta función integrada sirve para hacer que se devuelva una copia de un set. 


# Se escribe como: set.copy()

set1 = {1,2,3,4}
print(set1)
# {1,2,3,4}

set2 = set1.copy()
print(set2)
# {1,2,3,4}

###pero para que sirve hacer una copia, no es lo mismo que realizar una asignacion ??????####

#Diferencia entre copy y asignacion
#copy() crea una copia independiente del conjunto original, la asignación directa simplemente crea una nueva referencia al mismo conjunto en la memoria. Dependiendo del escenario, puede ser crucial mantener la independencia de los conjuntos, y en esos casos, copy() es la opción adecuada.

print("---------------")
a = {1, 2, 3}
b = a.copy()  # Copia del conjunto
b.add(4)
print(a)  # Resultado: {1, 2, 3}
print(b)  # Resultado: {1, 2, 3, 4}