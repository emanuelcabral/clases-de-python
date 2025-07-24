# Esta función integrada se usa para agregar un ítem a una lista, pero en un índice específico. 

# Se escribe como: lista.insert(posición, ítem). 
lista = [1,2,3,4,5]
print(lista)
#[1,2,3,4,5]
lista.insert(0, 0)
print(lista)
# [0,1,2,3,4,5]
# en el anterior caso agrego el cero en el indice cero

lista2 = [5,10,15,25]
print(lista2)
# [5,10,15,25]
lista2.insert(-1, 20) # Anteúltima posición
print(lista2)
# [5,10,15,20,25]

#si se quiere agregar en la ultima posicion para eso se usa append

lista3 = [5,10,15,25]
print(lista3)
# [5,10,15,25]
n = len(lista3)
print(n)
#4

lista3.insert(n, 30) # Última posición
print(lista3)
# [5,10,15,25,30]
