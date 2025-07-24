#Para prevenir el error deberíamos comprobar que una lista tenga como mínimo un elemento antes de intentar sacarlo, algo factible utilizando la función len():


lista = []
if len(lista) > 0:
    lista.pop()

#el error es que no se realiza la indentacion correspondiente dentro del if
#como lista no tiene valores y se contabiliza con len la cantidad de elementos
#nos devuelve 0 y al usar la condicion es 0 > 0, por lo tanto la condicion es falsa
#y si hubiese estado bien tabulado no nos devuelve error ya que al ser falso no importa el codigo dentro del if