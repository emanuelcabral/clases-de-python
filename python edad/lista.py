lista = [1,2,3,4,5]
# lista2 = lista.pop()
# print(lista2)
tupla = (8,15,4,39,5,89,87,19,7,-755,88,123,2,11,15,9,355)
milista= list(tupla)
milista = milista.pop()
print("Mi último elemento:" , milista)

micuenta = len(tupla)
print("la cantidad de numero de items de mi tupla: " , micuenta)
# posicion
posicion = tupla.index(87)
print("la posicion donde se encuentra el numero 87 :",posicion)

miultimos3 = tupla[-4:-1:1]
print("los ultimos 3: ",miultimos3)


posicion2 = tupla[8]
print("la posicion 8 :",posicion2)

posicion7 = tupla.count(7)
print("la cantidad de veces del 7 :",posicion7)
