def juego1():
    print("###################################")
    print("juguemos a piedra, papel o tijera")
    print("###################################")
    print("\n ingresa 1 para piedra \n ingresa 2 para papel \n ingresa 3 para tijera \n ")
    print("###################################")

    piedra = int(1)
    papel = int(2)
    tijera = int(3)

    while str(input("ingrese fin para terminar: ")) != "fin":
    
        usuario1 = int(input("Turno jugador 1 \n ingresa \n 1 para piedra \n 2 para papel \n 3 para tijera: \n"))
        usuario2 = int(input("Turno jugador 2 \n ingresa \n 1 para piedra \n 2 para papel \n 3 para tijera: \n"))
        
        if usuario1 == 1 and usuario2 == 3 :
            print("##########################")
            print("usuario 1 gana")
            print("piedra le gana a tijera")
            print("##########################")
        elif usuario1 == 2 and usuario2 == 1:
            print("##########################")
            print("usuario 1 gana")
            print("papel le gana a piedra")
            print("##########################")
        elif usuario1 == 3 and usuario2 == 2:
            print("##########################")
            print("usuario 1 gana")
            print("tijera le gana a papel")
            print("##########################")
        elif usuario1 == 1 and usuario2 == 2:
            print("##########################")
            print("usuario 2 gana")
            print("papel le gana a piedra")
            print("##########################")
        elif usuario1 == 2 and usuario2 == 3:
            print("##########################")
            print("usuario 2 gana")
            print("tijera le gana a papel")
            print("##########################")
        elif usuario1 == 3 and usuario2 == 1:
            print("##########################")
            print("usuario 2 gana")
            print("piedra le gana a tijera")
            print("##########################")
        elif usuario1 > 3 or usuario2 > 3:
            print("##########################")
            print("El numero ingresado es incorrecto")
            print("##########################")
        elif usuario1 <= 0 or usuario2 <= 0:
            print("##########################")
            print("El numero ingresado es incorrecto")
            print("##########################")
        else:
            print("##########################")
            print("empate")
            print("##########################")

juego1()