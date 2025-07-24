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