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

    #Método genérico con la misma implementación
    def describeme(self):  
        print("Soy un animal del tipo:" ,type(self).__name__)



#------------------------------------------------------------------


class Perro(Animal): 

    def __init__(self, especie, edad, dueño):#Constructor como siempre en la clase Padre

        #-atributos de la instancia-#
        
        #alternativa 1
        self.especie = especie
        self.edad = edad
        self.dueño = dueño

        #alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño

#------------------------------------------------------------------

mi_perro = Perro("mamifero", 7, "Luis")
mi_perro.especie
mi_perro.edad
mi_perro.dueño
