# Cálculo de índice de masa corporal (IMC)
#Escribe un programa en Python que solicite al usuario ingresar su peso en kilogramos y su altura en metros, y luego calcule e imprima su índice de masa corporal (IMC). La fórmula para calcular el IMC es: 
#imc = peso / (altura * altura)

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura * altura)
print("Tu índice de masa corporal (IMC) es: ", imc)

# Infrapeso: Delgadez Severa menos de 16 
# Infrapeso: Delgadez moderada entre 16 y 17
# Infrapeso: Delgadez aceptable entre 17 y 18.5
# peso normal= entre 18.5 y 25
# sobrepeso entre 25 y 30
# Obeso: Tipo I entre 30 y 35
# Obeso: Tipo II entre 35 y 40
# Obeso: Tipo III mas de 40















# print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")