# Si necesitamos saber cuantas veces aparece una subcadena dentro de la misma cadena, usando el método count(). 

# Se escribe como: string.count()


cadena = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena.count(" "))
# 6
print("HoLa amigo como estas amigo!".count("amigo"))
# 2


cadena = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena.count(""))
# 38

cadena = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena.count("hOLa"))
# 1

cadena = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena.count("1"))
# 0

cadena = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena.count("HOLA"))
# 0