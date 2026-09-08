lista=[4,"maria",34,"a",65,"4"]
# funcion lambda que aplica la funcion isinstance para detectar solo los elementos de tipo entero
# se aplica filter para todos los elementos de la lista
numeros=list(filter(lambda x: isinstance(x,int),lista))
print(numeros)