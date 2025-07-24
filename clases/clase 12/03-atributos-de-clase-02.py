class Perro:
    #atributos de la clase
    especie = "Mamífero"
    #constructor de la clase
    def __init__(self, nombre,raza):

        #atributos de la instancia
        self.nombre = nombre
        self.raza = raza

# Creación de una instancia de Perro
mi_perro = Perro("Toby","Bulldog")

print(Perro.especie) # Accediendo al atributo de clase
print(mi_perro.especie) # Accediendo al atributo de clase desde una instancia

# Mamífero
# Mamífero