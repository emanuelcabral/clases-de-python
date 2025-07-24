#pop elimina el último ítem de una lista, sin modificar el resto de la lista. 

numeros = [1, 2, 3, 4]
numeros.pop()
print(numeros)
# [1, 2, 3]

datos = [1, -5, 123, 34, "Una cadena", "Otra cadena"]
datos.pop()
print(datos)
# [1, -5, 123, 34, 'Una cadena']


##############################################################

datos2 = [1, -5, 123, 34, "Una cadena", "Otra cadena"]
#para eliminar un item en especial que no necesariamente sea el ultimo se puede especificar con el indice
datos2.pop(4)
print(datos2)
# [1, -5, 123, 34, 'Otra cadena']

# la diferencia de remove(), 
#es que solo elimina el primer elemento que coincida con un valor dado, ademas si quieres eliminar un valor en concreto remove es la mejor opcion.
#En cambio pop() devuelve el elemento eliminado, lo que te permite realizar operaciones adicionales con él si es necesario. Con pop eliminamos el numero de item deseado.
