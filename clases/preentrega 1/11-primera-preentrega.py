# Diccionario para almacenar los usuarios y contraseñas
usuarios = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    if usuario in usuarios:
        print("El nombre de usuario ya está en uso. Por favor, elija otro.")
        return
    
    contraseña = input("Ingrese contraseña: ")
    usuarios[usuario] = contraseña
    print(f"Usuario '{usuario}' registrado con éxito.")

# Función para mostrar la información de los usuarios registrados
def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for usuario, contraseña in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")

# Función para el inicio de sesión
def login():
    usuario = input("Ingrese nombre de usuario: ")
    if usuario not in usuarios:
        print("El nombre de usuario no existe.")
        return
    
    contraseña = input("Ingrese contraseña: ")
    if usuarios[usuario] == contraseña:
        print(f"Inicio de sesión exitoso. ¡Bienvenido, {usuario}!")
    else:
        print("Contraseña incorrecta.")

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Ejecutar el menú
menu()