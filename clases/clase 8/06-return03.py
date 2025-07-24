# Algo interesante que pasa si devolvemos una colección es que podemos utilizarla directamente desde la función y hacer uso de las funciones internas de las colecciones:

# Sin embargo, cada vez que hagamos un print a una función la estaremos llamando, por lo que lo ideal es asignarlo a una variable y trabajarlo desde ahí: 


def lista(): # se define la funcion lista
    return [1,2,3,4,5] #retornamos la lista con los valores 1,2,3,4,5
print(lista()[1:3])  #lanzamos un print con los valores 2 y 3 de nuestra lista a causa del slicing
#[2,3]

variable = lista() #se almacena la funcion en una variable
print(variable[1:4]) #se lanza el print y se llama a la variable aplicando slicing
#[2,3,4]