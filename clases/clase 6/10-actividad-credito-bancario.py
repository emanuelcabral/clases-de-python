# Aprobación de Crédito bancario

# Descripción de la actividad. 

# Para aprobar un crédito, el cliente debe ser mayor de edad. Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.  En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. Si no cumple ninguna de las condiciones, no se aprueba el crédito

# Datos iniciales
# edad = 15
# antigüedad = 10
# ingreso = 1500

edad = int(input("ingresa la edad: "))
antigüedad = int(input("ingrese la antigüedad: "))
ingreso = int(input("ingrese los ingresos mensuales: "))
#-------------------------------------------------------------
if edad >= 18:
    print("eres mayor de edad")
    if antigüedad >= 3:
        print("credito aprobado")
    else:
        if ingreso >= 4000:
            print("credito aprobado")
        else:
            print("credito no aprobado")
else:
    print("no eres mayor de edad y el credito no sera aprobado")

#---------------------------------------------------------------
# Otra forma mas simple
#---------------------------------------------------------------

# if edad >= 18 and ( antigüedad >= 3 or ingreso >= 4000 ):
#     print("credito aprobado")
# else:
#     print("credito no aprobado")