#un conjunto no puede incluir objetos mutables como listas, diccionarios, e incluso otros conjuntos o set.

# s = {{1,2}, [1,2,3,4],2}
# s = {[1,2,3,4],2}
# s = {[1,2,3,4]}
# print(s)

#Mensaje de error ↓↓↓
#----------------------------------#
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'set'
