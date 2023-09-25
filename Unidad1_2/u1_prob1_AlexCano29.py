'''
Nombre: Alexis Cano
Fecha: 25 septiembre
Ejercicio: ej.2 modulo 2

'''
#Resuelve el siguiente problema de raices mediante formula general

print ("Dame 3 valores a usar en la formula general")
print("a")
a = int (input())
print("b")
b = int (input())
print("c")
c = int (input())

print ("Dados tus valores la función a tratar es:", a ,"+", b ,"+",c)


form_g= ((-b+((b**2-(4*a)*c ))*1/2)/(2*a))

print("El resultado de la formula general es:",form_g)


