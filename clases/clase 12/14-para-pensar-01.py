class Persona:  # Define una clase llamada Persona.

    tipo = "Humano"  # Atributo de clase que almacena el tipo "Humano".
    __sueldo = 2000  # Atributo de clase privado que almacena el sueldo (no accesible directamente fuera de la clase).

    def __init__(self, nombre, apellido):  # Método especial de inicialización de objetos con argumentos nombre y apellido.
        self.nombre = nombre  # Atributo de instancia que almacena el nombre.
        self.__apellido = apellido  # Atributo de instancia privado que almacena el apellido.

    def __soy_feliz(self):  # Método privado que imprime "No les importa".
        print("No les importa ")

    def edad(self):  # Método público que retorna la edad 31.
        return 31 
    
persona1 = Persona("Nicolas", "Lopez")  # Creación de una instancia de la clase Persona con nombre "Nicolas" y apellido "Lopez".

print(f"Resultado1: {persona1.tipo}\n")  # Imprime el tipo de la persona (Humano).
print(f"Resultado2: {persona1.__sueldo}\n")  # Intento de acceder a un atributo privado fuera de la clase.
print(f"Resultado3: {persona1.nombre}\n")  # Imprime el nombre de la persona (Nicolas).
print(f"Resultado4: {persona1.__apellido}\n")  # Intento de acceder a un atributo privado fuera de la clase.
print(f"Resultado5: {persona1.__soy_feliz()}\n")  # Intento de llamar a un método privado fuera de la clase.
print(f"Resultado6: {persona1.edad()}\n")  # Imprime la edad de la persona (31).