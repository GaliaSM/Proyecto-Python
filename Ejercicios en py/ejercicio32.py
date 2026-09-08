# Función para buscar el nombre en una lista dada
def buscar_nombre(lista):
  """
    Función para buscar un nombre en una lista dada
    Parámetros:
    lista(list): Lista de nombres

    Retorna:
     un mensaje indicando que el nombre fue encontrado o no
    """
  encontrado=False
  nombre_a_buscar=input("Ingrese el nombre que desea buscar: ")
  # Recorre la lista y compara el nonbre a buscar con cada elemento de la lista
  for i in range(len(lista)):
    if nombre_a_buscar == lista[i]:
      print(f"El nombre {nombre_a_buscar} se encuentra en la lista en la posición {i}")
      encontrado=True
      break
  if encontrado==False:
    print(f"El nombre {nombre_a_buscar} no se encuentra en la lista")

lista_empleados=["Maria","Juan","Pedro"]
buscar_nombre(lista_empleados)