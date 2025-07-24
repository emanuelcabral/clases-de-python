#el semaforo

#Escribe un programa en Python que simule el comportamiento de un semáforo. El programa debe solicitar al usuario ingresar un número que corresponda al color del semáforo (1 para verde, 2 para amarillo, 3 para rojo). Dependiendo del número ingresado, el programa debe imprimir el mensaje correspondiente: "Circule!" para verde, "Precaucion!" para amarillo y "Detenerse!" para rojo.

color_luz = input("ingrese color de semaforo (1 - verde / 2 - Amarillo / 3 -Rojo): ")
if color_luz == "1":
	print("Circule!")
elif color_luz == "2":
	print("Precaucion!")
else:
	print("Detenerse!")