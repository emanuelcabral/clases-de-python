######################################
## cual es tu signo ?
######################################

def signo():
    mes = int(input("ingresa el mes: "))
    dia = int(input("ingresa el dia: "))

    if mes == 3 and dia >= 21 or mes == 4 and dia <= 20:
        print("eres de aries")
    elif mes == 4 and dia >= 21 or mes == 5 and dia <= 20:
        print("eres de tauro")
    elif mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
        print("eres de geminis")
    elif mes == 6 and dia >= 21 or mes == 7 and dia <= 20:
        print("eres de cancer")
    elif mes == 7 and dia >= 21 or mes == 8 and dia <= 20:
        print("eres de leo")
    elif mes == 8 and dia >= 21 or mes == 9 and dia <= 20:
        print("eres de virgo")
    elif mes == 9 and dia >= 21 or mes == 10 and dia <= 20:
        print("eres de libra")
    elif mes == 10 and dia >= 21 or mes == 11 and dia <= 20:
        print("eres de escorpio")
    elif mes == 11 and dia >= 21 or mes == 12 and dia <= 20:
        print("eres de sagitario")
    elif mes == 12 and dia >= 21 or mes == 1 and dia <= 20:
        print("eres de capricornio")
    elif mes == 1 and dia >= 21 or mes == 2 and dia <= 20:
        print("eres de acuario")
    elif mes == 2 and dia >= 21 or mes == 3 and dia <= 20:
        print("eres de pisis")
    else:
        print("has ingresado un valor invalido")

# signo()

while str(input("ingrese fin para terminar o cualquier valor para continuar: ")) != "fin":
    signo()
