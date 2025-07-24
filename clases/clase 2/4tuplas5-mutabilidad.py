# Como vimos, hay una diferencia entre listas y tuplas, las listas son mutables (podían reasignar sus ítems), en cambio, las tuplas son inmutables, esto significa que no podemos reasignar sus ítems. 

mi_tupla = (1, 2, 3, 4)
mi_tupla[2] = 5

#No es posible la mutabilidad con tuplas.

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
