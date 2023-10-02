'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Modulo 3

Lab: 3.2.1.14
'''
blocks = int(input("Ingresa el número de bloques: "))

# Inicializa la altura de la pirámide y los bloques usados
height = 0
used_blocks = 0

# Usa un bucle while para construir la pirámide
while used_blocks + height + 1 <= blocks:
    height += 1
    used_blocks += height

print("La altura de la pirámide:", height)
