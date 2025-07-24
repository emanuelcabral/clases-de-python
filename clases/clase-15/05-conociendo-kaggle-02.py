# import pandas as pd
# import numpy as np

# # Ruta local al archivo CSV (ajústala según donde tengas guardado tu archivo)
# ruta_csv = "./clases/clase-15/archivos/puntos_digitales.csv"

# # Abrir el archivo CSV usando pandas
# ejemplo2 = pd.read_csv(ruta_csv)

# # Mostrar las primeras filas del DataFrame para verificar la correcta lectura
# print(ejemplo2.head())



# try:
#     import pandas as pd
#     import numpy as np
# except ImportError:
#     import os
#     os.system('pip install pandas numpy')

# # Una vez instaladas, puedes proceder a leer el archivo CSV
# ruta_csv = "./clases/clase-15/archivos/puntos_digitales.csv"  # Ajusta la ruta según corresponda
# ejemplo2 = pd.read_csv(ruta_csv)
# print(ejemplo2.head())

#-------------------------------------------------------------------------------------

# import csv

# ruta_csv = "./clases/clase-15/archivos/puntos_digitales.csv"  # Ajusta la ruta según corresponda

# with open(ruta_csv, mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


#-------------------------------------------------------------------------------------

# import csv

# ruta_csv = "./clases/clase-15/archivos/puntos_digitales.csv"  # Ajusta la ruta según corresponda

# with open(ruta_csv, mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

#-------------------------------------------------------------------------------------

# import csv

# ruta_csv = "./clases/clase-15/archivos/puntos_digitales.csv"  # Ajusta la ruta según corresponda

# data = []
# with open(ruta_csv, mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         data.append(row)

# # Imprimir las primeras filas
# for row in data[:5]:
#     print(row)


#-------------------------------------------------------------------------------------


# import csv

# ruta_csv = "./clases/clase-15/archivos/puntos_digitales.csv"  # Ajusta la ruta según corresponda

# data = []
# with open(ruta_csv, mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         data.append(row)

# # Imprimir las primeras filas
# for row in data[:5]:
#     print(row)

#-------------------------------------------------------------------------------------

