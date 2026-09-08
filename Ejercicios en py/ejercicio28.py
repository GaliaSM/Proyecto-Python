# función que busca en una lista el primer elemento duplicado
def duplicado(lista):
   """
    Busca el primer elemento que aparezca duplicado en la lista

    Parámetros:
    lista(list): Lista de elementos.

    Retorna:
     Mensaje si se encontraron duplicados o no. En el caso de encontrarlo devuelve el primer duplicado
     con su valor y posición correspondiente del elemento buscado y la posición del elemento duplicado
    """
  # Usamos una bandera para saber si encontramos al menos un duplicado
  encontrado_duplicado = False
  for i in range(len(lista)):
    for j in range(i+1, len(lista)):
      if lista[i] == lista[j]:
        print(f"El elemento {lista[i]} está duplicado y se encuentra en la posición {i} y {j}")
        encontrado_duplicado = True # Marcamos que se encontró un duplicado
        break # Salimos del bucle interno
    if encontrado_duplicado:
      break # Salimos del bucle externo

  # Si no se encontró ningún duplicado después de revisar toda la lista
  if not encontrado_duplicado:
    print("No se encontraron elementos duplicados.")

# --- Prueba de la función con una lista de ejemplo (fuera de la definición de la función) ---
# Si quieres probar con la lista original que tenías:
lista_ejemplo_con_duplicados = [42, 56, 42, 67]
print("\n--- Probando con lista que tiene duplicados ---")
duplicado(lista_ejemplo_con_duplicados)

lista_ejemplo_sin_duplicados = [10, 20, 30, 40]
print("\n--- Probando con lista sin duplicados ---")
duplicado(lista_ejemplo_sin_duplicados)
