'''
Autor: Alexis Cano
Fecha 25 septiembre
Descripcion: Modulo 3

Lab: 3.2.1.3
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle! |
| Introduce un número entero      |
| y adivina qué número he         |
| elegido para ti.                |
| Entonces,                        |
| ¿Cuál es el número secreto?     |
+==================================+
""")

# Solicitar al usuario que ingrese un número entero
while True:
    user_number = int(input("Ingresa un número entero: "))
    
    # Comprobar si el número ingresado coincide con el número secreto
    if user_number == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
