#Verificar letra vocal o consonante

#Escribe un programa en Python que solicite al usuario ingresar una letra y determine si es una vocal o una consonante.

letra = input("Ingresa una letra: ").lower()

if letra in 'aeiou':
    print("La letra es una vocal")
else:
    print("La letra es una consonante")