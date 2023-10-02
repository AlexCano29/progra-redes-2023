'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Modulo 3

Lab: 3.1.1.11
'''
income = float(input("Introduce el ingreso anual:"))

# Verifica si el ingreso es menor o igual a 85,528 pesos
if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

# Asegúrate de que el impuesto no sea negativo
tax = max(0, tax)

# Redondea el impuesto al número entero más cercano
tax = round(tax)

print("El impuesto es:", tax, "pesos")
