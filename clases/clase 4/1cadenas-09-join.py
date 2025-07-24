# Esta función integrada sirve para devolver una cadena separada a partir de una especie de separador. 
# Se escribe como: "separador".join("cadena"). 

# Nota: Si no se especifica el separador nos devuelve un error.

cadena = "Hola mundo"
print(cadena)
print(",".join(cadena))
# "H,o,l,a, ,m,u,n,d,o"

print(" ".join(cadena))
# "H o l a   m u n d o"

#split y join son similares pero split permite separar en palabras y join separa en caracteres