#Este else sirve para ejecutar un bloque de código cuando el bucle while tenga una condición False o haya terminado y no haya sido forzado a salir mediante un break.

#un ejemplo:


chance  = 1
while chance <= 3:
    txt = input("Escribe SI: ")
    if txt == "SI":
        print("Ok, lo conseguiste en el intento", chance)
        break
    chance += 1 #acumulador/contador
else:
    print("Has agotado tus tres intentos")
