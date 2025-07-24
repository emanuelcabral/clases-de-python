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

    # Define el método especial __getitem__, que se llama automáticamente cuando se indexa un objeto de la clase.
    # Devuelve el elemento correspondiente a la posición especificada en el atributo _data.
    def __getitem__(self, pos):
        return self._data[pos]

    # Define el método especial __setitem__, que se llama automáticamente cuando se asigna un valor a una posición de un objeto de la clase.
    # Actualiza el elemento en la posición especificada en el atributo _data con el valor dado.
    def __setitem__(self, pos, value):
        self._data[pos] = value

    # Define el método especial __iter__, que se llama automáticamente cuando se itera sobre un objeto de la clase.
    # Devuelve un iterador que produce una cadena para cada elemento en el atributo _data.
    def __iter__(self):
        for pos in range(0, len(self._data)):
            yield f"Value[{pos}]: {self._data[pos]}"

# yield devuelve un valor en cada iteración sin finalizar la función, permitiendo generar datos de manera secuencial y eficiente.

# Crea un objeto de la clase Vector con la lista [1, 2] como su único dato.
v = Vector([1,2])

# Itera sobre el objeto v, lo que automáticamente llama al método __iter__ de la clase Vector.
# Cada elemento producido por el iterador se imprime.
for vec in v:
    print(vec)

#Value[0]: 1
#Value[1]: 2
