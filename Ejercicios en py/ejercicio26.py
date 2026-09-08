# Se piden los números al usuario
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
# funcion que calcula el resto
funcion_resto=lambda numero1, numero2: numero1%numero2
print("El resto de la division es: ", funcion_resto(numero1,numero2))
