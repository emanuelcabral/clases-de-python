class Perro:
    # Atributo de clase compartido por todas las instancias
    especie = "Mamífero"

    # Método especial __init__ para inicializar instancias de la clase
    def __init__(self, nombre, raza):
        # Mensaje que se imprime al crear un perro
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia específicos para cada perro
        self.nombre = nombre
        self.raza = raza
    
    # Métodos de instancia
    def ladrar(self):
        # Método para que el perro ladre
        print("Este perro ha ladrado :( \nEstá enojado")

    def caminar(self, pasos):
        # Método para que el perro camine una cierta cantidad de pasos
        print(f"Este perro ha caminado {pasos} pasos")

    # Método especial __str__ para devolver una representación de cadena de la instancia
    def __str__(self):
        return f"nombre: {self.nombre} raza: {self.raza} especie: {self.especie}"


class Persona: 
    # Método especial __init__ para inicializar instancias de la clase
    def __init__(self, nombre, apellido, perro):
        # Atributos de instancia específicos para cada persona
        self.nombre = nombre
        self.apellido = apellido
        self.perro = perro

    # Método especial __str__ para devolver una representación de cadena de la instancia
    def __str__(self):
        return "Mi nombre es: " + self.nombre + " " + self.apellido + "\n" + self.perro.__str__()

# Crear una instancia de la clase Perro con nombre "Sammy" y raza "Caniche"
perro1 = Perro("Sammy", "Caniche")
# Crear una instancia de la clase Persona con nombre "Nico", apellido "Perez" y el perro "perro1"
persona1 = Persona("Nico", "Perez", perro1)

# Imprimir la representación en cadena de la instancia de Persona
print(persona1)


# Creando perro Sammy, Caniche
# Mi nombre es: Nico Perez
# nombre: Sammy raza: Caniche especie: Mamífero