# Si necesitamos averiguar el índice en el que aparece una subcadena dentro de la misma cadena, 
#usamos el método find(). 

# Se escribe como: string.find(). 

# Si no encuentra la cadena devuelve un -1.


cadena = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena)
print(cadena.find("esta"))
# 11

# Si no encuentra la cadena devuelve un -1
print("HoLa amigo como estas amigo!".find("chau"))
# -1


print("HoLa amigo como estas amigo!".find("amigo"))
#aca en este ultimo muestra el indice del primer string amigo.
#5
