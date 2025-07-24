from collections import Counter # Importamos la clase Counter del módulo collections

l = [1,2,3,4,1,2,3,1,2,1]  #Definimos una lista con varios números
print(Counter(l)) # Usamos Counter para contar la frecuencia de cada elemento en la lista l y lo imprimimos

#nos muestra la cantidad de veces que se repite un valor.

# Counter({1: 4, 2: 3, 3: 2, 4: 1})