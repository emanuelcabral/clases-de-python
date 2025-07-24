class Perro:
    #atributos de la clase
    especie = "Mamífero"

    #El metodo __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        #atributos de la instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"caminando {pasos} pasos")

# Creando una instancia de la clase Perro, con nombre "Toby" y raza "bulldog"
mi_perro = Perro("Toby", "bulldog")

# Llamando al método ladra() de la instancia mi_perro
mi_perro.ladra()

# Llamando al método camina() de la instancia mi_perro, con 10 pasos como argumento
mi_perro.camina(10)

# Creando perro Toby, bulldog
# Guau
# caminando 10 pasos