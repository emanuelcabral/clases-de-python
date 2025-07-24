num1 = float(input("Ingresa tu primer número: "))
num2 = float(input("Ingresa tu segundo número: "))
operador = input("Ingresa el operador (+, -, *, /): ")

resultado = None

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operador no válido.")

if resultado is not None:
    print("El resultado es:", resultado)