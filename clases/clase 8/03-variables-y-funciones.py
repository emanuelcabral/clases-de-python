#Ten en cuenta que las variables creadas en una función no existen fuera de la misma, 
#es decir son variables locales.

# variable_test = 100
def test():
    variable_test = 10
    print(variable_test)

print(variable_test)


# test()

# NameError: name 'variable_test' is not defined
