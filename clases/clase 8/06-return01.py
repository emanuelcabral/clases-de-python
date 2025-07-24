#Las funciones pueden comunicarse con el exterior de las mismas, 
#al proceso principal del programa usando la sentencia return. 
#La comunicación con el exterior se hace devolviendo valores. 


#A continuación, un ejemplo de función usando return:

def saludar_con_nombre(nombre):
    saludando = print('Hola {}! ¿Cómo estás?'.format(nombre))
    return saludando

saludar_con_nombre("Juan")

#Hola Juan ¿Cómo estás?


#Nota: Por defecto, las funciones retorna el valor None.


print(saludar_con_nombre("Juan"))  # Muestra none