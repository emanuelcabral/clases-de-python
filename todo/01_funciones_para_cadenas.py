# Info completa: https://docs.python.org/es/3/library/stdtypes.html#string-methods

from itertools import count


cadena = "Soy una CaDENa de texto Para pruebas"

# Len(cadena)
print(count(cadena))
# count(subcadena)
# Retorna el numero de veces que se repite una subcadena dentro de la cadena de texto


# capitalize()
# Retorna una copia de la cadena con el primer carácter en mayúsculas y el resto en minúsculas.

# title()
# Retorna la primera letra de cada palabra en mayúsculas y el resto en minúsculas.

# lower()
# Retorna una copia de la cadena de caracteres con todas las letras en minúsculas

# upper()
# Retorna una copia de la cadena de caracteres con todas las letras en mayúsculas

# isalpha()
# Retorna True si todos los caracteres de la cadena son alfabéticos y hay, al menos, un carácter. En caso contrario, retorna False.

# isdigit()
#Retorna True si todos los caracteres de la cadena son dígitos y hay, al menos, un carácter. En caso contrario, retorna False

# endswith(subcadena)
# Retorna True si la cadena finaliza con la subcadena pasada como parametro

# startswith(subcadena)
# Retorna True si la cadena inicia con la subcadena pasada como parametro

# Extraer parte de una cadena
# cadena[2:5]


# print(dir(cadena))