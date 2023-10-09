"""
Nombre: Julián Alexis Cano Cruces
Fecha: 9/10/23
Ejercicio: problema1_practica3
"""

datos = []

for i in range (5):
    dato = int (input("Ingrese un valor númerico entero :",))
    datos.append (dato)
    
tuplaDatos = tuple(datos)

def mostrar_tupla (tupla):
    for elemento in tupla:
        print (elemento)

mostrar_tupla (tuplaDatos)

print ("La longitud de la tupla es:", len(tuplaDatos))

def sumar_tupla(tupla):
    total = sum(tupla)
    
    return total

resultado = sumar_tupla(tuplaDatos)
print ("La suma total de los datos en la tupla es de: ", resultado)

mostrar_tupla(tuplaDatos)

ultimo = tuplaDatos[-1]
tuplaDatos = tuplaDatos[:-1] + (ultimo * 2,)


print ("El contenido despues de la tupla luego de elimar el ultimo elemento es:", tuplaDatos)

def multi_tupla(tupla):
    total = 1
    for elemento in tupla:
        total *= elemento
    return total

resultado_multi = multi_tupla(tuplaDatos)
print ("El resultado de multiplicar la tupla es:", resultado_multi)

def sumar_tuplas(tupla1, tupla2):
    sumar_tuplas = tuple(x + y for x, y in zip (tupla1, tupla2))  
    return sumar_tuplas
    
    
    
datos2 = []

for i in range (5):
    dato2 = int (input("Ingrese un valor númerico entero :",))
    datos2.append (dato2)
    
tuplaDatos2 = tuple(datos2)

resultado_suma_tupla = sumar_tuplas(tuplaDatos, tuplaDatos2)

print ("El resultado de la suma de tuplas es:", resultado_suma_tupla)




        
    