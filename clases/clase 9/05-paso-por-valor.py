#Los números se pasan por valor y crean una copia dentro de la función, no les afecta externamente lo que hagamos con ellos en la función:

def doblar_valor(numero):
    numero *= 2
    print("este es el valor de numero dentro de una funcion:",numero)

numero = 10.5
doblar_valor(numero)
print(numero)

#10
#el valor que devuelve es 10 porque al trabajar con numeros se genera una copia dentro de la funcion
#se puede visualizar que no modifica su valor.