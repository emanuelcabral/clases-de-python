#ejemplo:

try:
    # Intentamos dividir por cero
    result = 10 / 0  #que pasa si cambiamos el 0 por una s
except:
    # Este bloque except captura cualquier otro tipo de error
    print("Ocurrió un error.")
except ZeroDivisionError:
    # Este bloque except captura ZeroDivisionError
    print("No se puede dividir por cero.")


#La instrucción except: por defecto debe estar al final.
