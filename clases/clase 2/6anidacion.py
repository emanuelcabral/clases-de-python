# En Python, una tupla y una lista pueden ser anidadas: esto significa que pueden contener una lista o una tupla dentro de sí respectivamente.


tupla_datos = [155, [2, 3, 4], "Una cadena", "Otra cadena"]
lista_otros_datos = (2, (5, 7, 8), 1, 8)
lista_con_tupla = [1, (2, 3, 4), "Una cadena", "Otra cadena"]
tupla_con_lista = (2, [5, 7, 8], 1, 8)


#######################################################################################


# A continuación mostraremos un ejemplo de cómo acceder a los datos anidados:

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
resultado = [a, b, c]
print(resultado)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(resultado[0])
# [1, 2, 3]
print(resultado[0][1])
# ↑↑ de esta forma busca en la primera lista y luego accede al 2.
# print(resultado[0[1]]) ← asi daria error
# 2

print(resultado[0][2])
print(resultado[1][2])
