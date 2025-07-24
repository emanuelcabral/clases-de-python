from datetime import datetime , timedelta

dt = datetime.now() # Obtenemos la fecha y hora actual
print(dt.strftime("%A %d de %B del %yY - %H: %M")) #strftime significa "string format time"
#Tuesday 18 de June del 24Y - 20: 30


#Detalles a tener en cuanta para dar formato:

# %A: Representa el nombre completo del día de la semana, por ejemplo, "Tuesday".
# %d: Representa el día del mes como un número decimal, por ejemplo, "18".
# %B: Representa el nombre completo del mes, por ejemplo, "June".
# %Y: Representa el año como un número decimal de cuatro dígitos, por ejemplo, "2024".
# %H: Representa la hora en formato de 24 horas como un número decimal de dos dígitos, por ejemplo, "20".
# %M: Representa los minutos como un número decimal de dos dígitos, por ejemplo, "30".