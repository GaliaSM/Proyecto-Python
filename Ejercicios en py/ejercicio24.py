# Se importa la función reduce de la libreria correspondiente
from functools import reduce
lista=[2,5,6,9,2,34,46]
# definición de la función lambda para calcular la diferenca
funcion_diferencia=lambda diferencia, numero: diferencia-numero
#Luego llamamos a la función con la funcion reduce para que pueda iterar en la lista
resultado=reduce(funcion_diferencia,lista)
print("El resultado de la diferencia de los numeros en la lista es: ", resultado)