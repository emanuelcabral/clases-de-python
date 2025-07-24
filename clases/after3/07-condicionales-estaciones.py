#Determinar la estación del año

# Escribe un programa en Python que solicite al usuario ingresar un mes (en formato de número del 1 al 12) y determine la estación del año correspondiente. Usa las siguientes reglas:

# Invierno: Diciembre (12), Enero (1), Febrero (2)
# Primavera: Marzo (3), Abril (4), Mayo (5)
# Verano: Junio (6), Julio (7), Agosto (8)
# Otoño: Septiembre (9), Octubre (10), Noviembre (11)

mes = int(input("Ingresa un mes (1-12): "))

if mes in [12, 1, 2]:
    print("Estación: Invierno")
elif mes in [3, 4, 5]:
    print("Estación: Primavera")
elif mes in [6, 7, 8]:
    print("Estación: Verano")
elif mes in [9, 10, 11]:
    print("Estación: Otoño")
else:
    print("Mes inválido")