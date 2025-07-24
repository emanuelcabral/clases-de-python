# Solicitar al usuario que ingrese la tasa de cambio de pesos a dólares
tasa_cambio_pesos_a_dolares = float(input("Ingrese la tasa de cambio de pesos a dólares: "))

# Solicitar al usuario que ingrese la cantidad de dinero en pesos
cantidad_pesos = float(input("Ingrese la cantidad de dinero en pesos: "))

# Calcular la cantidad equivalente en dólares
cantidad_dolares = cantidad_pesos * tasa_cambio_pesos_a_dolares

# Mostrar la cantidad equivalente en dólares
print("La cantidad equivalente en dólares es:", cantidad_dolares)