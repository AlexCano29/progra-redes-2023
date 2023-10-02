'''
Autor: Alexis Cano
Fecha 2 de Octubre
Descripcion: Problema 2

Ejercicio: u2_prob1
'''

'''
-Programa que almacene las asignaturas del estudiante de IRD durante cuarto cuatrimestre
(Probabilidad, Electronica, Conexion de Redes, Servidores, Programacion de Redes, Formacion, Ingles)
-Pregunte que nota saco de calificacion en la unidad 1 de cada una
-Muestre el mensaje en asignatura sacaste "" y la nota
'''
 
 # Lista de asignaturas
asignaturas = [
    "Probabilidad y Estadistica",
    "Electronica para IDC",
    "Conexion de Redes WAN",
    "Administración de Servidores",
    "Programacion de Redes",
    "Formacion Sociocultural",
    "Ingles"
]

# Almacenar las notas
notas = {}

# Preguntar por la calificación de la unidad 1 de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota sacaste en la unidad 1 de {asignatura}? "))
    notas[asignatura] = nota

# Mostrar las notas
for asignatura, nota in notas.items():
    print(f"En {asignatura} sacaste {nota} de calificación.")

 
 
