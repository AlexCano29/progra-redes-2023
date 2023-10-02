'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Modulo 3

Lab: 3.6.1.9
'''
# Lista original con repeticiones
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Lista para almacenar elementos únicos
unique_list = []

# Iterar sobre la lista original
for num in original_list:
    # Verificar si el elemento no está en la lista de elementos únicos
    if num not in unique_list:
        unique_list.append(num)

# La lista unique_list ahora contiene elementos únicos
print("Lista original:", original_list)
print("Lista sin repeticiones:", unique_list)
