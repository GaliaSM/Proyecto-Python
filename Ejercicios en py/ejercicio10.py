def promedio(lista):
  """
    Calcula el promedio de una lista de números.

    Parámetros:
    lista(list): Lista de numeros.

    Retorna:
    media: La media de la lista.
    """
  # Incializa la variable donde se va a acumular
  suma=0
  try:
    longitud=len(lista)
  except longitud==0:
    print("La lista está vacía")
    return("La lista está vacia y no se puede dividir entre cero")
    # Se recorre la lista para realizar la suma de todos los numeros
  for i in range(len(lista)):
    suma=suma+lista[i]
  # se calcula el promedio
  media=suma/len(lista)
  return media

# Agregar numeros a la lista
lista=[]
respuesta="S"
# Se realiza un bucle para pedir al usuario los numeros e ir llenando la lista
while respuesta.upper()=="S":
  try:
    numero=int(input("Ingrese un numero: "))
  except ValueError:
    print("Debe ingresar un número")
  lista.append(numero)
  respuesta=input("¿Desea ingresar otro numero? (S/N): ")

print("El promedio de la lista es: ", promedio(lista))