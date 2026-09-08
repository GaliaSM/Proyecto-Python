def diferencia(num1,num2):
  """
    Realiza la diferencia entre dos numeros

    Parámetros:
    num1 (int): primer numero
    num2 (int): segundo numero

    Retorna:
    el resultado de la diferencia entre los dos numeros
  """
  return num1-num2

lista1=[10,20,30,40,50]
lista2=[1,2,3,4,5]
# Se aplica la función map para que itere con los numeros de cada lista y
# aplique la función diferencia
resultado=list(map(diferencia,lista1,lista2))
print(resultado)
