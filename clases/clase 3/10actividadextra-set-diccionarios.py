# Consigna Sets 

# Crear un conjunto en Python que posea los siguientes elementos:
# Países: Inglaterra, USA, México.
# Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA
# Elimina a los países: Chile e Italia
# Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove?, ¿Qué pasó con el element de USA?


Paises = {"Inglaterra", "USA", "México"}
print(Paises)

Paises.update(["Islandia", "Italia", "Argentina y Portugal", "USA"])
print(Paises)
#como USA ya se encontraba no lo agrega. Recordemos que los set no agrega valores duplicados

Paises.discard("Italia") #Elimina al item "Italia"
Paises.discard("Chile") #Como "chile" no se encuentra dentro del set no elimina nada.
print(Paises)

# Paises.remove("Chile", "USA")
# Paises.remove("USA")
# Paises.remove("Chile")
print(Paises)

#Cuando queremos remover un item inexistente nos lanza un error por que no encuentra el item.
#Como el item USA ya se encontraba en el set, lo ignora.


################################################################################

# Consigna Dicts

# Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:
# Ejemplo del output solicitado: 
# Juan tiene 25 años, y vive en Carrera 7 - Bogotá

# Usuario = {"Nombre": input("ingresa tu nombre:"), "Edad": int(input("ingresa tu edad:")), "Direccion": input("ingresa tu domicilio:") }
# print(Usuario)

#-------------------otra alternativa-----------------------------#

# Crear un diccionario para almacenar la información del usuario
usuario = {}

# Solicitar al usuario su nombre, edad y dirección
usuario['nombre'] = input("Por favor, introduce tu nombre: ")
usuario['edad'] = input("Por favor, introduce tu edad: ")
usuario['direccion'] = input("Por favor, introduce tu dirección: ")

# Mostrar la información del usuario por pantalla
# print(f"{usuario['nombre']} tiene {usuario['edad']} años, y vive en {usuario['direccion']}.")
print(usuario['nombre'] + " tiene " + usuario['edad'] + " años, y vive en " + usuario['direccion'] + ".")

