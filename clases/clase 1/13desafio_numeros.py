# En nuestro trabajo, nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo. 
# Para ello, debemos considerar tres aspectos: 

# Jugaron 20 partidos durante el torneo.
# Los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos.
# El promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos

#############################################################################################

# La cantidad de partidos que debemos considerar a un equipo para el ejemplo se detallan a continuación: 

# partidos_ganados 8
# partido_empatados 7
# partido_perdidos 5

# Importante: Cada una de las cantidades de partidos ganados, empatados o perdidos debe solicitarse al usuario utilizando la función input().

partidos_ganados = int(input("ingresa la cantidad de partidos ganados:"))
partidos_empatados = int(input("ingresa la cantidad de partidos empatados:"))
partidos_perdidos = int(input("ingresa la cantidad de partidos perdidos:"))


puntos = (partidos_ganados * 3) + (partidos_empatados)
print("tienes:" , puntos , "puntos")

puntaje_ideal = 20 * 3
# print(puntaje_ideal)
promedio = (puntos * 100) / puntaje_ideal
print("tu promedio es de: " ,promedio , "%")