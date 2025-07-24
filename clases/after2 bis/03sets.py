# Deberan crear un conjunto con los valores de 20,30,40,60,70
# Deben agregar el valor de 50 con alguna funcion integrada
# Se debe eliminar el valor de 60
# Se debera elimiar el valor de 90
# Por ultimo eliminar todo el conjunto




















# Crear un conjunto con los valores 20, 30, 40, 60, 70
conjunto = {20, 30, 40, 60, 70}
print(conjunto)

# Agregar el valor de 50
conjunto.add(50)
print(conjunto)

# Eliminar el valor de 60
conjunto.remove(60)
print(conjunto)

# Eliminar el valor de 90 (usamos discard para evitar error si no está presente)
conjunto.discard(90)
print(conjunto)

# Eliminar todo el conjunto
conjunto.clear()
print(conjunto)
