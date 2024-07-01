import ephem
from datetime import datetime, timedelta

# Define la ubicación
pelayos = ephem.Observer()
pelayos.lat = '40.3616'  # latitud de Pelayos de la Presa
pelayos.lon = '-4.3669'  # longitud de Pelayos de la Presa

# Crea objetos para el sol y la luna
sol = ephem.Sun()
luna = ephem.Moon()

# Calcula la próxima salida y puesta del sol
proxima_salida_del_sol = pelayos.next_rising(sol)
proxima_puesta_del_sol = pelayos.next_setting(sol)

# Calcula la próxima salida y puesta de la luna
proxima_salida_de_la_luna = pelayos.next_rising(luna)
proxima_puesta_de_la_luna = pelayos.next_setting(luna)

# Convierte a la zona horaria local (España/Europa)
def convertir_a_hora_local(hora_utc):
    hora_local = hora_utc.datetime() + timedelta(hours=2)  # Ajusta según tu zona horaria
    return hora_local

# Imprime los resultados
print(f'Próxima salida del sol: {convertir_a_hora_local(proxima_salida_del_sol)}')
print(f'Próxima puesta del sol: {convertir_a_hora_local(proxima_puesta_del_sol)}')
print(f'Próxima salida de la luna: {convertir_a_hora_local(proxima_salida_de_la_luna)}')
print(f'Próxima puesta de la luna: {convertir_a_hora_local(proxima_puesta_de_la_luna)}')
