class Perro:
    #atributos de la clase
    especie = "Mamífero"
    #constructor de la clase
    def __init__(self, nombre,raza):

        #atributos de la instancia
        self.nombre = nombre
        self.raza = raza

print(Perro.especie) # Accediendo al atributo de clase