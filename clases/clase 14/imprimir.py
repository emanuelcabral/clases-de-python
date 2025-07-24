# imprimir.py
import sys

if len(sys.argv) == 2:
    texto = sys.argv[1]
    print(f"Texto recibido: {texto}")
else:
    print("Error - Introduce un solo argumento")
    print('Ejemplo: python imprimir.py "Hola Mundo"')