class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        pass

    def frenar(self):
        pass

    def girar(self):
        pass

    def describir(self):
        print("Soy el método describir")


# Crear una instancia de la clase
mi_vehiculo = Vehiculo("Toyota", "Corolla")

# Llamar al método que imprime el mensaje
mi_vehiculo.describir()  

# # Salida: Soy el método describir

#------------------------------------------------------------------


# class Empleado:
#     def __init__(self, nombre, puesto, salario):
#         self.nombre = nombre
#         self.puesto = puesto
#         self.salario = salario
    
#     def trabajar(self):
#         pass
    
#     def tomar_descanso(self):
#         pass
    
#     def recibir_sueldo(self):
#         pass
    
#     def info(self):
#         print("este es el print del metodo info")
