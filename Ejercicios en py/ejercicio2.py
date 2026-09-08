#funcion donde se calcula el doble del número
def doble_valor(numero):
  """
    Calcula el doble del vaor de un numero

    Parámetros:
    numero (int): El numero al que se le calcula su doble.

    Retorna:
    el resultado del doble del numero
    """
  return 2*numero

lista=[3,10,6,12,9]
# se aplica map para que devuelva el doble de cada numero en la lista
nueva=list(map(doble_valor,lista))
print(nueva)
