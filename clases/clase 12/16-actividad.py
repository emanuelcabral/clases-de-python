class Alumno:  # Define una clase llamada Alumno.

    def __init__(self, nombre, nota):  # Método especial de inicialización de objetos con argumentos nombre y nota.
        self.nombre = nombre  # Atributo de instancia que almacena el nombre.
        self.nota = nota  # Atributo de instancia que almacena la nota.

    # Función para imprimir los datos del alumno.
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    # Función para obtener el resultado del alumno (aprobado o suspendido).
    def resultado(self):
        if self.nota < 5:  # Si la nota es menor a 5...
            print("El alumno ha suspendido")  # Imprime "El alumno ha suspendido".
        else:  # Si la nota es igual o mayor a 5...
            print("El alumno ha aprobado")  # Imprime "El alumno ha aprobado".

# Bloque principal

alumno1 = Alumno("ivan", 8)  # Creación de una instancia de la clase Alumno con nombre "ivan" y nota 8.
alumno2 = Alumno("juan", 4)  # Creación de una instancia de la clase Alumno con nombre "juan" y nota 4.

# Imprimimos los datos y resultados de cada alumno
alumno1.imprimir()  # Llama al método imprimir de alumno1 para mostrar sus datos.
alumno1.resultado()  # Llama al método resultado de alumno1 para mostrar su resultado (aprobado o suspendido).
alumno2.imprimir()  # Llama al método imprimir de alumno2 para mostrar sus datos.
alumno2.resultado()  # Llama al método resultado de alumno2 para mostrar su resultado (aprobado o suspendido).


# Nombre:  ivan
# Nota:  8
# El alumno ha aprobado
# Nombre:  juan
# Nota:  4
# El alumno ha suspendido