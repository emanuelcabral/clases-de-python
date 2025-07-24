#calcular promedio de equipos de futbol
#tener en cuenta que jugaron 20 partidos
#3puntos ganados - empate 1 punto - perdidos 0
#para sacar el promedio de puntos se debe sumar todos los puntos dividos por la cantidad de partidos
#pg 8 - pe 7 - pp5

#datos de mi equipo

pg = int(input("ingresa la cantidad de partidos ganados: "))
pe = int(input("ingresa la cantidad de partidos empatados: "))
pp = int(input("ingresa la cantidad de partidos perdidos: "))


puntos = pg*3 + pe*1 + pp*0
print("la cantidad de puntos de tu equipo es: " , puntos)
promedio = puntos / 20
print("el promedio de tu equipo es: " , promedio)