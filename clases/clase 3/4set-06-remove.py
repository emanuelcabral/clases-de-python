# La función remove funciona igual al discard, pero con una diferencia,
# en discard si el ítem a remover no existe, simplemente se ignora. 
# En remove en este caso nos indica un error.


numeros =  {1, 2, 3, 4}
print(numeros)
numeros.remove(2)
print(numeros)
# {1, 3, 4}

numeros.remove(5)

#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#KeyError: 5

