#Determinar la estación del año

# Escribe un programa en Python que solicite al usuario ingresar un mes (en formato de número del 1 al 12) y determine la estación del año correspondiente. Usa las siguientes reglas:

# Determinar la estación del año en el hemisferio sur

# Verano: Diciembre (12), Enero (1), Febrero (2)
# Otoño: Marzo (3), Abril (4), Mayo (5)
# Invierno: Junio (6), Julio (7), Agosto (8)
# Primavera: Septiembre (9), Octubre (10), Noviembre (11)

mes = int(input("Ingresa un mes (1-12): "))

if mes in [12, 1, 2]:
    print("Estación: Verano")
elif mes in [3, 4, 5]:
    print("Estación: Otoño")
elif mes in [6, 7, 8]:
    print("Estación: Invierno")
elif mes in [9, 10, 11]:
    print("Estación: Primavera")
else:
    print("Mes inválido")



# otra version mas especifica seria:

# mes = int(input("Ingresa un mes (1-12): "))
# dia = int(input("Ingresa un día (1-31): "))

# if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or (mes == 3 and dia < 21):
#     print("Estación: Verano")
# elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or (mes == 6 and dia < 21):
#     print("Estación: Otoño")
# elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or (mes == 9 and dia < 21):
#     print("Estación: Invierno")
# elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or (mes == 12 and dia < 21):
#     print("Estación: Primavera")
# else:
#     print("Fecha inválida")