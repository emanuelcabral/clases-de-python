# Consigna
# Realizar una función llamada año_bisiesto:

# Recibirá un año por parámetro
# Imprimirá “El año año es bisiesto” si el año es bisiesto
# Imprimirá “El año año no es bisiesto” si el año no es bisiesto
# Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

# Información a tener en cuenta:

# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
#---------------------------------------#

#-----------------------------------------------------------------------------------#
#--------------------------PROGRAMA FINAL DE AÑO BISIESTO 1-------------------------#
#-----------------------------------------------------------------------------------#

# #INGRESAMOS EL DATO EN UNA VARIABLE SIN MENCIONAR EL TIPO DE DATO
# entrada = input("Ingresa el año para determinar si es bisiesto: ")
# #CONVIERTO A ENTERO
# año = int(entrada)
# #LANZO MENSAJE
# print("Gracias por ingresar el año correctamente")
# #SE CONSULTA SI EL AÑO DIVIDIDO 4 DA RESTO 0 Y SI EL AÑO DIVIDIDO 100 ES DISTINTO AL RESTO 0
# # Ó SI EL AÑO DIVIDIDO POR 400 ES IGUAL AL RESTO 0 LANZA EL MENSAJE QUE EL AÑO ES BISIESTO
# if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#     print("El año es bisiesto")
# #CASO CONTRARIO LANZA EL MENSAJE EL AÑO NO ES BISIESTO
# else:
#     print("El año no es bisiesto")



#-----------------------------------------------------------------------------------#
#--------------------------PROGRAMA FINAL DE AÑO BISIESTO 2-------------------------#
#-----------------------------------------------------------------------------------#

##SE AGREGA EL METODO ISDIGIT PARA CONSULTAR SI ES EL DATO DE ENTRADA SON TODOS CARACTERES NUMERICOS(0-9)
##RETORNA TRUE EN TAL CASO DE CUMPLIR CON ESTA CARACTERISTICA
##SI SE INGRESO TODOS NUMERO PERO HAY UN CARACTER DIFERENTE COMO LETRAS RETORNA FALSE

# entrada = input("Ingresa el año para determinar si es bisiesto: ")

# if entrada.isdigit(): #SE AGREGA EL METODO PARA SABER SI SON DIGITOS NUMERICOS
#     año = int(entrada)
#     print("Gracias por ingresar el año correctamente")

#     if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#         print("El año es bisiesto")
#     else:
#         print("El año no es bisiesto")
# else:
#     print("Has ingresado un dato erróneo") #CASO CONTRARIO LANZA EL MENSAJE DATO ERRÓNEO

#-----------------------------------------------------------------------------------#
#--------------------------PROGRAMA FINAL DE AÑO BISIESTO 3-------------------------#
#-----------------------------------------------------------------------------------#

##SE AGREGA EL CODIGO A UNA FUNCION

# def determinar_bisiesto(): #SE CREA LA FUNCION
#     entrada = input("Ingresa el año que te encuentras para determinar si es bisiesto: ")

#     if entrada.isdigit(): #Con el metodo isdigit le consultamos si el valor ingresado es un digito numerico
#         año = int(entrada)
#         print("Gracias por ingresar el año correctamente.")

#         if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#             print("El año es bisiesto.")
#         else:
#             print("El año no es bisiesto.")

#     else:
#         print("Has ingresado un dato erróneo.")


# # Uso de la función
# determinar_bisiesto()



#-----------------------------------------------------------------------------------#
#--------------------------PROGRAMA FINAL DE AÑO BISIESTO 4-------------------------#
#-----------------------------------------------------------------------------------#

##SE AGREGA UN BUCLE PARA QUE EN TAL CASO SI EL USUARIO INGRESA UN DATO ERRONEO LO VUELVA A INGRESAR


# def determinar_bisiesto():
#     while True:  # Se crea un bucle infinito para que el usuario pueda intentar nuevamente
#         entrada = input("Ingresa el año que te encuentras para determinar si es bisiesto: ")

#         if entrada.isdigit():  # Verifica si la entrada es un número
#             año = int(entrada)
#             print("Gracias por ingresar el año correctamente.")

#             if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#                 print("El año es bisiesto.")
#             else:
#                 print("El año no es bisiesto.")

#             break  # Rompe el bucle después de procesar la entrada válida

#         else:
#             print("Has ingresado un dato erróneo. Por favor, ingresa un año válido.")


# ## Uso de la función
# determinar_bisiesto()

#-----------------------------------------------------------------------------------#
#--------------------------PROGRAMA FINAL DE AÑO BISIESTO 5 FINAL-------------------#
#-----------------------------------------------------------------------------------#

##SE AGREGA UN BUCLE PARA QUE EL USUARIO VUELVA A CONSULTAR LOS AÑOS QUE QUIERA

# def determinar_bisiesto():
#     while True:  # Bucle principal para permitir múltiples consultas
#         while True:  # Bucle para solicitar un año válido
#             entrada = input("Ingresa el año que te encuentras para determinar si es bisiesto: ")

#             if entrada.isdigit():  # Verifica si la entrada es un número
#                 año = int(entrada)
#                 print("Gracias por ingresar el año correctamente.")

#                 if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#                     print("El año es bisiesto.")
#                 else:
#                     print("El año no es bisiesto.")
                    
#                 break  # Rompe el bucle después de procesar la entrada válida

#             else:
#                 print("Has ingresado un dato erróneo. Por favor, ingresa un año válido.")

#         consulta_nueva = input("¿Deseas consultar nuevamente? (si/no): ")
#         if consulta_nueva.lower() != "si":
#             print("Fin del programa.")
#             break  # Salir del bucle principal si el usuario no desea consultar nuevamente


# ## Uso de la función
# determinar_bisiesto()

#------------------------------------------------------------------------------------------------------#

# def determinar_bisiesto():
#     while True:  # Bucle general para permitir múltiples consultas
#         while True:  # Bucle para validar el año ingresado
#             entrada = input("Ingresa el año que te encuentras para determinar si es bisiesto: ")

#             if entrada.isdigit(): 
#                 año = int(entrada)
#                 print("Gracias por ingresar el año correctamente.")
#                 break  # Salir del bucle de validación del año si se ingresa correctamente
#             else:
#                 print("Has ingresado un dato erróneo. Por favor, ingresa un año válido.")

#         if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#             print("El año es bisiesto.")
#         else:
#             print("El año no es bisiesto.")

#         consulta_nueva = input("¿Deseas consultar nuevamente? (si/no): ")
#         if consulta_nueva.lower() != "si":
#             print("Fin del programa.")
#             break  # Salir del bucle general si el usuario no desea consultar nuevamente

# # Uso de la función
# determinar_bisiesto()