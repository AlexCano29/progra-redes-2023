'''
Autor: Alexis Cano
Fecha 25 septiembre
Descripcion: Iniciando con Python

Lab:2.4.1.9
'''
millas = 7.38
kilometros = 12.25
factor_millas = 1.61
factor_km = 1 / factor_millas
conversion_millas = millas * factor_millas
conversion_kilometros = kilometros * factor_km
print(millas, "millas son", round(conversion_millas, 2), "kilómetros")
print(kilometros, "kilómetros son", round(conversion_kilometros, 2), "millas")
