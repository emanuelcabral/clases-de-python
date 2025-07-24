# Importa la clase namedtuple del módulo collections
from collections import namedtuple

# Crea una namedtuple llamada "Fish" con tres campos: "name", "species" y "tank"
Fish = namedtuple("Fish", ["name", "species", "tank"])

#Esto crea una clase Fish con los atributos publicos nombre, especie y tanque

#Por el momento no nos devuelve nada

print(Fish)