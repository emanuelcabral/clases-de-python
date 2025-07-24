#Para prevenir el fallo debemos poner el código propenso a errores en un bloque try y luego encadenar un bloque except para tratar la situación excepcional mostrando que ha ocurrido un fallo:

try: 
    n= float(input("ingresar n:\n")) #input dan una cadena

    m = 0

    print(f"---> {n}/{m} = {n/m}")

except:
    print("algo salio mal! :( ")
