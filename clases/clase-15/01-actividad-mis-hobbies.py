# Definimos la ruta donde se almacenará el archivo
ruta = "./"  # Usamos el directorio actual

# Abrimos (o creamos) un archivo de texto en modo escritura
f = open(ruta + "clases/clase-15/mis-hobbies.txt", "w")  # 'f' es una variable que representa el archivo abierto

# La "w" es un modo de escritura. Abre el archivo para escribir.
# Si el archivo ya existe, su contenido se borra. Si el archivo no existe, se crea uno nuevo.

hobbie1 = input("Ingrese el Hobbie1: ")
hobbie2 = input("Ingrese el Hobbie2: ")
hobbie3 = input("Ingrese el Hobbie3: ")

# Escribimos un texto en el archivo
f.write("Hobbie1: " + hobbie1 + "\nHobbie2: " + hobbie2 + "\nHobbie3: " + hobbie3)

f.close()  # Cerramos el archivo para asegurarnos de que los cambios se guarden