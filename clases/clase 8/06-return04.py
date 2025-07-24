
#Una característica interesante, es la posibilidad de devolver valores múltiples separados por comas:


def test(): #se define la funcion sin parametros
    return "Python", 20, [1,2,3]  #retorna varios valores

#test() ##con el test no muestra la funcion porque no presenta parametros
print(test()) #lanzando el print de la funcion nos devuelve los valores
# ('Python', 20, [1, 2, 3])

print(type(test())) #aca podemos comprabar que es una tupla

#<class 'tuple'>