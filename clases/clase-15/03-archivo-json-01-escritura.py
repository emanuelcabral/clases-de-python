import json  # Importamos el módulo json para trabajar con JSON

data = {}  # Creamos un diccionario vacío llamado 'data'

data['clients'] = []  # Creamos una lista vacía dentro de 'data' con la clave 'clients'

# Agregamos información de clientes a la lista 'clients' dentro de 'data'
data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17
})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]  # La cantidad es una lista de números
})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11
})

ruta = "./clases/clase-15/archivos/"  # Definimos la ruta donde se almacenará el archivo JSON

# Abrimos el archivo 'primerJson.json' en modo escritura y 
# usamos 'json.dump()' para escribir 'data' en el archivo

with open(ruta + "primerJson.json", 'w') as file:
    json.dump(data, file, indent=4)  # 'indent=4' para una salida JSON con formato indentado de 4 espacios


#La función .dump() es un método de la biblioteca json en Python que convierte un objeto Python (como un diccionario o lista) en una cadena JSON y la escribe directamente en un archivo.