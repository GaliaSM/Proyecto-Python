def compara(lista,palabra_objeto):
  """
    Realiza la comparacion de las palabras en la lista con
    la palabra objetivo

    Parámetros:
    lista (str): Lista de palabras
    palabra_objeto (str): Palabra objetivo

    Retorna:
    la lista con las palabras que coinciden con la palabra objetivo
    """
  nueva=[]
  # recorre la lista
  for elemento in lista:
    # compara cada palabra en la lista con la palabra objetivo y si coincide la
    # agrega a la lista nueva
    if elemento==palabra_objeto:
      nueva.append(elemento)
  return (nueva)

lista_palabras=["pedro", "carolina", "maria", "pedro", "carlospedro", "Pedro","maria"]
palabra_objetivo="maria"
objetivo=compara(lista_palabras,palabra_objetivo)
print(objetivo)

