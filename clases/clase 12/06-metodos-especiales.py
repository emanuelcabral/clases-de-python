class Perro:
    # Atributos de la clase
    especie = "Mamífero"

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        # Se imprime un mensaje indicando la creación del perro con su nombre y raza
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza
    
    # Métodos
    def ladrar(self):
        # Método que imprime un mensaje indicando que el perro ha ladrado y está enojado
        print("Este perro ha ladrado :( \nEstá enojado")

    def caminar(self, pasos):
        # Método que imprime un mensaje indicando cuántos pasos ha caminado el perro
        print(f"Este perro ha caminado {pasos} pasos")

# Se crea una instancia de la clase Perro con el nombre "Sammy" y la raza "Caniche"
perro1 = Perro("Sammy", "Caniche")

# Se imprime el nombre del perro utilizando el atributo de instancia "nombre"
print(f"Su nombre es: {perro1.nombre}")

# Se imprime la raza del perro utilizando el atributo de instancia "raza"
print(f"Su raza es: {perro1.raza}")

# Se imprime la especie del perro utilizando el atributo de clase "especie"
print(f"Es un: {perro1.especie}")

# Se llama al método "ladrar" de la instancia "perro1"
perro1.ladrar()

# Se llama al método "caminar" de la instancia "perro1" con el argumento "5" pasos
perro1.caminar(5)


# Creando perro Sammy, Caniche
# Su nombre es: Sammy
# Su raza es: Caniche
# Es un: Mamífero
# Este perro ha ladrado :(      
# Está enojado
# Este perro ha caminado 5 pasos


