class Persona:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def info(self):
        print("Este es el print del método info de Persona")

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    
    def trabajar(self):
        pass
    
    def tomar_descanso(self):
        pass
    
    def recibir_sueldo(self):
        pass
    
    def info(self):
        print("este es el print del metodo info")

# Crear una instancia de la clase
mi_empleado1 = Empleado("Carlos", "Programador", 1500)

# Llamar al método que imprime el mensaje
mi_empleado1.info()  

#este es el print del metodo info

# persona1 = Persona("carlos", "programador")
# persona1.info()