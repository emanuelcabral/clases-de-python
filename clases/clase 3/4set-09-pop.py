#La función pop retorna un elemento en forma aleatoria 
#(no podría ser de otra manera, ya que los elementos no están ordenados). 
#Así, el siguiente bucle imprime y remueve uno por uno los miembros de un conjunto.


#En este ejemplo borra todos los elementos del set
numeros =  {1,2,3,4}
while numeros: # Mientras haya elementos en el set
    print("Se está borrando: ", numeros.pop()) # Elimina y devuelve un elemento, luego lo imprime

# el resultado sera
# Se está borrando:  1
# Se está borrando:  2
# Se está borrando:  3
# Se está borrando:  4


#otro ejemplo mas
numeros =  {5,6,7,8}
while numeros: # Mientras haya elementos en el set
    print("Se está borrando: ", numeros.pop()) # Elimina y devuelve un elemento, luego lo imprime


# De esta forma elimina un item de forma ramdom
numeros =  {"hola",5,1,2,3,4}
print(numeros)

print(numeros.pop())
print(numeros.pop())