lista1=[1,4,6,9,12]
lista2=[2,3,5,8,10]

# La función lambda suma dos números (elementos correspondientes de las listas)
suma_elementos = lambda x, y: x + y
# Luego, map aplica la lambda a cada par de elementos.
# Finalmente, convertimos el resultado de map a una lista.
resultado = list(map(suma_elementos, lista1, lista2))

print("La lista resultante de la suma de elementos es: ", resultado)