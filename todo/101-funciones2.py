# crear un programa que permita almacenar los costos mensuales de una persona

# def gastos():
#     sueldo = int(input("ingresa tus sueldo en pesos: "))
#     gastosfinales = int(0)
#     while str(input("ingrese fin para terminar: ")) != "fin":
#         gasto = int(input("ingresa tus gastos en pesos: "))
#         # sueldo = int(input("ingresa tus sueldo en pesos: "))
#         if gastosfinales < sueldo:
#             # print("tus gastos hasta el momento son: ", gastosfinales)
#             gastosfinales= gastosfinales + gasto
#             print("tus gastos hasta el momento son: ", gastosfinales)
#             print("tus saldo actual es: ", sueldo - gastosfinales)
#         else:
#             print("no tienes más plata!!!")

# gastos()
    


#calcular la cantidad de alumnos que aprobaron con mas de 7

# def aprobados():
#     a= int(0)
#     while str(input("ingrese fin para terminar: ")) != "fin":
#         nota = int(input("ingresa tu nota: "))
#         if nota >= 7:
#             print("has aprobado")
#             a=a+1
#             print("cantidad de aprobados: ", a)
#         else:
#             print("has desaprobado")

# aprobados()


##############################################
### averiguar el promedio de varias notas
##############################################

# def calpromedio():
#     suma= int(0)
#     cont= int(0)

#     while str(input("ingrese fin para terminar: ")) != "fin":

#         print("ingrese las notas para determinar el promedio")
#         num= int(input("ingrese la nota: "))
#         suma= suma+num
#         cont=cont+1
#         promedio= suma/cont
#     print("tu promedio es de: ", promedio)

# calpromedio()