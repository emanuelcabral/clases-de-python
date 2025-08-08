import csv  # Importamos el módulo csv

# Ruta al archivo CSV local (debes ajustar esta ruta según donde tengas el archivo)
archivo_csv = "./clases/clase-15/archivos/disney_movies.csv"

# Abrir el archivo CSV en modo lectura ('r') y usar un contexto para garantizar
# que se cierre correctamente después de su uso
with open(archivo_csv, 'r') as archivo:
    contenido_csv = archivo.read()  # Leer todo el contenido del archivo CSV

# Mostrar todo el contenido del archivo CSV
print(contenido_csv)  # Imprimir todo el contenido del archivo CSV