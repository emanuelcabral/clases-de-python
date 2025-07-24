#ejemplo:

try:
    # Intentamos dividir un número por cero
    result = 10 / 0
except ValueError:
    # Este bloque except solo captura errores de tipo ValueError
    print("Ocurrió un error de tipo ValueError.")



#para que salga el error del except este seria el codigo

# try:
#     # Intentamos dividir un número por cero
#     result = 10 / int("no es numero")
# except ValueError:
#     # Este bloque except solo captura errores de tipo ValueError
#     print("Ocurrió un error de tipo ValueError.")
