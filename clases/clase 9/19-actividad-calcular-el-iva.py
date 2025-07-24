###########################################################################
# #funciones con parametros calcular el IVA
###########################################################################

#crear la funcion impuesto con parametros
#mostrar mensaje del precio del producto sin iva
#mostrar mensaje del valor del iva del producto
#mostrar el valor del producto mas iva
#el iva debe ingresarse por teclado y el valor del producto igual ambos deben ser flotantes.

def impuesto(iva, producto):
    print("el precio del producto sin iva es: ", producto)
    soloiva = (producto * iva)/100
    print("el iva del producto es: ", soloiva)
    productoiva = soloiva + producto
    print("el precio del prducto con iva: ", productoiva)

# impuesto(21,15000)
impuesto(float(input("ingrese el iva: ")), float(input("ingrese el valor del producto: ")))


#-----------------otra alternativa con **kwars --------------------------------#

# def impuesto(**kwars):
#     for key, value in kwars.items():
#         print("Producto: {}, precio sin IVA: {}".format(key, value))
#         iva = 0
#         iva = value * 0.21
#         prod_con_iva = 0
#         prod_con_iva = value + iva
#         print("IVA: {}, Total: {}".format(iva,prod_con_iva))

# impuesto(jabon=3000,carne=8000,pan=2500)