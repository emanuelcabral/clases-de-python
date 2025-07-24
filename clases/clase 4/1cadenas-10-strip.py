# Esta función integrada sirve para devolver una cadena borrando todos los caracteres ,de delante y detrás solamente, de la cadena especificados en la cadena de caracteres a borrar que se le pasan entre parentesis a strip. Se escribe como: 
# Se escribe como: cadena.strip("caracteres_a_borrar"). 

# Nota: Si no se especifica el carácter elimina los espacios


cadena = "---------Hola mundo--------"
print(cadena)
print(cadena.strip("-"))
# "Hola mundo"

print("                Hola mundo              ".strip())
# "Hola mundo"

print("ssaddaHolas mundoddsaa".strip("asd"))
# "Hola mundo"
print("ssaddaHolas asd mundoddsaa".strip("asd")) # aca lo incluye porque es solo al comienzo y al fin
#Holas asd mundo

# Lo que hace es buscar todos los caracteres "a", "s" y "d" del comienzo y fin del string
# No importa el orden, no necesariamente debe respetarlo
# En tal caso que se repitieran los caracteres tambien son eliminados

#El método strip() en Python puede traducirse como "recortar" o "eliminar" los caracteres innecesarios