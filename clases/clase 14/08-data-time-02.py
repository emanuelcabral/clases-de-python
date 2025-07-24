from datetime import datetime

# Creamos un objeto datetime con la fecha y hora específicas
dt = datetime(2000,1,1) 

print("la fecha y hora es:", dt) # Imprimimos la fecha y hora
# #la fecha y hora es: 2000-01-01 00:00:00



# Reemplazamos el año del datetime original por el año 3000
dt = dt.replace(year=3000)
print(dt) # Imprimimos la fecha y hora
