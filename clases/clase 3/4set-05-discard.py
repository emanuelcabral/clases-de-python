# Si add te deja agregar un ítem al set, discard hace todo lo contrario,
# elimina el ítem del set, sin modificar el resto del set,
# si el elemento pasado como argumento a discard() no está dentro del conjunto es simplemente ignorado.

numeros =  {1, 2, 3, 4}
print(numeros)
numeros.discard(2)
print(numeros)
# {1, 3, 4}

datos = {1, -5, 123.34, "Una cadena", "Otra cadena"}
print(datos)
datos.discard("Otra cadena")
print(datos)
# {1, -5, 123,34, "Una cadena"}

#intentemos eliminar un dato que no se encuentra en el set
datos.discard("una")
print(datos)
# {1, -5, 123,34, "Una cadena"}