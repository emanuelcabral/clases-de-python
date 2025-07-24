class Persona:
    tipo = "Humano"
    __sueldo = 2000

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.__apellido = apellido

    def __soy_feliz(self):
        print("No les importa ")

    def edad(self):
        return 31 
    
persona1 = Persona("Nicolas", "Lopez")

print(f"Resultado1: {persona1.tipo}\n")
# print(f"Resultado2: {persona1.__sueldo}\n")
print(f"Resultado3: {persona1.nombre}\n")
# print(f"Resultado4: {persona1.__apellido}\n")
# print(f"Resultado5: {persona1.__soy_feliz()}\n")
print(f"Resultado6: {persona1.edad()}\n")