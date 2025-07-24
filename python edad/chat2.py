users = {}

def register():
    while True:
        username = input("Ingresa un nombre de usuario: ")
        if username in users:
            print("El nombre de usuario ya existe, intenta con otro.")
        else:
            password = input("Ingresa una contraseña: ")
            users[username] = password
            print(f"Usuario '{username}' registrado exitosamente.")
            break

def login():
    while True:
        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu contraseña: ")
        if username in users and users[username] == password:
            print(f"Bienvenido/a, {username}!")
            break
        else:
            print("Nombre de usuario o contraseña incorrectos. Intenta nuevamente.")

# Ejemplo de uso
while True:
    action = input("Ingresa 'r' para registrar un nuevo usuario, 'l' para hacer login, o 'q' para salir: ")
    if action == 'r':
        register()
    elif action == 'l':
        login()
    elif action == 'q':
        break
    else:
        print("Acción no reconocida. Intenta nuevamente.")
