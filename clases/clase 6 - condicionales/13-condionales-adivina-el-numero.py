# Adivinar el número

# Escribe un programa en Python que tenga un número secreto (puedes definirlo tú mismo) y pida al usuario adivinar el número. El programa debe decirle al usuario si su suposición es "Demasiado alta", "Demasiado baja" o "¡Correcta!".

numero_secreto = 42  # Puedes cambiar este número si lo deseas
adivinanza = int(input("Adivina el número secreto: "))

if adivinanza > numero_secreto:
    print("Demasiado alta")
elif adivinanza < numero_secreto:
    print("Demasiado baja")
else:
    print("¡Correcta!")