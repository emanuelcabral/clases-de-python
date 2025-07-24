import os

users = {}

def menu():
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("\nIngrese una opción: ")
    return opcion

def registro():
    nombre = input("\nIngrese su nombre: ")
    contrasena = input("Ingrese su contraseña: ")
    users[nombre] = contrasena
    print("\n¡Registro exitoso!")

def inicio_sesion():
    nombre = input("\nIngrese su nombre: ")
    contrasena = input("Ingrese su contraseña: ")
    if nombre in users and users[nombre] == contrasena:
        print("\n¡Inicio de sesión exitoso!")
    else:
        print("\nNombre de usuario o contraseña incorrectos.")

while True:
    opcion = menu()

    if opcion == "1":
        registro()

    elif opcion == "2":
        inicio_sesion()

    elif opcion == "3":
        print("\n¡Hasta luego!")
        break

    else:
        print("\nOpción inválida. Intente de nuevo.")

filename = "users.txt"

with open(filename, "w") as file:
    for nombre, contrasena in users.items():
        file.write(f"{nombre}:{contrasena}\n")

print(f"\nBase de datos guardada en el archivo {filename}")