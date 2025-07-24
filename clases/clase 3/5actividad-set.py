# Descripción de la actividad. 

# Trabajaremos con el notebook de la sesión, específicamente sobre la temática de Sets. 
# Crear un conjunto en Python que posea los siguientes elementos: 

# Colores: Rojo, Blanco, Azul.
# Posteriormente, agrega nuestro set de colores, los valores de: Violeta y Dorado
# Elimina a los colores: Celeste, Blanco y Dorado

# Pregunta: ¿Qué pasa si queremos eliminar el color Celeste utilizando el método discard?


colores = {"Rojo", "Blanco", "Azul"}
print(colores)

# colores.add("Violeta", "Dorado") ← No se puede agregar mas de un item.
colores.add("Violeta")
colores.add("Dorado")
print(colores)

#otra forma de agregar mas de un item ↓↓↓

# colores.update(["Violet", "gold"])
# print(colores)


# colores.discard("Celeste", "Blanco" ,"Dorado") ← No se puede agregar mas de un item.
colores.discard("Celeste")
colores.discard("Blanco")
colores.discard("Dorado")
print(colores)

#Como se puede apreciar al descartar el color Celeste no sucede nada porque no estaba dentro del set
