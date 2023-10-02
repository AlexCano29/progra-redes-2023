'''
Autor: Alexis Cano
Fecha 2 de Octubre
Descripcion: Problema 2

Ejercicio: u1_prob1
'''

'''Los intereses para la declaracion de ISR en un determinado pais son los siguientes:

Menos 10,000 = 5%
Entre 10,000 y 20,000 = 15%
Entre 20,000 y 35,000 = 20%
Entre 35,000 y 60,000 = 30%
Mas de 60,000 = 45%

'''

#Crea una funcion que acepte la cantidad y regrese el impuesto calculado
#Solo se permiten valores positivos mayores a 0

print("Dime la cantidad de dinero que ganas actualmente")

cant = int(input())
tax = float(0)
if cant>0:
    if cant < 10000:
        tax = 0.05
        print("Tu impuesto es del 5%") #Imprime el impuesto en cuestión
    elif cant >= 10000 and cant < 20000:
        tax = 0.15
        print("Tu impuesto es del 15%")
    elif cant >= 20000 and cant < 35000: 
        tax = 0.20
        print("Tu impuesto es del 20%")
    elif cant >= 35000 and cant < 60000:
        tax = 0.30
        print("Tu impuesto es del 30%")
    elif cant >= 60000:
        tax = 0.45  
        print("Tu impuesto es del 45%")
        
        

else:
     print("El valor introducido en menor a 0, o conteniene caracteres decimales")#Genera un error al mandar un valor invalido
    
imp_cal = cant * tax #se multiplica la cantidad por el impuesto

print("Tu impuesto calculado es de:", imp_cal)