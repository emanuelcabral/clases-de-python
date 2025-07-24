# Como vimos, si pasamos ordenado el argumento, se verá reflejado ordenadamente el parámetro. 
# Para cambiar esto se utiliza la asignación de argumentos por nombre, si indicamos durante la llamada que valor tiene cada parámetro a partir de su nombre:

def resta(a, b):
    return a - b
resultado = resta(b=15, a=12)
print(resultado)
