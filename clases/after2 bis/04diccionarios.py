# Crear un diccionario con los valores de juan:20, majo:25, marcos:30, juliana:35
# Con get deberan consultar el valor de majo
# Buscaran todas las claves del diccionario con una funcion integrada, cual?
# Ahora deberan mostrar todos los valores con una funcion integrada, cual?
# Por último agregaran lo siguiente esteban:24, leo:20, que funcion puedo utilizar?






# Crear un diccionario con los valores de juan:20, majo:25, marcos:30, juliana:35
personas = {
    "juan": 20,
    "majo": 25,
    "marcos": 30,
    "juliana": 35
}
print(personas)

# Con get deberan consultar el valor de majo
edad_majo = personas.get("majo")
print(edad_majo)  # Salida: 25


# Buscaran todas las claves del diccionario con una funcion integrada keys
claves = personas.keys()
print(claves)  # Salida: dict_keys(['juan', 'majo', 'marcos', 'juliana'])


# Ahora deberan mostrar todos los valores con una funcion integrada values
valores = personas.values()
print(valores)  # Salida: dict_values([20, 25, 30, 35])

# Por último agregaran lo siguiente esteban:24, leo:20 utilizando la funcion integrada update
personas.update({"esteban": 24, "leo": 20})
print(personas)
