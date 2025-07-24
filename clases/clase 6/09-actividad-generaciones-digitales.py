# Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado
# Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: “No existe generación asociada”


fecha_de_nacimiento = int(input("ingresa tu fecha de nacimiento: "))

if fecha_de_nacimiento >= 1920 and fecha_de_nacimiento < 1940:
    print("Eres de la generacion silenciosa")
elif fecha_de_nacimiento >= 1946 and fecha_de_nacimiento < 1964:
    print("Eres de la generacion bommer")
elif fecha_de_nacimiento >= 1965 and fecha_de_nacimiento < 1979:
    print("Eres de la generacion X")
elif fecha_de_nacimiento >= 1980 and fecha_de_nacimiento < 2000:
    print("Eres de la generacion Y")
elif fecha_de_nacimiento >= 2000 and fecha_de_nacimiento < 2010:
    print("Eres de la generacion Z")
else:
    print("No existe generación asociada")