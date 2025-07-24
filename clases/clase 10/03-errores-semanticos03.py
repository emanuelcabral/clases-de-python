# Cuando leemos un valor con la función input(), éste siempre se obtendrá como una cadena de caracteres. Si intentamos operarlo directamente con otros números tendremos un fallo TypeError que tampoco detectan los editores de código:

n = input("ingresar n:\n")

m = 4
print(type(n))
print(type(m))

print(f"--->{n}/{m} = {n/m}")

# Traceback (most recent call last):
#   File "c:\Users\emanu\OneDrive\Desktop\py\clases\clase 10\03-errores-semanticos03.py", line 7, in <module>
#     print(f"--->{n}/{m} = {n/m}")
#                            ~^~
# TypeError: unsupported operand type(s) for /: 'str' and 'int'


#El error es que cada vez que ingresamos por input un valor es tenido en cuenta como string
#Al querer realizar una operacion matematica como una division nos devuelve error
#la solucion es convertirlo a flotante o entero.