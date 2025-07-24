# Otra cosa en la que se parecen las tuplas a las listas, es que en ambos casos se puede concatenar.
# Importante:  Las tuplas no contienen la función append() 👀, pero puedes agregar elementos con la técnica de concatenación:

numeros = (1, 2, 3, 4)
numeros += (5, 6, 7, 8)
print(numeros)
# (1, 2, 3, 4, 5, 6, 7, 8)
años = (2020, 2021, 2022)
años += (2023,)
print(años)
# (2020, 2021, 2022, 2023)
