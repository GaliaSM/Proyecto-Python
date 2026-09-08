# se debe importar la funcion reduce de la libreria correspondiente
from functools import reduce
# funcion que concatena los numeros que van pasando de la lista de enteros
def lista_numeros(acumulador, numero):
  """
    Funcion que transforma los numeros de la lista a string y los concatena.

    Parámetros:
    acumulador(str): almacena la concatenación de los numeros de la lista
    numero (int): numero de la lista

    Retorna:
    acumulador (str): los numeros de la lista concatenados
    """
  # transforma a string los enteros y hace la concatenación
  acumulador=str(acumulador)+str(numero)
  return acumulador

# lista de digitos enteros
digitos=[4,3,2]
# usa la funcion reduce pasando por paramentros la lista de numeros y el valor actual del iterable
resultado=reduce(lista_numeros,digitos)
print(resultado)