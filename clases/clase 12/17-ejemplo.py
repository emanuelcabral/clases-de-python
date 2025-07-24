class Alumno:
    Nombre = "carlos"
    nota = 9

    def __init__(self, imprimir, resultado):

        # Atributos de la instancia
        self.imprimir = imprimir
        self.resultado = resultado

        # Métodos
    def imprimiendo(self):

        print("El alumno se llama ", Alumno.Nombre )

    def resultado_nota(self):
        
        print("El alumno tiene una nota de ", Alumno.resultado )