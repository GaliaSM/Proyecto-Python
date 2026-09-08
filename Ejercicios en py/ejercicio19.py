lista_numeros=[1,2,3,4,5,6,7,8,9,10]
# funcion lambda para saber si los numeros en la lista son impares y se aplica filter
# para que aplique a los elementos de la lista de numeros
impares=list(filter(lambda x: x%2!=0,lista_numeros))
print(impares)