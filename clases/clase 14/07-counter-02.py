from collections import Counter

estudiantes = "Nicolas Claudio Brenda Flor Nicolas Flor"

print(Counter(estudiantes))
#Counter({'o': 5, 'l': 5, ' ': 5, 'a': 4, 'i': 3, 'r': 3, 'N': 2, 'c': 2, 's': 2, 'd': 2, 'F': 2, 'C': 1, 'u': 1, 'B': 1, 'e': 1, 'n': 1})

print(Counter(estudiantes.split()))
#Counter({'Nicolas': 2, 'Flor': 2, 'Claudio': 1, 'Brenda': 1})