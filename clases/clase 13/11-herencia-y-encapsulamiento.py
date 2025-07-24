class Animal:

  def __init__(self, especie, edad):#Constructor como siempre en la clase Padre
    self.especie = especie
    self.edad = edad

  def __hablar(self):  #metodo privado
    print("este es el metodo hablar")

  def moverse(self):
    print("este es el metodo moverse")

class Perro(Animal): #creamos una clase perro perteneciente a la clase animal
  pass

perro1 = Perro("Mamífero", 11) #instanciamos un objeto

perro1.moverse()

perro1.__hablar() #no se puede acceder dado que no fue un metodo heredado por la clase hija

#Que pasas si eliminamos el __ del metodo y del llamado?