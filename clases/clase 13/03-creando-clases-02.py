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
    def describeme(self):  
        print(f"Soy un animal del tipo: {type(self).__name__}")

#----------------------------------------------------------------
#----------------------------------------------------------------


class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    #nuevo metodo
    def picar(self):
        print("Picar!")

#----------------------------------------------------------------
# Crear instancias de las clases
mi_perro = Perro("mamifero", 10)
mi_vaca = Vaca("mamifero", 23)
mi_abeja = Abeja("insecto", 1)

mi_perro.hablar()
mi_vaca.hablar()
#Guau!
#Muuu!

mi_vaca.describeme()
mi_abeja.describeme()
# Soy un animal del tipo: Vaca
# Soy un animal del tipo: Abeja

mi_abeja.picar()
#Picar!