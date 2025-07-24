# Consigna

# Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:  
# Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación: 
# nota_1 cuenta como el 20% de la nota final
# nota_2 cuenta como el 30% de la nota final
# nota_3 cuenta como el 50% de la nota final

# Aspectos a incluir

# Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto. 
# Los datos deben guardarse en variables y deben ser dinámicos por medio de input.


nota_1 = int(input("ingresa la primer nota:"))
nota_2 = int(input("ingresa la segunda nota:"))
nota_3 = int(input("ingresa la tercer nota:"))

nota_final = nota_1 * 0.2 + nota_2 * 0.3 + nota_3 * 0.5

print("la nota final es de: ", nota_final)