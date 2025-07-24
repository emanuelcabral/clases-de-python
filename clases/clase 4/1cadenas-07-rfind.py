# Es exactamente igual al método find() los diferencia en que rfind() devuelve el índice, 
# pero de la última ocurrencia de la subcadena, es decir, la última vez que aparece en la cadena. 

# Se escribe como: string.rfind(). 

# Si no encuentra la cadena devuelve un -1.

print("HoLa amigo como estas amigo!".find("amigo"))
# 5 - muestra el primer indice de donde comienza con find
print("HoLa amigo como estas amigo!".rfind("amigo"))
# 22 - muestra el indice de donde comienza el ultimo string buscado
print("HoLa amigo como estas amigo! hola amigo".rfind("amigo"))
# 34

#rfind significa reverse find - busqueda inversa