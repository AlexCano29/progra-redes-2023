'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Modulo 3

Lab: 3.1.1.11
'''
year = int(input("Introduce un año:"))

if year < 1582:
    print("No dentro del período del calendario Gregoriano")
else:
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        print("Año Común")
    else:
        print("Año Bisiesto")
