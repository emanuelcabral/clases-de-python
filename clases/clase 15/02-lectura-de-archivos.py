# Abrimos el archivo en modo lectura y leemos su contenido
ruta = "./clases/clase-15/mis-hobbies.txt"  # Definimos la ruta del archivo a leer

# Abrimos el archivo en modo lectura y leemos su contenido
with open(ruta, "r") as f: # Se abre el archivo especificado por 'ruta' en modo lectura ("r")
    contenido = f.read()  # Se lee todo el contenido del archivo y se guarda en la variable 'contenido'
    print("Contenido del archivo:") # Se imprime un mensaje indicando que se mostrará el contenido del archivo
    print(contenido) # Se imprime el contenido del archivo


# la palabra clave with en Python se utiliza para gestionar contextos, 
# como abrir y cerrar archivos de forma segura.

# la funcion open(ruta, "r"): Abre el archivo en modo lectura.

# la palabra clave as f: Asigna el archivo abierto a la variable f.

# la funcion .read lee el archivo