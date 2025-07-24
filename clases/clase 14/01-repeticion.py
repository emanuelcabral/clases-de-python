import sys # Importa el módulo sys para acceder a los argumentos de la línea de comandos.

cadena = sys.argv[1] # Asigna el primer argumento de la línea de comandos al variable cadena.

repeticiones = int(sys.argv[2])
# Convierte el segundo argumento de la línea de comandos a un entero y lo asigna a la variable repeticiones.

for repeticion in range(repeticiones): # Se crea un bucle
    
    print(cadena) # Imprime la cadena especificada por el usuario tantas veces como indique repeticiones.

