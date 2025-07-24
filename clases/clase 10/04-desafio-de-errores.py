#Retorna None cuando sucede el fallo 

#Descripción de la actividad. 

# En la función de nuestro ejercicio hay un fallo potencial, averigua cuándo sucede y retorna el valor None en ese caso especial, en cualquier otro caso devuelve el resultado normal de la función.

# >>> def dividir(a, b):
# return a/b

# Pista: Valor indeterminado


def dividir(a, b):
    if b == 0:
        return None
    return a / b

print(dividir(10, 2))  # Debería retornar 5.0
print(dividir(10, 0))  # Debería retornar None
print(dividir(10, 5))  # Debería retornar 2.0
print(dividir(-10, 2)) # Debería retornar -5.0


#cuando dividimos por cero nos arroja un error ZeroDivisionError: division by zero