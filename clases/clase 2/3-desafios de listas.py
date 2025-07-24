
# PASO 1: Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras. Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.
# PASO 2: Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
# PASO 3: Luego añade a la lista_2 el <str> "Hola y adiós", y luego el <int> 5555
# PASO 4: Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
# PASO 5: Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
# PASO 6: Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3 


#PASO1:
lista_1 = [1, 2, 3, 4, "texto1", 6 , "ultimo texto"]
lista_2 = [1,"a","b","c",9,10]

print(lista_1)
print(lista_2)

#PASO 2:

##### en este caso estamos conviertiendo al numero en entero
#lista_2.append(int(456789))
#####por default en este caso sera tratado como entero.
lista_2.append(456789)

##### en este caso estamos conviertiendo a string
#lista_2.append(str("Hola Mundo"))
#####por default en este caso sera tratado como string
lista_2.append("Hola Mundo")

#####conclusión para este caso no es necesario aplicar la conversion.

print(lista_2)

#PASO 3
lista_2.append("Hola y adiós")
lista_2.append(5555)
print(lista_2)

#PASO 4

lista_3 = lista_1[0:-1:1]
print(lista_3)

#PASO 5

lista_4 = lista_2[1:-1:1]
print(lista_4)

#PASO 6

lista_5 = lista_3 + lista_4
print(lista_5)
