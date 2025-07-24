# La función Add permite agregar un nuevo ítem al set

numeros =  {1,2,3,4}
print(numeros)

#agregamos un item al set
numeros.add(5)
print(numeros)
#{1,2,3,4,5}

#otro ejemplo con strings y enteros
cadena = {1, "hola" , 2, "que tal", "a", "b"}
cadena.add(3)
print(cadena)

#que sucede si agrego otro valor existente
cadena = {1, "hola" , 2, "que tal", "a", "b"}
cadena.add(1)
print(cadena)