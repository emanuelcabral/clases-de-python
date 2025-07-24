# Descripción de la actividad. 
#1- A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

#2- El último ítem de tupla
#3- El número de ítems de tupla
#4- La posición donde se encuentra el ítem 87 de tupla
#5- Una lista con los últimos tres ítems de tupla
#6- Un ítem que haya en la posición 8 de tupla
#7- El número de veces que el ítem 7 aparece en tupla

# Copia esta tupla para iniciar el ejercicio:
# tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

#1
tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)
#2
print(tupla[-1])
#3
print(len(tupla))
#4
print(tupla.index(87))
#5
print(tupla[-3:])
#6
print(tupla[7])
#7
print(tupla.count(7))