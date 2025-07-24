#La función int() solo procesa correctamente cadenas que contengan exclusivamente números. 

#Si la cadena contiene cualquier otro carácter, la función devuelve una excepción ValueError.

int("2.5")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '2.5'

int("doscientos")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'doscientos'
