# definición de la función promedio para calcular la media
def promedio(lista):
  """
    Calcula el promedio de una lista de números.

    Parámetros:
    lista(list): Lista de numeros.

    Retorna:
    media: La media de la lista.
    """
  # Incializa la variable donde se va a acumular
  suma=0
  # Se recorre la lista para realizar la suma de todos los numeros
  for i in range(len(lista)):
    suma=suma+lista[i]
  # se calcula la media
  media=suma/len(lista)
  return media


# Lista de numeros
lista=[45,62,34,41,53]
print("El promedio de la lista es: ", promedio(lista))