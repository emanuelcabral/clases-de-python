class Persona:
    """
    Esta es una clase donde se agregan todos los datos
    respecto a una persona
    """
    def __init__(self, nombre, edad):
        # Todo lo que definamos en __init__ se corre
        # al crear una instancia de la clase
        self.nombre = nombre
        self.edad = edad

#El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.

#Link de Interes: https://ejemplos.net/que-significa-self-en-python/

#Creamos un objeto p1 que es una instancia de la clase Persona
p1 = Persona("Juan", 26)

print(p1.nombre) #Le pedimos a p1 su nombre
print(p1.edad) #Le pedimos a p1 su edad

#Vemos el tipo de objeto que es p1
# type(p1)
print(type(p1))

#Devuelve
# Juan
# 26
# <class '__main__.Persona'>

# __main__ indica que la clase Persona está definida en el script que se está ejecutando directamente.
# Por ejemplo, si tu script estuviera en un archivo llamado mi_script.py y lo importaras desde otro archivo, el tipo de p1 aparecería como <class 'mi_script.Persona'>.