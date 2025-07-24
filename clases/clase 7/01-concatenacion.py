nombre = "oscar"
apellido = "valdez"
edad = 34

print("1-mi nombre y apellido es", nombre , apellido , "tengo", edad, "años de edad")
#otra manera seria usando el metodo format
print("2-mi nombre y apellido es {} {} tengo {} años de edad" .format(nombre, apellido, edad) )
#otra forma de concatenar f-strings (formatted string literals) - literales de cadena formateados
print(f"3-mi nombre y apellido es {nombre} {apellido} tengo {edad} años de edad")