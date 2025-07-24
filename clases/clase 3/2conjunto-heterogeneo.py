#En otros lenguajes, las colecciones tienen una restricción la cual solo permite tener un tipo de dato. 
#Pero en Python, no tenemos esa restricción. 
#Podemos tener un conjunto heterogéneo que contenga números, variables, strings, o tuplas.

mi_var = 'Una variable'
datos = {1, -5, 123.1,34.32, 'Una cadena', 'Otra cadena', mi_var}
print(datos)
print(type(datos))


#Los conjuntos al igual que las listas son mutables.
#Ademas los conjuntos no mantienen un orden especifico,
#con lo cual no se puede acceder a los elementos por su indice
#No se puede trabajar con el indice ni slicing
