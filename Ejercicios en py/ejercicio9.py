# función que filtra las mascotas prohibidas, se uso una función lambda para aplicarla como filtro a la lista
# y se usa filter para aplicar el filtro a la variable iterativa
def filtrar_mascotas(lista_mascotas):
  """
    Filtra una lista de mascotas comparando con la lista de mascotas prohibidas.

    Parámetros:
    lista_mascotas (list): Lista de mascotas

    Retorna:
    lista: lista de mascotas filtradas.
    """
  mascotas_prohibidas=["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
  mascotas_filtradas=list(filter(lambda x: x not in mascotas_prohibidas, lista_mascotas))
  return mascotas_filtradas

mascotas=["Perro", "Gato","Mapache", "Vaca","Tigre", "Loro","Guacamaya","Serpiente Pitón", "Cocodrilo", "Oso"]
mascotas_filtradas=filtrar_mascotas(mascotas)
print(mascotas_filtradas)