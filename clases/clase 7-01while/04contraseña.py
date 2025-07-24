# Contraseña

# Escribe un programa que pida al usuario una contraseña y la compare con una contraseña predefinida. Si la contraseña no es correcta, debe seguir pidiéndola.

contrasena_correcta = "python123"
contrasena = input("Introduce la contraseña: ")
while contrasena != contrasena_correcta:
    print("Contraseña incorrecta.")
    contrasena = input("Introduce la contraseña: ")
print("¡Acceso concedido!")