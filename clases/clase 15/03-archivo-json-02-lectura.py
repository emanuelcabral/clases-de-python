import json  # Importamos el módulo json para trabajar con JSON

ruta = "./clases/clase-15/archivos/"  # Definimos la ruta donde se encuentra el archivo JSON

# Abrimos el archivo JSON en modo lectura
with open(ruta + "primerJson.json") as file:
    dataLectura = json.load(file)  # Cargamos el contenido del archivo JSON en dataLectura como un diccionario

    # Iteramos sobre la lista de clientes en dataLectura['clients']
    for client in dataLectura['clients']:
        print('First name:', client['first_name'])  # Imprimimos el nombre del cliente
        print('Last name:', client['last_name'])    # Imprimimos el apellido del cliente
        print('Age:', client['age'])                # Imprimimos la edad del cliente
        print('Amount:', client['amount'])          # Imprimimos el monto del cliente
        print('')                                   # Imprimimos una línea en blanco entre cada cliente para mejor legibilidad

