'''
Nombre: Alexis Cano
Fecha: 25 septiembre
Ejercicio: ej.1 modulo 2

'''
#Una panaderia vende barras de pan a $3.49 cada una. El pan que no es del dia tiene un descuento
# del 60%. Escribe un programa que lea el numero de barras vendidas que no son del dia, despues 
# debera mostrar el precio habitual, el descuento y el coste final.

print("¿Cuantas barras pan del dia anterior se vendio?")
venta = float (input ())
pan = 3.49
precio_habitual = venta * pan
descuento= precio_habitual * 0.60

total= precio_habitual - descuento

print("El precio que se pagaria habitualmente es:", precio_habitual)
print("El descuento por la compra es de un total de:", descuento)
print("El total a pagar con el descuento ya aplicado es de:", total)


