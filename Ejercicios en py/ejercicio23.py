# Se importa la función reduce de la libreria correspondiente
from functools import reduce

palabras=["hola", "mundo", "de", "Python"]
# definición de la función lambda para concatenar las palabras de una lista
funcion_concatenar=lambda acumulador, palabra: acumulador+" "+palabra
#Luego llamamos a la función con la funcion reduce para que pueda iterar en la lista
resultado=reduce(funcion_concatenar,palabras)
print("El resultado de concatenar las palabras es: ", resultado)