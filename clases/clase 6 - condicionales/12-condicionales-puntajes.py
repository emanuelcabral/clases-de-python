# Clasificación de puntajes

# Escribe un programa en Python que solicite al usuario ingresar un puntaje entre 0 y 100 y determine la calificación correspondiente. Usa las siguientes reglas:

# 90-100: "A"
# 80-89: "B"
# 70-79: "C"
# 60-69: "D"
# 0-59: "F"

puntaje = int(input("Ingresa tu puntaje (0-100): "))

if puntaje >= 90:
    print("Calificación: A")
elif puntaje >= 80:
    print("Calificación: B")
elif puntaje >= 70:
    print("Calificación: C")
elif puntaje >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")