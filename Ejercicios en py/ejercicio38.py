# Define si es de mañana, tarde o noche.
def dianoche(horas):
  """
    Función que determina si es de mañana, tarde o noche según la hora proporcionada
  """
  if horas >= 6 and horas < 12:
      print("Es de mañana")
  elif horas >= 12 and horas < 18:
    print("Es de tarde")
  else:
    print("Es de noche")

# Se pide la hora al usuario
hora = input("Ingrese la hora (hh:mm): ")
try:
  # 2. Separar el texto por los dos puntos
    partes = hora.split(":")

    # 3. Convertir cada parte a un número entero
    horas = int(partes[0])
    minutos = int(partes[1])

    # 4. Validar que sea una hora real en formato de 24 horas
    if 0 <= horas < 24 and 0 <= minutos < 60:
        print(f"Hora ingresada correctamente: {horas:02d}:{minutos:02d}")
        dianoche(horas)
    else:
        print("Error: Las horas deben estar entre 0-23 y los minutos entre 0-59.")
except ValueError:
    print("Error: El formato de la hora no es válido.")