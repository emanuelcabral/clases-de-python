# La función items es similar a keys y values, 
# pero esta crea una lista con clave y valor de los ítems de un diccionario. 

#se utiliza para obtener una vista de los pares clave-valor en un diccionario. La vista devuelta es un objeto que proporciona una representación de todos los pares clave-valor presentes en el diccionario. Esta vista es dinámica, lo que significa que si el diccionario cambia, la vista también se actualizará automáticamente.

# Se escribe como: dict.items()

colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
print(colores)
# { "amarillo":"yellow", "azul":"blue", "verde":"green" }

print(colores.items())
# dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])

#convierte el diccionario en una lista de tuplas↑↑↑

#debajo se genera un bucle donde agrupa en dos columas una de keys y otra de valores buscando nuestro diccionario con sus items

for clave, valor in colores.items():
    print(clave, valor)
    
# amarillo yellow
# azul blue
# verde green
