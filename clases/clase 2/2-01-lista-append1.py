# Esta función permite agregar un nuevo ítem al final de una lista.

#Acepta un único argumento que es el elemento que se va a agregar a la lista.

numeros = [1, 2, 3, 4]
numeros.append(5)
print(numeros)
# [1, 2, 3, 4, 5]

#si quisieramos agregar un valor en otra ubicacion
numeros2 = [1, 5 , 8, 20, 35]
print(numeros2)

#insert(indice, valor)
numeros2.insert(2,100)
print(numeros2)
