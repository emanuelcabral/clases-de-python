#De la misma forma podemos obtener un conjunto a partir de cualquier objeto iterable:

#para este ejemplo esta utilizando una lista temporal para inicializar el set,
#la forma mas comun de declarar un set es con el uso de las {}.
#Es otra alternativa para crear un set
set1 = set([1, 2, 3, 4])
print(set1)

##En este ejemplo me trae error porque estoy utilizando la lista.
# set1 = set([1, 2, 3, 4],10)
# print(set1)

set2 = set(range(10))
print(set2)

#range permite ingresar una serie de valores numericos consecutivos hasta el valor indicado (no inclusivo)

#Diferencia entre Conjuntos, listas y tuplas.
#Los conjuntos son utiles para trabajar con elementos unicos que no sean duplicados.
#Las Listas para trabajar con elementos por indice y elementos duplicados.
#Las tuplas para elementos no mutables, por tal motivo ofrece seguridad y eficiencia.


