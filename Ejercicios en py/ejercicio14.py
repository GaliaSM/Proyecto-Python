# funcion para que solo tome las palabras que inician por la letra dada
def una_palabra(palabra):
  """
    Toma una palabra y compara si comienza por la letra dada.

    Parámetros:
    palabra(str): una palabra

    Retorna:
    palabra (str): la palabra si cumple con la condición, si no devuelve None
    """

  if palabra[0]==inicio:
    return palabra

lista=["maria", "pedro", "casa", "calcomania", "mama"]
inicio="m" #letra por la que quiero que inicie la palabra
# aplico la función con map pero devuelve las palabras encontradas y las que no comienzan por inicio devuelve None
resultado=list(map(una_palabra,lista))
# limpio el resultado con un filtro para que solo se vean las palabras encontradas
resultado=list(filter(lambda x: x is not None, resultado))
print(resultado)
