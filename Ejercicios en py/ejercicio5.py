def media(lista,nota_aprobado=5):
  """
    Calcula la media de una lista de numeros y si es mayor o igual que la nota
    aprobada devuelve aprobado, de lo contrario suspenso

    Parámetros:
    lista (list): Lista de numeros reales
    nota_aprobado (float): Nota aprobada por defecto es 5

    Retorna:
    Tupla con la media y el estado
    """
  # en python se puede aplicar la funcion sum para que sume todos los elementos
  # de la lista y se divide entre la cantidad de elementos que obtenemos con
  # la función len
  media=sum(lista)/len(lista)
  # Se aplica la estructura de desición para saber el estado
  if media>=nota_aprobado:
    estado="aprobado"
  else:
    estado="suspenso"
  return (media,estado)

lista=[4.5,8.76,3.90,4.05,5.60,4.50,9.87,8,85]
tupla=media(lista)
print("La media es: ", tupla[0])
print("El estado es: ", tupla[1])