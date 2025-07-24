#Pasaremos de milímetros a metros según el parámetro de la función

# Descripción de la actividad. 

# Realiza una función que, dependiendo de los parámetros que reciba, convierta a milímetros o a metros.  
# 1- Si recibe un argumento, supone que son milímetros y convierte a metros, centímetros y milímetros.
# 2- Si recibe 3 argumentos, supone que son metros, centímetros y milímetros y los convierte a milímetros.


def convertir_longitud(*args):
    if len(args) == 1:
        milimetros = args[0]
        metros = milimetros / 1000
        centimetros = milimetros / 10
        return metros, centimetros, milimetros
    elif len(args) == 3:
        metros, centimetros, milimetros = args
        total_milimetros = metros * 1000 + centimetros * 10 + milimetros
        return total_milimetros
    else:
        return "Número incorrecto de argumentos. La función acepta 1 o 3 argumentos."

# Ejemplos de uso:

# Conversión de milímetros a metros, centímetros y milímetros
print(convertir_longitud(5000))  # Salida: (5.0, 500.0, 5000)

# Conversión de metros, centímetros y milímetros a milímetros
print(convertir_longitud(2, 50, 300))  # Salida: 25300

