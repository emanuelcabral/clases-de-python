# Crear un diccionario vacío para almacenar usuarios y contraseñas
users = {}

def register():
    # Pedir al usuario que ingrese un nombre de usuario y una contraseña
    username = input("Ingresa un nombre de usuario: ")
    password = input("Ingresa una contraseña: ")
    # Verificar si el nombre de usuario ya existe
    if username in users:
        print("El nombre de usuario ya existe, intenta con otro.")
    else:
        # Agregar el nuevo usuario al diccionario
        users[username] = password
        print("¡Registro exitoso!")

def login():
    # Pedir al usuario que ingrese su nombre de usuario y contraseña
    username = input("Ingresa tu nombre de usuario: ")
    password = input("Ingresa tu contraseña: ")
    # Verificar si el nombre de usuario y contraseña coinciden con los datos almacenados
    if username in users and users[username] == password:
        print("¡Inicio de sesión exitoso!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Ejemplo de uso
register()
login()