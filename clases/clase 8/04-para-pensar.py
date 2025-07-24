#Si las variables creadas en una función, solo existen dentro de esa función ¿Cómo explicarías esto?

variable_test = 10
def test():
		print(variable_test)

# variable_test = 100
test()


#Es el scope determina dónde y cómo se pueden usar las variables en el código. Comprender el scope es fundamental para evitar errores y escribir código claro y efectivo.

#Aunque las variables creadas dentro de una función solo existen dentro de esa función (variables locales), las variables definidas fuera de las funciones (variables globales) pueden ser accedidas desde cualquier parte del código, incluidas las funciones. En tu ejemplo, variable_test es una variable global, por lo que la función test() puede acceder y usar esta variable.