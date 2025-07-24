#Igual que en la sentencia while podemos usar también las instrucciones break continue y pass.


for numero in range(10):
    if numero == 2:
        continue
    elif numero == 8:
        break
    else:
        print("Se terminó de iterar y numero vale: ", numero)
