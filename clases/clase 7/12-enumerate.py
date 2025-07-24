#La función incorporada enumerate(lista/tupla_de_valores) toma como argumento un objeto iterable y retorna otro cuyos elementos son tuplas de dos objetos:

#ejemplo simple:

# Lista de colores
colores = ['rojo', 'verde', 'azul', 'amarillo']

# Usando enumerate para obtener el índice y el valor
for indice, color in enumerate(colores):
    print(f"El color en la posición {indice} es {color}")

#for var_indice var_valor_lista in enumerate(colores):
#al utilizar enumerate se usan dos variables una para el indice y otra para interactuar por ejemplo con una lista

#Ejemplo de las slides:

# numeros = [0,1,2,3,4,5,6,7,8,9,10]
# print("Lista original:", numeros)
# for indice, numero in enumerate(numeros): 
#     numeros[indice] *= 5
# print("Lista después de multiplicar cada elemento por 5:", numeros)



#Por defecto, enumerate() comienza con el índice 0. Puedes especificar un índice de inicio diferente usando el parámetro start.

# lista = ['a', 'b', 'c']
# for indice, valor in enumerate(lista, start=1):
#     print(f'Índice: {indice}, Valor: {valor}')

#enumerate() puede ser utilizado con cualquier objeto iterable, como listas, tuplas, cadenas, conjuntos, diccionarios (iterando sobre las claves), generadores, etc.