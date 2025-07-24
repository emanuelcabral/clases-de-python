#Para añadir múltiples elementos a un set se usa la función update(), 
#que puede tomar como argumento una lista, tupla, string, conjunto o cualquier objeto de tipo iterable. 

numeros =  {1,2,3,4}
#actualizamos al set con el ingreso de una lista
numeros.update([5,6,7,8])
# numeros.update(5,6,7,8)
print(numeros)
#{1, 2, 3, 4, 5, 6, 7, 8}

#con range podemos definir que se agregue un cierto rango desde donde hasta donde. El inicio es inclusivo y el fin no lo es.
numeros.update(range(9,12))
print(numeros)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}