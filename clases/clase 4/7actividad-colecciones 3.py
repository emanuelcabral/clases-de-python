# Descripción de la actividad. 

# Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}. 

# Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar. 

# En el caso de ingresar una divisa no existente en nuestro diccionario, deberemos indicarle con un mensaje de notificación que la divisa no se encuentra disponible. 

monedas = {'Dolar':'$','Euro':'€', 'Libra':'£'}

# print(monedas.get(input("ingresa el tipo de moneda: "), "no se encuentra esa moneda"))

# para este otro ejemplo agregamos un input para que ingrese un monto y se lo concatene al signo de la moneda
print(monedas.get(input("ingresa el tipo de moneda: "), "no se encuentra esa moneda ") + input("ingrese el monto de su moneda: "))