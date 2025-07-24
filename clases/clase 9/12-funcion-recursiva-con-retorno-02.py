


def suma_hasta(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_hasta(numero - 1)

resultado = suma_hasta(5)
print("La suma de los números hasta 5 es:", resultado)

# La suma de los números hasta 5 es: 15

#Flujo de ejecucion

# Primera llamada suma_hasta(5):

# numero = 5.
# ¿numero == 1? No, pasamos al bloque else.
# Retornamos 5 + suma_hasta(4).
# Llamada suma_hasta(4):

# numero = 4.
# ¿numero == 1? No, pasamos al bloque else.
# Retornamos 4 + suma_hasta(3).
# Llamada suma_hasta(3):

# numero = 3.
# ¿numero == 1? No, pasamos al bloque else.
# Retornamos 3 + suma_hasta(2).
# Llamada suma_hasta(2):

# numero = 2.
# ¿numero == 1? No, pasamos al bloque else.
# Retornamos 2 + suma_hasta(1).
# Llamada suma_hasta(1):

# numero = 1.
# ¿numero == 1? Sí, retornamos 1.
# Ahora, retrocediendo:

# suma_hasta(1) retorna 1.
# suma_hasta(2) retorna 2 + 1, que es 3.
# suma_hasta(3) retorna 3 + 3, que es 6.
# suma_hasta(4) retorna 4 + 6, que es 10.
# suma_hasta(5) retorna 5 + 10, que es 15.
# Entonces, el resultado final es 15, que es la suma de todos los números desde 1 hasta 5.