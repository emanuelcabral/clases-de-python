# La función get sirve para poder buscar un elemento a partir de su key, 
# en el caso de no encontrar devuelve un valor por defecto que le indicamos nosotros. 
# Se escribe como: dict.get(key, "valor por defecto")

colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
print(colores)
# { "amarillo":"yellow", "azul":"blue", "verde":"green" }

print(colores.get("rojo", "no hay clave rojo"))
# "no hay clave rojo"  #Como no hay key rojo devuelve este valor

print(colores.get("amarillo", "no hay clave amarillo"))
# "yellow" # en este caso como hay key amarillo nos devuelve el valor de esa key
