class Animal: 

    def __init__(self, especie, edad):#Constructor como siempre en la clase Padre
        self.especie = especie
        self.edad = edad

    #Método generico pero con implementacion particular
    def hablar(self):  
        #print("este es el metodo hablar")
        #metodo vacio
        pass
    
    #Método generico pero con implementacion particular
    def moverse(self): 
        #print("este es el metodo moverse")
        #metodo vacio
        pass

    # def __str__(self):
    #     return f"ESPECIE: {self.especie} , EDAD: {self.edad}"

    #Método genérico con la misma implementación
    def describir(self):  
        print(f"Soy un animal del tipo: {type(self).__name__}")

# self: Se refiere a la instancia actual del objeto de la clase donde se llama al método.
# type(self): Devuelve el tipo del objeto, es decir, la clase a la que pertenece la instancia self.
# __name__: Es un atributo especial que contiene el nombre de la clase como una cadena de caracteres.




# class Perro(Animal):
#     pass

# class Gato(Animal):
#     pass


# # Creando instancias
# mi_perro = Perro("Perro", 5)
# mi_gato = Gato("Gato", 3)

# # Usando el método describir
# mi_perro.describir()  # Salida: Soy un animal del tipo: Perro
# mi_gato.describir()   # Salida: Soy un animal del tipo: Gato

# # Usando el método hablar
# print(mi_perro.hablar())  # Salida: ¡Guau!
# print(mi_gato.hablar())   # Salida: ¡Miau!