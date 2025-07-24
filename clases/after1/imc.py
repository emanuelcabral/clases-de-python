# Solicitar al usuario que ingrese su peso en kg y su altura en metros
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC (Índice de Masa Corporal)
imc = peso / (altura ** 2)

# Mostrar el resultado del IMC
print("Su Índice de Masa Corporal es:", imc)


# Interpretación del IMC
if imc < 18.5:
    print("Usted está bajo peso.")
elif imc >= 18.5 and imc < 25:
    print("Usted tiene un peso normal.")
elif imc >= 25 and imc < 30:
    print("Usted tiene sobrepeso.")
else:
    print("Usted tiene obesidad.")