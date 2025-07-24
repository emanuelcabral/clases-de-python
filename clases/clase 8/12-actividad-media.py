#Escribir una función que reciba una muestra de números en una lista y devuelva su media

def promedio(muestra):
    return sum(muestra)/len(muestra)

print(promedio([1, 2, 3, 4, 5]))
print(promedio([2.3, 3.7, 7.8, 9.7, 15.1, 20.6]))


## otra alternativa

# def promedio(lista):
#     valor = 0
#     for item in lista:
#         valor += item
#     promedio = valor/len(lista)
#     return promedio
# print(promedio([1,2,3,4,5]))