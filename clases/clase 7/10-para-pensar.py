#¿Qué pasó en este ejemplo? 

c = -3
while c < 10:
    c += 1
    if c == 2:
        pass
    print('c vale', c)


# Primero, establecemos una variable llamada 'c' y le damos el valor de -3. Luego, comenzamos un bucle que continuará hasta que 'c' sea mayor o igual a 10. En cada paso del bucle, aumentamos 'c' en 1 y mostramos su valor. Sin embargo, hay una pequeña excepción: cuando 'c' es igual a 2, no mostramos su valor, pero en lugar de eso simplemente continuamos con el siguiente número. Aunque hay una línea que dice 'pass' para manejar el caso de 'c' igual a 2, no hace nada especial aquí. En resumen, este programa simplemente muestra números desde -2 hasta 10, saltándose el número 2."