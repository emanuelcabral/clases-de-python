#Primero importamos a el modulo random
import random

#Aleatorios en un rango
print(random.randrange(20, 50)) # Genera un número aleatorio en el rango [20, 50)

#Aleatorios en un rango
print(random.randrange(20, 50,7)) 
# Genera un número aleatorio en el rango [20, 50) con un paso de 7


#---------------------------------------
#otro ejemplo
lista = [1, 2, "Coder", -1, "Nico", 3]

print(random.choice(lista)) # Elige un elemento aleatorio de la lista

#---------------------------------------

string = "Esta es una cadena de caracteres."

print(random.choice(string)) # Elige un carácter aleatorio de la cadena