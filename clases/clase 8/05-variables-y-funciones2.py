
#El print le da prioridad a la variable dentro de la función antes que a la de afuera.


variable_test = 10
def test():
    variable_test = 155
    print(variable_test)
test()


#155

# print(variable_test) 

#si hubiesemos llamado a la variable por fuera de la funcion nos devuelve 10 el valor de la variable global