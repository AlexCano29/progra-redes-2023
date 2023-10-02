'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Iniciando con Python

Lab:2.6.1.10
'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

# Calcula la cantidad de horas y minutos que sumar al tiempo de inicio
add_hours = duracion // 60
add_minutes = duracion % 60

# Calcula el tiempo final
final_hour = (hour + add_hours + (mins + add_minutes) // 60) % 24
final_minutes = (mins + add_minutes) % 60

# Muestra el resultado en formato de hora y minutos
print(f"El evento terminará a las {final_hour:02d}:{final_minutes:02d}")

