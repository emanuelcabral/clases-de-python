
#-----igualdad

#El operador de igualdad sirve para preguntarle a nuestro programa si ambos operandos son iguales.
#Devolverá True si son iguales, y False si son distintos. Este operador se escribe con dos signos igual (==).
print("---Igualdad---")

a = 3
print(a)
#3
print(a == 3)
# True

#No confundir el operador de asignación (=) con el operador de igualdad (==)

#------------------------------------------------------------------#

#-----desigualdad

#Este operador se escribe como un signo de exclamación y un signo igual (!=) como tachando al operador de igualdad.

#El operador de Desigualdad sirve para preguntarle a nuestro programa si ambos operandos son distintos.
#Devolverá True si son distintos, y False si son iguales. 

print("---Desigualdad---")

b = 3
print(b)
print(b != 3)
#False

#------------------------------------------------------------------#

#-----menor que

print("---Menor que---")

# El operador Menor que sirve para preguntarle a nuestro programa si el primer operando es menor que el segundo operando.

print(7 < 3)
# False
print(1 < 15)
#True

#Devolverá True si el primero es menor al segundo, y False si el primero es mayor que el segundo. Este operador se escribe con un signo de menor que (<).

#------------------------------------------------------------------#

#-----menor o igual que

print("---Menor o igual que---")

#El operador Menor igual que sirve para preguntarle a nuestro programa si el primer operando es menor que el segundo operando o si ambos son iguales.

print(7 <= 3)
#False
print(15 <= 15)
#True

#Devolverá True si el primero es menor o igual al segundo, y False si el primero es mayor que el segundo. 
#Este operador se escribe con un signo de menor que y un igual (<=).

#------------------------------------------------------------------#

#-----mayor que

print("---Mayor que---")

#El operador Mayor que sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando.

print(7 > 3)
#True
print(1 > 1)
#False

#Devolverá True si el primero es mayor al segundo, y False si el primero es menor que el segundo. Este operador se escribe con un signo de mayor que (>).


#------------------------------------------------------------------#
#-----mayor o igual que

print("---Mayor o igual que---")

#El operador Mayor igual que sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando, o si ambos son iguales.

print(7 >= 3)
#True
print(15 >= 15)
#True

#Devolverá True si el primero es mayor o igual al segundo, y False si el primero es menor que el segundo. 
#Este operador se escribe con un signo de mayor que y un igual (>=).


#------------------------------------------------------------------#

#¿Operadores en Strings?

print("---¿Operadores en Strings?---")

print('Hola' == "Hola")
#True
a = "Hola"
print(a[0] != 'H')
#False - es falso porque H no es distinta de H

#🧐 También podemos comparar en Listas, Booleanos y más tipos de datos.

# No sólo podemos hacer operaciones relacionales en números, también podemos hacerlas en strings.


#------------------------------------------------------------------#

#Tipo Lógico

print("---Tipo Lógico---")

#Los Booleanos tienen un valor aritmético por defecto. 
#True tiene un valor de 1 y mientras tanto False tiene un valor de 0. 
#Es decir, tienen un valor binario que se utiliza para poder operar entre sí.

print(True > False)
# True
print(True * 3)
# 3
print(False / 5)
# 0.0
