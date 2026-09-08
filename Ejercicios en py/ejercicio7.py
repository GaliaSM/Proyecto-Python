#funcion para convertir un elemento en cadena de caracteres
def conversor(t):
  """
    Convierte un elemento a string.

    Parámetros:
    t (cualquier tipo): El elemento que se requiere convertir a string.

    Retorna:
    str: El elemento convertido en string.
    """
  return(str(t))

# se inicializa la lista y la tupla con diferentes tipos de datos
lista=[]
tupla=[(1,2,3,4,5),(True,False),("Maria","Petra")]
# se llama a la funcion desde map para que la aplique a todos los elementos de la tupla
resultado=list(map(conversor,tupla))
print(resultado)
