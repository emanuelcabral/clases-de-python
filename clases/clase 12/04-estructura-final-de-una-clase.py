class Perro:
    #atributos de la clase
    especie = "Mamífero"
    #constructor de la clase
    def __init__(self, nombre,raza):

        #atributos de la instancia
        self.nombre = nombre
        self.raza = raza

# Creación de una instancia de Perro
perro1 = Perro("sammy", "Caniche")

print(f"Su nombre es: {perro1.nombre}") # Imprime el atributo nombre de la instancia perro1
print(f"Su raza es: {perro1.raza}") # Imprime el atributo raza de la instancia perro1
# Imprime el atributo de clase especie, que es común para todas las instancias de Perro
print(f"Es un: {perro1.especie}") 

# Su nombre es: sammy
# Su raza es: Caniche
# Es un: Mamífero 