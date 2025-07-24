#desafio slicing

cadena_volteada = "acitametaM ,5.8 ,otipeP ordeP"
cadena = cadena_volteada[::-1]
print(cadena)
nombre_alumno = cadena[0:12:1]
print(nombre_alumno)
nota_alumno = cadena[14:17:1]
print(nota_alumno)
materia_alumno = cadena[19::1]
print(materia_alumno)

print(nombre_alumno, "ha sacado un", nota_alumno , "en", materia_alumno )