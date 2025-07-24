# Esta función integrada sirve para devolver una lista con la cadena de caracteres separada por cada índice de la lista. 

# Se escribe como: string.split("cadena_a_separar"). 

# Si no se indica alguna cadena para separar separa por "espacios".



cadena = "hOLA mUNDO"
print(cadena)
print(cadena.split())
# ["hOLA", "mUNDO"]
#con el split solo separa las palabras con comas
print("HoLa amigo como estas amigo!".split("amigo"))
# ['HoLa ', ' como estas ', '!']
#con el split mas la busqueda de una palabra considera que en base a esa palabra se reemplaza por la coma

print("HoLa amigo como estas amigo!".split(""))
# ValueError: empty separator

print("HoLa amigo como estas amigo!".split(" "))
# 'HoLa', 'amigo', 'como', 'estas', 'amigo!'