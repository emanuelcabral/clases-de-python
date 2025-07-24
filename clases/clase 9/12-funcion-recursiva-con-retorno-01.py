#Un ejemplo de una función recursiva con retorno, 
#es el ejemplo del cálculo del factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número.

def factorial(numero):

    print("valor inicial ->", numero)

    if numero > 1:
        
        numero = numero * factorial(numero -1)

    print("valor final ->", numero)

    return numero

print(factorial(5))

# valor inicial -> 5
# valor inicial -> 4
# valor inicial -> 3
# valor inicial -> 2
# valor inicial -> 1
# valor final -> 1
# valor final -> 2
# valor final -> 6
# valor final -> 24
# valor final -> 120
# 120


#n= 5 * f(4) #f(4)= 120
#n= 4 * f(3) #f(3)= 24
#n= 3 * f(2) #f(2)= 6
#n= 2 * f(1) #f(1)= 2
#n= 1 * f(0) #f(0)= 1


#desglozamiento

# def factorial(numero):
#     print("valor inicial -> 5")
#     if 5 > 1:
#         numero = 5 * factorial(4)
#     print("valor final -> 120")
#     return 120

# def factorial(numero):
#     print("valor inicial -> 4")
#     if 4 > 1:
#         numero = 4 * factorial(3)
#     print("valor final -> 24")
#     return 24

# def factorial(numero):
#     print("valor inicial -> 3")
#     if 3 > 1:
#         numero = 3 * factorial(2)
#     print("valor final -> 6")
#     return 6

# def factorial(numero):
#     print("valor inicial -> 2")
#     if 2 > 1:
#         numero = 2 * factorial(1)
#     print("valor final -> 2")
#     return 2

# def factorial(numero):
#     print("valor inicial -> 1")
#     if 1 > 1:
#         numero = 1 * factorial(0)
#     print("valor final -> 1")
#     return 1

# 1 * 1 = 1     ->  factorial(1)
# 2 * 1 = 2     ->  factorial(2)
# 3 * 2 = 6     ->  factorial(3)
# 4 * 6 = 24    ->  factorial(4)
# 5 * 24 = 120  ->  factorial(5)