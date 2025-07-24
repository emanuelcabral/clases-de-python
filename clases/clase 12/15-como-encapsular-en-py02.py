# Definición de la clase Customer
class Customer:
    # Constructor de la clase que inicializa el número de cuenta del cliente
    def __init__(self):
        self.__accountNumber = 4321

    # Método privado para procesar la cuenta del cliente (no utilizado en este ejemplo)
    def __processAccount(self):
        print("Processing Account")

    # Método público para obtener el número de cuenta del cliente
    def getAccountNumber(self):
        return self.__accountNumber

# Creación de una instancia de la clase Customer
customer1 = Customer()

# Impresión del número de cuenta del cliente utilizando el método getAccountNumber()
print("Customer Account Number:", customer1.getAccountNumber())  # Esto imprimirá "Customer Account Number: 4321"