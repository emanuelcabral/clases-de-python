while (True):
    try:   
        a = float(input("Introduce un número: "))
        b = float(input("Introduce otro número: "))
        print(a + b)
    except:
        print("Ha ocurrido un error. Tienes que introducir 2 números.")
    else:
        print("La suma se ha realizado correctamente.")
        break   # Importante romper la iteración si todo ha ido bien.
    finally:
        print("Fin del bucle") # Esto se ejecuta siempre.


# Es útil para realizar tareas de limpieza (por ejemplo, cerrar archivos o liberar recursos)

# Ejecución garantizada: El bloque finally se ejecutará siempre, sin importar si se produce una excepción en el bloque try o si se maneja dicha excepción en el bloque except. Esto garantiza que ciertas acciones de limpieza o tareas importantes se realicen, incluso si ocurren errores.

# Uso común: Se utiliza comúnmente para liberar recursos adquiridos en el bloque try, como cerrar archivos, conexiones de bases de datos o liberar bloqueos, independientemente de si el código dentro del bloque try genera una excepción o no.

# Flujo de control: Después de que se ejecuta el bloque try, si se produce una excepción y hay un bloque except correspondiente, el flujo de control pasa al bloque except. Luego, después de manejar la excepción, el flujo de control pasa al bloque finally. Si no se produce ninguna excepción, el flujo de control pasa directamente al bloque finally.

# No es necesario: El bloque finally no es obligatorio en un bloque try-except. Puedes tener un bloque try sin un bloque finally, o incluso un bloque try-except sin un bloque finally. Sin embargo, si se proporciona un bloque finally, se ejecutará independientemente de si se produce una excepción o no.

# En resumen, el bloque finally es una herramienta poderosa para garantizar que ciertas tareas se realicen, independientemente de si ocurren errores en el código. Esto ayuda a mantener el código limpio y asegura una gestión adecuada de recursos.