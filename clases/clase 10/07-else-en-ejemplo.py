while (True):
    try:  
        a = float(input("Introduce un número: "))
        b = float(input("Introduce otro número: "))
        print(a + b)
    except:
        print("Ha ocurrido un error. Tienes que introducir 2 números.")
    else:
        print("La suma se ha realizado correctamente.")
        break  # Importante romper la iteración si todo ha ido bien.




# El bloque else en Python se ejecuta cuando el bloque try no genera ninguna excepción