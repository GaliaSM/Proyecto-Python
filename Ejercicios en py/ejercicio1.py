def contar_frecuencia_caracteres(cadena_texto):
    """
    Calcula la frecuencia de cada carácter en una cadena de texto,
    ignorando los espacios en blanco.

    Parámetros:
    cadena_texto (str): La cadena de texto de entrada.

    Retorna:
    frecuencias: Un diccionario donde las claves son los caracteres y los valores
          son sus respectivas frecuencias.
    """
    frecuencias = {} # Inicializamos un diccionario vacío para almacenar las frecuencias


    # Iteramos sobre cada carácter de la cadena
    for caracter in cadena_texto:
        # comparación para verificar si no es un blanco
        if caracter != ' ':
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1

    return frecuencias



texto1 = "hola mundo"
print(f"Texto: '{texto1}'")
print(f"Frecuencias: {contar_frecuencia_caracteres(texto1)}")
# Salida esperada: {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
