#Si intentamos sacar un elemento de una lista vacía, algo que no tiene mucho sentido, el programa dará fallo de tipo IndexError. 
#Esta situación ocurre sólo durante la ejecución del programa, por lo que los editores no lo detectarán:

lista = []
lista.pop()

#   File "c:\Users\emanu\OneDrive\Desktop\py\clases\clase 10\03-errores-semanticos.py", line 5, in <module>
#     lista.pop()
# IndexError: pop from empty list

#el problema es que la lista esta vacia y se quiere eliminar un elemento, automaticamente nos lanza un error