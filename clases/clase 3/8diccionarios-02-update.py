#Este método actualiza un diccionario agregando los pares clave-valores. 

numeros =  {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
print(numeros)
numeros.update({'cinco': 5, 'seis': 6}) 
print(numeros)
# {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6}

#otra forma seria creando otro diccionario y actualizandolo con update:
otro_dict = dict(siete=7)
numeros.update(otro_dict)
print(numeros)
# {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7}
