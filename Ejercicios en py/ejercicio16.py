def consigue_palabra(palabra,n):
  """
    Toma una palabra y un numero que representa la longitud dada.

    Parámetros:
    palabra(str): una palabra
    n (int): longitud dada

    Retorna:
    palabra (str): la palabra si cumple con la condición, si no devuelve None
    """
  # consigue la longitud de la palabra para poder comparar con n
  longitud=len(palabra)
  if longitud>=n:
    return palabra
n=3
frase_cadena="Hola estamos aprendiendo python"
lista_palabras=frase_cadena.split()
# Crea una lista donde 'n' se repite para cada palabra en lista_palabras
n_list = [n] * len(lista_palabras)
# Usa map con dos iterables: lista_palabras y n_list
temp_resultado=list(map(consigue_palabra, lista_palabras, n_list))
# Filtra los valores None del resultado
resultado = list(filter(lambda x: x is not None, temp_resultado))
print(resultado)