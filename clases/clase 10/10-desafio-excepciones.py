#Captura la excepción
# Descripción de la actividad. 

# Tomando la solución del ejercicio anterior, en lugar de devolver None al dividir entre cero, tienes que capturar una excepción que muestre por pantalla EXACTAMENTE el mensaje: “No se puede dividir entre cero”; si falla el código

# >>> def dividir(a, b):
# if b == 0:
#         		return None
# return a/b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return None
    
print(dividir(10, 2))  # Debería retornar 5.0
print(dividir(10, 0))  # Debería imprimir "No se puede dividir entre cero" y retornar None
print(dividir(10, 5))  # Debería retornar 2.0
print(dividir(-10, 2)) # Debería retornar -5.0