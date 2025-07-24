#Python, nos deja asignar unos valores por defecto a los parámetros, 
#es decir, indicarle que tendrán un valor por defecto si no viene ningún valor.

def resta(a=10, b=5):
    return a - b

resultado = resta()
print(resultado)
#5

#aca en esta funcion se pasaron los valores a la funcion dentro de los parametros