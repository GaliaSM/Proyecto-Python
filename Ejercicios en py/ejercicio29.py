# Función para convertir los caracteres de una cadena a # menos los ultimos cuatro
def enmascarar_cadena(variable):
  """
    Se enmascara los caracteres de una cadena a # menos los ultimos cuatro

    Parámetros:
    variable(str): cadena de texto.

    Retorna:
     La cadena de texto enmascarada con # exceptuando los ultimos cuatro caracteres
    """
  # Convertir la variable a una cadena de texto
  cadena = str(variable)

  # Si la cadena tiene 4 caracteres o menos, no enmascarar nada
  if len(cadena) <= 4:
    return cadena
  else:
    # Calcular cuántos caracteres deben ser enmascarados
    caracteres_a_enmascarar = len(cadena) - 4

    # Crear la parte enmascarada (con '#')
    parte_enmascarada = '#' * caracteres_a_enmascarar

    # Obtener los últimos cuatro caracteres
    ultimos_cuatro = cadena[-4:]

    # Unir la parte enmascarada con los últimos cuatro caracteres
    return parte_enmascarada + ultimos_cuatro

# --- Ejemplos de uso ---
print("Ejemplo 1 (cadena larga):", enmascarar_cadena("Hola estamos aprendiendo Python"))
print("Ejemplo 2 (número):", enmascarar_cadena(1234567890))
print("Ejemplo 3 (cadena corta):", enmascarar_cadena("Python"))
print("Ejemplo 4 (cadena muy corta):", enmascarar_cadena("abc"))
print("Ejemplo 5 (booleano):", enmascarar_cadena(True))