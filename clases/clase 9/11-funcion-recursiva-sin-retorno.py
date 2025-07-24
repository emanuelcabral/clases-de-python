#Un ejemplo de una función recursiva con retorno, es el ejemplo del cálculo del factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número.


def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero) #Esta es una llamada recursiva. La función cuenta_regresiva se llama a sí misma con el nuevo valor de numero. Aquí es donde ocurre la recursión.
    else:
        print("Booom!")
    print("fin de la funcion ", numero )

cuenta_regresiva(5)

#4
#3
#2
#1
#Booom!
#fin de la funcion 0
#fin de la funcion 1
#fin de la funcion 2
#fin de la funcion 3
#fin de la funcion 4


#--------------- Flujo de ejecución -------------#
# Vamos a seguir el flujo de ejecución paso a paso:

# Primera llamada cuenta_regresiva(5):

# numero = 5
# numero -= 1 → numero = 4
# if 4 > 0 → True
# print(4) → imprime 4
# cuenta_regresiva(4)
# Segunda llamada cuenta_regresiva(4):

# numero = 4
# numero -= 1 → numero = 3
# if 3 > 0 → True
# print(3) → imprime 3
# cuenta_regresiva(3)
# Tercera llamada cuenta_regresiva(3):

# numero = 3
# numero -= 1 → numero = 2
# if 2 > 0 → True
# print(2) → imprime 2
# cuenta_regresiva(2)
# Cuarta llamada cuenta_regresiva(2):

# numero = 2
# numero -= 1 → numero = 1
# if 1 > 0 → True
# print(1) → imprime 1
# cuenta_regresiva(1)
# Quinta llamada cuenta_regresiva(1):

# numero = 1
# numero -= 1 → numero = 0
# if 0 > 0 → False
# print("Booom!") → imprime Booom!
# print("fin de la funcion ", 0) → imprime fin de la funcion 0
# Ahora se retrocede en la pila de llamadas recursivas:

# Retorno a la cuarta llamada cuenta_regresiva(2):

# print("fin de la funcion ", 1) → imprime fin de la funcion 1
# Retorno a la tercera llamada cuenta_regresiva(3):

# print("fin de la funcion ", 2) → imprime fin de la funcion 2
# Retorno a la segunda llamada cuenta_regresiva(4):

# print("fin de la funcion ", 3) → imprime fin de la funcion 3
# Retorno a la primera llamada cuenta_regresiva(5):

# print("fin de la funcion ", 4) → imprime fin de la funcion 4