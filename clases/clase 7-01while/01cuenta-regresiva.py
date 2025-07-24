#cuenta regresiva

# Escribe un programa que pida al usuario un número entero positivo que sea ingresado por teclado y que realice una cuenta regresiva desde ese número hasta cero. Deberás utilizar el uso del bucle while.


numero = int(input("Introduce un número entero positivo: "))
while numero >= 0:
    print(numero)
    numero -= 1