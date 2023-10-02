'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Modulo 3

Lab: 3.4.1.6
'''
hat_list = [1, 2, 3, 4, 5]  # Lista de números ocultos en el sombrero.

# Paso 1: Reemplazar el número central en la lista con un número entero ingresado por el usuario.
hat_list[2] = int(input("Ingresa un número entero para reemplazar el número central: "))

# Paso 2: Eliminar el último elemento de la lista.
hat_list.pop()

# Paso 3: Imprimir la longitud de la lista existente.
print("Longitud de la lista:", len(hat_list))

print(hat_list)
