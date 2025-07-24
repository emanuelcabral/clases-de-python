#not
#El not es la negación o también conocida como el NO. Es un poco especial, ya que solo afecta a los tipos lógicos True y False; solo requiere un operando en una expresión.

print(not True)
# False
print(not True == False)
# True


###############################################################

#and
#Si tenemos dos afirmaciones que son verdaderas, evidentemente estaremos diciendo la verdad. Python también puede comprender esto, es decir, si preguntamos sobre dos afirmaciones unidas por un Y, sabrá decir si es verdadero o falso.


print(2 > 1 and 5 > 2)
#True
print(5 > 20 and 20 < 1)
#False

################################################################

#or

#Ahora, veamos el operador de disyunción denominado Or en castellano O. 
#Si el AND unía, el OR separa. Es decir, si a Python le pregunto por dos afirmaciones, y al menos una es (verdadera)True, Python me dirá que esta afirmación es True.


print(2 > 1 or 5 > 2)
#True
print(5 < 20 or 20 < 1)
#True
