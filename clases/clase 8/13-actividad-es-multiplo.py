#Crea un programa que le pida dos números enteros al usuario y diga por consola, 
#si alguno de ellos es múltiplo del otro. La función debe llamarse es_multiplo().

def es_multiplo(num1, num2):
    # Verifica si num1 es múltiplo de num2 o num2 es múltiplo de num1
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

# Solicita el primer número al usuario y lo convierte a entero
numero1 = int(input("Número 1:"))

# Solicita el segundo número al usuario y lo convierte a entero
numero2 = int(input("Número 2:"))

# Verifica si alguno de los números es múltiplo del otro
if es_multiplo(numero1, numero2):
    # Imprime si alguno de los números es múltiplo del otro
    print(numero1, "es múltiplo de", numero2, "o viceversa")
else:
    # Imprime si ninguno de los números es múltiplo del otro
    print(numero1, "no es múltiplo de", numero2, "ni viceversa")

























# def es_multiplo(num1,num2):
#     # Verifica si num1 es múltiplo de num2
#     if num1 % num2 == 0:
#         return True
#     else:
#         return False

# # Solicita el primer número al usuario y lo convierte a entero
# numero1 = int(input("Número 1:"))

# # Solicita el segundo número al usuario y lo convierte a entero
# numero2 = int(input("Número 2:"))

# # Verifica si numero1 es múltiplo de numero2
# if es_multiplo(numero1,numero2):
#     # Imprime si numero1 es múltiplo de numero2
#     print(numero1,"es múltiplo de",numero2)
# else:
#     # Imprime si numero1 no es múltiplo de numero2
#     print(numero1,"no es múltiplo de",numero2)
