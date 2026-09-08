def factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Parámetros:
    n (int): El número entero no negativo para el cual calcular el factorial.

    Retorna:
    int: El factorial del número n.
    """
    # factorial de n=0 o n=1 es 1 condicion de salida para la recursividad
    if n == 0:
        return 1
    else:
        # se vuelve a llamar recursivamente la función
        return n * factorial_recursivo(n-1)
n=1
# Se realiza un bucle para pedir los numeros al usuario y sacar su factorial
# hasta que se ingrese un numero negativo
while n>0:
  n=int(input("Ingrese un numero:(-1 para salir) "))
  if n<0:
    print("El numero debe ser positivo")
  else:
    factorial=factorial_recursivo(n)
    print(f"El factorial de {n} es: {factorial}")
