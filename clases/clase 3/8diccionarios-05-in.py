# Para determinar si un elemento pertenece a un dict, utilizamos la palabra reservada in.
# Se escribe como clave_a_validar in mi_dict

numeros =  {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
print(numeros)

#Consultamos si la llave "dos" se encuentra dentro del diccionario
print('dos'in numeros)
# True - nos devuelve verdadero

#consultamos si "2" no se encuentra dentro del diccionario como llave, no como valor!
print(2 not in numeros)
# True

# consultamos si "4" se encuentra dentro del diccionario como llave,
# como no se encuentra me devuelve false
print(4 in numeros)
# False
