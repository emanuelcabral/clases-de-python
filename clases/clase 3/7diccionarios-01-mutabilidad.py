#Los diccionarios al igual que las listas son mutables, 
#es decir, que podemos reasignar sus ítems haciendo referencia con el índice.



colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores)

#mutamos el valor
colores[" amarillo"] = " white "
print(colores[" amarillo"])
# "white"

#solo se pueden modificar los valores no las keys. Ya que las keys son inmutables.