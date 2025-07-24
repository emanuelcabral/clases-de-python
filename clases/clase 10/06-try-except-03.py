#ejemplo:

try:
    # Intentamos dividir por cero
    result = 10 / 0  #que pasa si cambiamos el 0 por una s
except ZeroDivisionError:
    # Este bloque except captura ZeroDivisionError
    print("No se puede dividir por cero.")
except:
    # Este bloque except captura cualquier otro tipo de error
    print("Ocurrió un error.")


#Si el error que arroja no es ZeroDivisionError. 
#Busca otro excepte otro except donde en este caso captura cualquier tipo de error.
