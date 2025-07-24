class Persona:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def info(self):
        print("Este es el print del método info de Persona")

class Empleado(Persona):
    def __init__(self, nombre, puesto, salario):
        super().__init__(nombre, puesto)
        self.salario = salario
    
    def trabajar(self):
        print("Este es el print del método trabajar")
    
    def tomar_descanso(self):
        print("Este es el print del método tomar_descanso")
    
    def recibir_sueldo(self):
        print("Este es el print del método recibir_sueldo")
    
    def info(self):
        # super().info() #aqui llamamos a este metodo
        print("Este es el print del método info de Empleado")

# Crear una instancia de la clase
mi_empleado1 = Empleado("Carlos", "Programador", 1500)

# Llamar al método que imprime el mensaje
mi_empleado1.info()