#login

#Escribe un programa en Python que simule un sistema de login sencillo. El programa debe solicitar al usuario ingresar un nombre de usuario y una contraseña. Si el nombre de usuario es "ema" y la contraseña es "12345", el programa debe imprimir "Bienvenido". En caso contrario, debe imprimir "Usuario incorrecto".

# el usuario cargado es ema y el pass es 12345
user = input("ingrese su usuario : ")
password = input("ingrese su contraseña : ")

if password == 12345 and user == "ema":
	print("Bienvenido")
else:
	print("Usuario incorrecto")