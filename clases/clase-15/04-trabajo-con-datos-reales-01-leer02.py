import csv

# Ruta al archivo CSV local (ajusta la ruta según donde tengas el archivo)
archivo_csv = "./clases/clase-15/archivos/disney_movies.csv"

# Diccionario para contar las ocurrencias de los títulos de películas
conteo_peliculas = {}

# Abrir el archivo CSV en modo lectura
with open(archivo_csv, 'r', encoding='utf-8') as archivo:
    # Crear un lector CSV
    lector_csv = csv.reader(archivo)
    
    # Saltar la primera línea (encabezados) si es necesario
    next(lector_csv)
    
    # Iterar sobre las filas del archivo CSV
    for fila in lector_csv:
        # Obtener el título de la película de la columna correspondiente
        titulo_pelicula = fila[0]  # Ajusta el índice según la ubicación de la columna en tu CSV
        
        # Contar el título de la película en el diccionario
        if titulo_pelicula in conteo_peliculas:
            conteo_peliculas[titulo_pelicula] += 1
        else:
            conteo_peliculas[titulo_pelicula] = 1

# Mostrar los resultados
for titulo, conteo in conteo_peliculas.items():
    print(f"{titulo}: {conteo}")