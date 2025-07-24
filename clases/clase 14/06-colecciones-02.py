from collections import namedtuple

# Definición de la namedtuple llamada "Fish" con los campos "name", "species", y "tank"
Fish = namedtuple("Fish", ["name", "species", "tank"])
#Esto crea una clase Fish con los atributos publicos nombre, especie y tanque

# Creación de una instancia de la namedtuple Fish llamada miPrimerPez
miPrimerPez = Fish("Sammy", "Tiburón", "Tanque grande")

# Impresión de la instancia miPrimerPez, que muestra los valores asignados a cada campo
print(miPrimerPez)


#otra cosa útil es transformar una instancia de una clase en un
#diccionario

# Uso de _asdict() para convertir la namedtuple en un diccionario
print(miPrimerPez._asdict())


# Fish(name='Sammy', species='Tibrón', tank='Tanque grande')
# OrderedDict([('name', 'Sammy'), ('species', 'Tiburón'), ('tank', 'Tanque grande')])