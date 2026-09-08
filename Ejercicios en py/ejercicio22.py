# Se importa la función reduce de la libreria correspondiente
from functools import reduce
lista=[2,5,6,9,2,34,46]
# funcion lambda que va obteniendo el acumulado del producto por el numero
funcion_producto=lambda producto, numero: producto*numero
# Luego llamamos a la función_producto con la funcion reduce para que pueda iterar
# en la lista de numeros
resultado=reduce(funcion_producto,lista)
print("El resultado del producto de los numeros en la lista es: ", resultado)
