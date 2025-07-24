# Consigna

#PASO 1: A partir de una lista realizar las siguientes tareas sin modificar la lista original:

#PASO 2: Borrar los elementos duplicados
#PASO 3: Ordenar la lista de mayor a menor
#PASO 4: Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
#PASO 5: Realizar una suma de todos los números que quedan (sum(lista))
#PASO 6: Añadir como primer elemento de la lista la suma realizada insert(0, suma)
#PASO 7: Devolver la lista modificada
#Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

# lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
# Nota: Recuerda que para sumar todos los números de una lista puedes usar sum



###------------paso1--------------###
#crear lista
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

###------------paso2--------------###
#eliminar valores duplicados convirtiendo a un set
lista = set(lista)
print(lista)

#vuelvo a convertir a lista
lista = list(lista)
print(lista)

###------------paso3--------------###
lista.sort() # con sort ordenamos de menor a mayor
print(lista)

###------------paso4--------------###

for num in lista[:]:  # Iteramos sobre una copia de la lista original
    if num % 2 == 1:  # Le pregunta si el numero al dividirlo por dos tiene un resto = 1 - De esa forma sabemos si es impar.
        lista.remove(num)  # Lo eliminamos de la lista original
        #lista.pop(lista.index(num)) # otra alternativa con el pop
print(lista)

###------------paso5--------------###
#sumanos todo con la funcion sum
suma = sum(lista)
print("Suma de los números es:", suma)

###------------paso6--------------###
#insertamos la suma realizada en el indice 0
lista.insert(0, suma)

###------------paso7--------------###
#mostramos la lista
print(lista)
