#Como vemos, siempre nos indica "class" delante. 
#Eso es porque en Python todo son clases, pero hablaremos de este concepto más adelante. 
#Lo importante ahora es que podemos mostrar solo el nombre del tipo de dato (la clase) 
#consultando su propiedad especial name de la siguiente forma:

e=True

print( type(e).__name__)
print(type(1).__name__)
print(type(3.14).__name__)
print(type([]).__name__)
print(type(()).__name__)

#ahora solo muestra el nombre sin la palabra class
