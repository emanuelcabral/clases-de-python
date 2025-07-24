class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass

print(Clase3.__mro__)
#(<class '__main__.Clase3'>, <class '__main__.Clase1'>, <class '__main__.Clase2'>, <class 'object'>)


#El atributo __mro__ significa "Method Resolution Order" (Orden de Resolución de Métodos)

# Este atributo es una tupla que muestra el orden en el que las clases se buscan cuando se llama a un método o se accede a un atributo en una instancia de una clase. Este orden es crucial en el caso de la herencia múltiple, donde una clase hereda de más de una clase base.