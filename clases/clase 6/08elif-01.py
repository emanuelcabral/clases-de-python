#Como podemos observar, la primera condición valida si A es igual a 4, como esto no es verdadero, 
#se evalúa la siguiente condición, si A es igual a 5, si no A es igual a 6? .
#Finalmente, se define un bloque else por default que se ejecutará cuando ninguna de las condiciones anteriores sea verdadera.

#Pregunta! ¿Cuál sería el resultado de este ejemplo?


a = 2 + 3
if a == 4: 
    print ("A es igual a cuatro")
elif a == 5:
    print ("A es igual a cinco")
elif a == 6:
    print ("A es igual a seis")
else:
    print ("No se cumple la condición")
