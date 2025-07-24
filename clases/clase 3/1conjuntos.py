#Esta es la forma correcta de declarar un conjunto
conjunto =  {1, 2, 3, 4}
print(conjunto)
otro_conjunto = {"Hola", "como", "estas", "?"}
print(otro_conjunto)


#que sucede si al conjunto se le agrega valores duplicados?
conjunto2 =  {1, 2, 3, 4, 2, 1}
print(conjunto2)
#Solo crea el conjunto sin los valores duplicados

#En muchas ocasiones podremos ver distinto el orden de nuestros items,
# ya que no siempre respeta el orden declarado
conjunto3 =  {100, 120, 30, 40, 20, 10}
print(conjunto3)

#En este otro caso aleatorio.
conjunto4 =  {100, 120, 30, 40, 20, 10, "string1" , "string3", "string2" }
print(conjunto4)

#este es un conjunto vacio
conjunto_vacio = set()
print(conjunto_vacio)

# Para crear un conjunto vacío debemos decirle set()
# De lo contrario si quisiéramos hacer como las listas y crearlo con {} Python crea un diccionario