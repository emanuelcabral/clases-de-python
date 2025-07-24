# Esta función integrada sirve para ordenar una lista automáticamente por valor, de menor a mayor. 

# Se escribe como: lista.sort().

lista = [5,-10,35,0,-65,100]
lista.sort()
print(lista)
# [-65, -10, 0, 5, 35, 100]


# Si ponemos el argumento reverse=True la lista se ordenará de mayor a menor
lista.sort(reverse=True)
print(lista)
# [100, 35, 5, 0, -10, -65]
