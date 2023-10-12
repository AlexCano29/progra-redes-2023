'''
Autor: Julian Alexis Cano Cruces
Fecha: 10/10/2023
Descripcion: Laboratorio 4.3.1.6
'''
def is_year_leap(year):
    # Comprobamos si el año es divisible por 4 y no divisible por 100, o si es divisible por 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

#Probamos datos
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")



