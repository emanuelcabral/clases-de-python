# Determinar la categoría de edad

# Escribe un programa en Python que solicite al usuario ingresar su edad y determine su categoría de acuerdo con la siguiente clasificación:

# Menor de 12: "Niño"
# Entre 13 y 17: "Adolescente"
# Entre 18 y 64: "Adulto"
# 65 o más: "Adulto mayor"

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Categoría: Niño")
elif edad <= 17:
    print("Categoría: Adolescente")
elif edad <= 64:
    print("Categoría: Adulto")
else:
    print("Categoría: Adulto mayor")