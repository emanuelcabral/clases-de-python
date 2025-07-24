# #De esta forma es posible analizar el tipo de error que sucede gracias a su identificador:



try:
    n = input("Introduce un número: ")  # no transformamos a número
    result = 5 / n  # sino lo convertimos a entero nos lanza el error
    # result = 5 / int(n)  # convertimos a número para evitar errores de tipo
except Exception as e:  # guardamos la excepción como una variable e
    print("Ha ocurrido un error =>", type(e).__name__)


# __name__ en Python es un atributo especial que devuelve el nombre de la clase de un objeto. 
#En el contexto del ejemplo dado, type(e).__name__ se usa para imprimir el nombre de la clase de una excepción, lo que ayuda a identificar el tipo de error que ha ocurrido durante la ejecución del código.


# try:
#     n = input("Introduce un número: ")  # no transformamos a número
#     result = 5 / n  # sino lo convertimos a entero nos lanza el error
#     # result = 5 / int(n)  # convertimos a número para evitar errores de tipo
# except Exception as e:  # guardamos la excepción como una variable e
#     print("Ha ocurrido un error =>", type(e))