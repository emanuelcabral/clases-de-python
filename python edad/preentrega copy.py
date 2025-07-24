# from os import uname_result
# from visual import drive
# drive.mount("/drive/" , force_remount=True)

# ruta = "/content/basecoder"

nuevo_usuario = str()
si = "y"
no = "n"

print("ingrese → y ← para un si o → n ← para un no")
nuevo_usuario = input("desea realizar un registro de un nuevo usuario? ")
while nuevo_usuario == si:
    if nuevo_usuario == si:
        print("has ingresado un si, por favor complete lo siguiente")
        usuario = input("ingresa tu usuario: ")
        contraseña = input("ingresa tu contraseña: ")
        base = [ usuario + ":" + contraseña ]
        print(base)
        base.append("otro usuario")
        print(base)
        #base_final = base + ":" + base
        #print(base_final)
        bases = {"USUARIO": usuario, "CONTRASEÑA": contraseña}
        print(base)
    else:
        print("gracias y vuelve cuando quieras registrar un usuario")
#reg ={usuario:contraseña}
#print(reg)
#reg[usuario] = contraseña

# f = open("/content/basecoder/archivo.txt", "w")
# f.write(bases["USUARIO"] + ":" + bases["CONTRASEÑA"])
# f.close()