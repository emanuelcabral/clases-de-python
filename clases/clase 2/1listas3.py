# Las listas son muy parecidas a los strings, ya que funcionan exactamente igual respecto al índice y el slicing

datos = [1, -5, 123, 34, "Una cadena", "Otra cadena", "Pepito"]

###indice

print(datos[2])
# 123
print(datos[-1])
# 'Pepito'

###slicing

print(datos[-2:])
# ['Otra cadena', 'Pepito']
