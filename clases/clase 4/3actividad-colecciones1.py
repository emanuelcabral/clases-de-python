# Descripción de la actividad. 

# Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:

# gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista

########################################

# Transforma el texto en:

# Gordon lanzó su curva...
# - Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# - Dos pies le corrigió Troop.
# - Strawberry menea la cabeza como disgustado… -agrega el comentarista.

# Lo único prohibido es modificar directamente el texto

texto_original = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

# Reemplazar los caracteres especiales con los adecuados para formatear el texto
texto_formateado = texto_original.replace("&", "\n-").replace("curva", "curva...")
# Capitalizar el nombre "Gordon"
texto_formateado = texto_formateado.replace("gordon", "Gordon").replace("strawberry","Strawberry")

# Imprimir el resultado
print(texto_formateado)