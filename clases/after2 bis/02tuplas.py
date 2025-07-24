# Crear una tupla que contenga las estaciones del año
# Mostrar la ubicación de "otoño" usando una función integrada.
# Deben mostrar la longitub de la tupla.
# Con la funcion integrada sorted deberan ordenar la tupla.

# Crear la tupla con las estaciones del año
estaciones = ("primavera", "verano", "otoño", "invierno")
print(estaciones)

# Mostrar la ubicación del "otoño" usando la función integrada index()
ubicacion_otono = estaciones.index("otoño")
print(f"La ubicación de 'otoño' es: {ubicacion_otono}")

# Mostrar la longitud de la tupla usando la función integrada len()
longitud_tupla = len(estaciones)
print(f"La longitud de la tupla es: {longitud_tupla}")

# Ordenar la tupla con la función integrada sorted() (devuelve una lista ordenada)
tupla_ordenada = sorted(estaciones)
print(f"La tupla ordenada es: {tupla_ordenada}")