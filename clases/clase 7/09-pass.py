

#Ejemplo 1
n = 0
while n < 10:
    n += 1
    # n=n+1
    if n == 2:
        pass
    print('n vale' , n)  #se ejecuta 10 veces porque esta dentro del while

#Ejemplo 2
# n = 0
# while n < 10:
#     n += 1
#     if n == 2:
#         pass
#         print('n vale' , n) #solo se ejecuta cuando n valga 2 porque esta dentro del if

#Ejecuta el código para analizar las diferencias ☺


# Diferencias clave:

# En el Ejemplo 1, print('n vale', n) se ejecuta en cada iteración del bucle while, por lo tanto, imprime el valor de n desde 1 hasta 10.

# En el Ejemplo 2, print('n vale', n) solo se ejecuta cuando n es igual a 2, debido a que está indentado dentro del bloque if.

# Esta diferencia de indentación cambia completamente el comportamiento del programa y el resultado final.



# pass es una herramienta que te permite mantener la estructura y la sintaxis correctas en tu código cuando no necesitas ejecutar ninguna acción en un punto específico. Es una forma de indicar explícitamente que no hay ninguna acción planeada en ese lugar, en lugar de simplemente dejarlo vacío, lo que podría dar lugar a errores de sintaxis.