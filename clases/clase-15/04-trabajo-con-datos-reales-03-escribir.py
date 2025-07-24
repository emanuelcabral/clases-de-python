import csv  # Importamos el módulo csv

# Definir los datos a escribir en el archivo CSV
datos = [
    ['Día', 'Clases', 'Materia'],        # Encabezados de las columnas
    ['Lunes', 'No hay clases', 'estas libre'],          # Datos para el día Lunes
    ['Martes', 'Si', 'Python'],         # Datos para el día Martes
    ['Miércoles', 'No hay clases', 'estas libre'],      # Datos para el día Miércoles
    ['Jueves', 'Si', 'Python'],         # Datos para el día Jueves
    ['Viernes', 'No hay clases', 'estas libre'],        # Datos para el día Viernes
    ['Sábado', 'No hay clases', 'estas libre'],         # Datos para el día Sábado
    ['Domingo', 'No hay clases', 'estas libre']         # Datos para el día Domingo
]

# Ruta donde se creará el archivo CSV (ajusta la ruta según tu necesidad)
archivo_csv = "./clases/clase-15/archivos/horario_clases_con_python.csv"

# Abrir el archivo CSV en modo escritura ('w') con newline='' para evitar líneas en blanco adicionales
with open(archivo_csv, 'w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)  # Crear un objeto escritor de CSV asociado al archivo abierto
    
    escritor_csv.writerows(datos)  # Escribir todas las filas de datos en el archivo CSV utilizando writerows()

print(f'Se ha creado el archivo CSV "{archivo_csv}" con éxito.')  # Mensaje de confirmación
