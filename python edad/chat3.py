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

def show_users():
    print("Usuarios registrados:")
    for username, password in users.items():
        print(f"Nombre de usuario: {username}, Contraseña: {password}")

# Ejemplo de uso
while True:
    action = input("Ingresa 'r' para registrar un nuevo usuario, 'l' para hacer login, 's' para ver la lista de usuarios o 'q' para salir: ")
    if action == 'r':
        register()
    elif action == 'l':
        login()
    elif action == 's':
        show_users()
    elif action == 'q':
        break
    else:
        print("Acción no reconocida. Intenta nuevamente.")
