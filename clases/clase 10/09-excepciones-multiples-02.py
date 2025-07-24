#Cada error tiene un identificador único que curiosamente se corresponde con su tipo de dato. 
#Aprovechando eso podemos mostrar la clase del error utilizando la sintaxis:


try:
    n = input("Introduce un número: ")  # no transformamos a número
    result = 5 / n  # sino lo convertimos a entero nos lanza el error
    # result = 5 / int(n)  # convertimos a número para evitar errores de tipo
except Exception as e:  # guardamos la excepción como una variable e
    print( type(e) ) #Nos muestra el error
