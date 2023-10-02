'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Modulo 3

Lab: 3.2.1.10
'''
# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra ingresada a mayúsculas
user_word = user_word.upper()

# Recorrer cada letra de la palabra
for letter in user_word:
    # Verificar si la letra es una vocal (A, E, I, O, U)
    if letter in "AEIOU":
        continue  
    else:
        print(letter)  
