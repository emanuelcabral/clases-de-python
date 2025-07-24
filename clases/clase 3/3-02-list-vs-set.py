#Como hablamos, las listas son mutables, sin embargo, el set también es mutable,
# pero no podemos hacer slicing, ni manejar un set por índice.

conjunto = {"a", "b", "c", "d", "e", "f"}
print(conjunto)

conjunto[:3] = ["A", "B", "C"]
print(conjunto)

#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'set' object is not subscriptable
