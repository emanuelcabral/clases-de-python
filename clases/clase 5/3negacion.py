# Si negamos una cosa que es verdad, esta se convierte en mentira. Por lo tanto, si negamos una cosa que es mentira, esta se convierte en verdad.

# No Verdadero = Falso
# No Falso = Verdadero

# Definimos las variables booleanas
soleado = True
lluvioso = False

# Asignamos el valor de 'soleado' a la variable 'dia'
dia = soleado

# Verificamos si 'dia' no es igual a 'lluvioso' e imprimimos el resultado
print("¿No es un día lluvioso?", not dia == lluvioso)

# Imprimimos el valor de 'dia'
print("El valor de 'dia' es:", dia)

#not True == False = verdadero
#not False == False = Falso
#not False == True = verdadero
#not True == True = Falso