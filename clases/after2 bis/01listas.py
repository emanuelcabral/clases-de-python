# Crear una lista que contenga todos los dias de la semana.
# Eliminar el ultimo valor de la lista para eso debes usar una funcion integrada
# Eliminar el dia martes y jueves de la lista con otra funcion integrada
# Utiliza append, extend o insert para agregar los valores faltantes de los dias de la semana
# Por ultimo contabilizar con una funcion integrada la longitud de la lista





# Crear una lista que contenga todos los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Lista inicial:", dias_semana)

# Eliminar el último valor de la lista (Domingo) usando una función integrada (pop)
dias_semana.pop()
print("eliminar el último día:", dias_semana)

# Eliminar Martes y Jueves usando una función integrada (remove)
dias_semana.remove("Martes")
dias_semana.remove("Jueves")
print("eliminar Martes y Jueves:", dias_semana)

# Agregar los días faltantes usando append, extend o insert
dias_semana.append("Martes")  # Agregar Martes al final
dias_semana.insert(3, "Jueves")  # Insertar Jueves en la posición correcta (índice 3)
dias_semana.append("Domingo")  # Agregar Domingo al final
print("agregar los días faltantes:", dias_semana)

# Contabilizar la longitud de la lista usando len()
longitud_lista = len(dias_semana)
print("La longitud de la lista es:", longitud_lista)