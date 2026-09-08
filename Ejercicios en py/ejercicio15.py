lista=[1,2,3,4,5,6,7,8,9,10]
# funcion lambda para agregar 3 a cada numero
suma=(lambda x: x+3)
# se aplica map para aplicar la funcion lambda a la lista
resultado=list(map(suma,lista))
print(resultado)
