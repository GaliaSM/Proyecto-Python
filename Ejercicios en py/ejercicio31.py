def ingresar(lista):
   """
    Función que solicita al usuario ingresar un nombre y lo agrega a la lista.
    El proceso se repite hasta que el usuario no quiera seguir.

    Parámetros:
    lista(list): Lista de nombres

    Retorna:
     la lista con los nombres ingresados
    """
   respuesta="S"
  # Para pedir varias veces un nombre hasta que el usuario no quiera seguir
   while respuesta.upper()=="S":
      nombre=input("Ingrese un nombre: ")
      lista.append(nombre)
      respuesta=input("¿Desea ingresar otro nombre? (S/N): ")
   return lista

def buscar_nombre(lista):
    """
    Función que solicita al usuario ingresar un nombre a buscar en la lista.
    Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado,
    de lo contrario, se lanza una excepción.
    Parámetros:
    lista(list): Lista de nombres

    Retorna:
     un mensaje indicando que el nombre fue encontrado o no
    """

    nombre_a_buscar=input("Ingrese el nombre que desea buscar: ")
    if nombre_a_buscar in lista:
      print(f"El nombre {nombre_a_buscar} se encuentra en la lista")
    else:
      # Si el nombre no está en la lista, se lanza una excepción
      raise ValueError(f"El nombre {nombre_a_buscar} no se encuentra en la lista")

lista_nombres=[]
lista_nombres=ingresar(lista_nombres)
try:
  buscar_nombre(lista_nombres)
except ValueError as e:
    print(e)
