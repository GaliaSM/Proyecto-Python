#función que toma un caracter y lo lleve a minuscula y a mayuscula
def caracteres(caracter):
  """
    Transforma un caracter tanto a mayuscula como a minuscula.

    Parámetros:
    caracter (str): El caracter que se requiere transformar.

    Retorna:
    str: El caracter en mayuscula y en minuscula.
    """
  return (caracter.upper(),caracter.lower())

# conjunto de caracteres
conjunto={'a', 'b', 'C', 'd', 'A', 'e'}
# se aplica map con la funcion y el conjunto, pero a esa salida se le
# aplica set para que elimine los duplicados y finalmente se aplica tuple para
# que transforme el resultado a una tupla como se pide
resultado=tuple(set((map(caracteres,conjunto))))
print(resultado)
