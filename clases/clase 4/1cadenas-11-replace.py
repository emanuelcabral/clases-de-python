# Esta función integrada sirve para devolver una cadena reemplazando los sub caracteres indicados. 

# Se escribe como: cadena.replace("caracter_a_remplazar", "caracter_que_reemplaza"). 

# También podemos indicar cuantas veces lo reemplazaremos utilizando un índice.


cadena = "Hola mundo"
print(cadena.replace("o", "0"))
# "H0la mund0"

print("Hola mundo mundo mundo mundo mundo".replace(' mundo','',4))
# "Hola mundo"

# print("Hola mundo mundo mundo mundo mundo".replace('busca la palabra','lo remplaza por nada',indica la cantidad de palabras))

#en este ultimo ejemplo busca la palabra mundo y lo reemplaza por nada,
#por el ultimo el 4 indica la cantidad de palabras "mundo" que reemplazara.


# Nota: En el último reemplazamos mundo 4 veces por un sólo carácter vacío
