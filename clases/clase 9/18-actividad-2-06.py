#------------------------------------------------------------------------------------#

# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()


#------------------------------------------------------------------#


# Función separar()

def separar(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    pares.sort()
    impares.sort()
    return pares, impares

# Comprobación de la función separar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar(lista)
print(f"Pares: {pares}")
print(f"Impares: {impares}")

#------------------------------------------------------------------#