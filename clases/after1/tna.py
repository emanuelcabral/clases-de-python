# Calcular ganancias
tna = float(input("Ingresa el TNA: "))
anio = int(input("Ingresa la cantidad de días del año: "))
saldo = float(input("Ingresa tu saldo: "))

# Calcular ganancia diaria
resultado = (tna / 100 / anio) * saldo
print("Tu ganancia diaria es de: $", resultado)

#Calcular ganancia por cierta cantidad de dias
dias = int(input("ingresa la cantidad de dias a multiplicar: "))
print("Tu ganancia en ", dias , "es de: $", (resultado*dias))