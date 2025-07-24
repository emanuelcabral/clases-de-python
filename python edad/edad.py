anio_act= int(input("Ingrese el año actual:")) 
mes_act= int(input("Ingrese el mes actual:")) 
dia_act= int(input("Ingrese el dia actual:"))
anio_nac= int(input("Ingrese el año de nacimiento:")) 
mes_nac= int(input("Ingrese el mes de nacimiento:"))
dia_nac= int(input("Ingrese el dia de nacimiento:"))
edad_sup = anio_act - anio_nac
edad_final = edad_sup

if anio_act > anio_nac :
    print("la diferencia de años es de: ↓↓")
    print(anio_act - anio_nac)
    if mes_act < mes_nac:
        print("la dif de meses es de: ↓↓")
        print(mes_nac - mes_act)
        print("tu edad es la sig: ↓")
        print(edad_final - 1)
        if dia_act > dia_nac:
            print("la dif de dias es de: ")
            print(dia_act - dia_nac)
            print("tu edad es la sig:")
            print(edad_final - 1)
        if dia_act < dia_nac:
            print(dia_act - dia_nac)
            print("tuedad es ↓↓↓:")
            print(edad_final - 1)
        if dia_act == dia_nac:
            print("tuedad es ↓↓↓↓↓:")
            print(edad_final - 1)
    if mes_act > mes_nac:
        print(mes_act - mes_nac)
        print("tu edad es ↓↓↓↓↓↓↓↓↓:")
        print(edad_final)
    if mes_act == mes_nac:
        if dia_act > dia_nac:
            print(dia_act - dia_nac)
            print("ya paso tu cumple tu edad es :")
            print(edad_final)
        if dia_act < dia_nac:
            print("falta poco para tu cumple y tu edad es:")
            print(edad_final - 1)
        if dia_act == dia_nac:
            print("feliz cumple, tu edad es:")
            print(edad_final)

elif anio_act < anio_nac:
    print("esto no es posible")

        
elif anio_act == anio_nac:
    if mes_act < mes_nac:
        print("esto no es posible por el mes indicado, todavia no viajamos al futuro!")
    if mes_act > mes_nac:
        print("no has cumplido años porque no has nacido!!")
    if mes_act == mes_nac:
        if dia_act > dia_nac:
            print("error en la fecha")
        if dia_act < dia_nac:
            print("tu edad es:")
            print(edad_final)
            print("eres recien nacido tines tantos dias... PROXiMAMENTE")
        if dia_act == dia_nac:
            print("hoy es tu nacimiento")