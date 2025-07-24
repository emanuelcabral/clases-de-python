def juego_piedra_papel_tijera():
    print("###################################")
    print("¡Juguemos a Piedra, Papel o Tijera!")
    print("###################################")
    print("\nIngresa 1 para Piedra, 2 para Papel o 3 para Tijera\n")
    print("###################################")

    while True:
        usuario1 = int(input("Turno jugador 1\nIngresa:\n1 para piedra\n2 para papel\n3 para tijera\nO '0' para terminar: "))
        if usuario1 == 0:
            print("¡Gracias por jugar!")
            break

        usuario2 = int(input("Turno jugador 2\nIngresa:\n1 para piedra\n2 para papel\n3 para tijera: "))
        
        if usuario1 == usuario2:
            print("Empate")
        elif usuario1 == 1 and usuario2 == 3 or usuario1 == 2 and usuario2 == 1 or usuario1 == 3 and usuario2 == 2:
            print("¡Jugador 1 gana!")
        else:
            print("¡Jugador 2 gana!")

juego_piedra_papel_tijera()