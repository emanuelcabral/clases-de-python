# Clasificación de temperaturas

# Escribe un programa en Python que solicite al usuario ingresar una temperatura en grados Celsius y determine si la temperatura es "Alta", "Moderada" o "Baja". Considera temperaturas mayores o iguales a 30°C como "Alta", temperaturas entre 15°C y 29°C como "Moderada", y temperaturas menores a 15°C como "Baja".

temperatura = float(input("Ingresa la temperatura en grados Celsius: "))

if temperatura >= 30:
    print("Temperatura Alta")
elif temperatura >= 15:
    print("Temperatura Moderada")
else:
    print("Temperatura Baja")