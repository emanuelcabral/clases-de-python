class Customer:  # Define una clase llamada Customer
    def __init__(self):  # Define un método especial llamado __init__ para inicializar objetos de la clase Customer
        self.__accountNumber = 4321  # Inicializa un atributo privado llamado __accountNumber con el valor 4321

    def getAccountNumber(self):  # Define un método llamado getAccountNumber que devuelve el número de cuenta
        return self.__accountNumber  # Devuelve el valor del atributo privado __accountNumber

# Crear una instancia de la clase Customer
customer1 = Customer()  # Crea un objeto de la clase Customer llamado customer1

# Obtener y mostrar el número de cuenta
print("El número de cuenta del cliente es:", customer1.getAccountNumber())  # Imprime el número de cuenta del cliente utilizando el método getAccountNumber()


#Para acceder a un valor encapsulado, se utiliza un método que devuelve ese valor. Ese método puede llamarse con el prefijo get (por convención), o tener cualquier otro nombre