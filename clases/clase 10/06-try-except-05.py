#ejemplo:

try:
    # Intentamos dividir un número por cero
    result = 10 / 0 #devuelve ZeroDivisionError
    # result = 10 / a #devuelve NameError
    # result = 10 / "a" #devuelve TypeError
    # result = 10 / int("esto no es un numero") #Devuelve ValueError
    # si agrego valor que no corresponde al tipo de dato me da un error del tipo ValueError
    # si agrego un string me da un error TypeError
except ValueError:
    # Este bloque except captura errores de tipo ValueError
    print("Ocurrió un error de tipo ValueError.")
except TypeError:
    # Este bloque except captura errores de tipo TypeError
    print("Ocurrió un error de tipo TypeError.")


#En este caso, se intenta dividir un número por cero, lo que genera un ZeroDivisionError. 
#Ninguno de los bloques except especificados coincide con este tipo de excepción.  
#Entonces, Python lanza el mensaje de error
