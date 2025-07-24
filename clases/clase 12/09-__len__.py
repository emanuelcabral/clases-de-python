class Vector():
    # Define el método de inicialización (__init__) que se ejecuta automáticamente al crear un objeto de la clase.
    # Se inicializa el atributo _data con el valor pasado como argumento.
    def __init__(self, data):
        self._data = data

    # Define el método especial __str__, que se llama automáticamente al imprimir un objeto de la clase.
    # Devuelve una representación en cadena del objeto Vector y su contenido.
    def __str__(self):
        return f"The values are: {self._data}"

    # Define el método especial __len__, que se llama automáticamente cuando se usa la función len() en un objeto de la clase.
    # Devuelve la longitud de los datos contenidos en el atributo _data.
    def __len__(self):
        return len(self._data)

# Crea un objeto de la clase Vector con la lista [1, 2] como su único dato.
v = Vector([1,2])

# Imprime la longitud del objeto v, lo que automáticamente llama al método __len__ de la clase Vector.
print(len(v))

#2
