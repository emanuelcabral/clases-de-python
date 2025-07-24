#Las listas u otras colecciones son del tipo compuesto, por lo que se pasa por referencia, 
#las modificaciones dentro de la función también se harán por fuera.


def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

listaDeNico = [10,50,100]
# print(listaDeNico)
doblar_valores(listaDeNico)

print(listaDeNico)

#[20, 100, 200]

#en cambio en este ejemplo al trabajar con una coleccion, mas precisamente una lista se pasan por referencia
#lo que significa que no se crea una copia y se trabaja directamente con la coleccion(lista en este caso)
#como se puede apreciar los valores al llamarse por fuera de la funcion se muestra una lista con los valores cambiados
