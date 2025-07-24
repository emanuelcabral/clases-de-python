# Como vimos en las listas, podemos sumar una lista con otra lista de la siguiente forma

numeros = [1,2,3,4]
print(numeros)

print(numeros + [5,6,7,8])


# Pero también podemos hacer uso de extend, ya que une una lista con otra. 

# Se usa como lista.extend(otra_lista)

lista1 = [1,2,3,4]
print(lista1)
# [1,2,3,4]

lista2 = [5,6,7,8]
print(lista2)
# [5,6,7,8]

lista1.extend(lista2)
print(lista1)
# [1,2,3,4,5,6,7,8]

# lista2.extend(lista1)
# print(lista2)