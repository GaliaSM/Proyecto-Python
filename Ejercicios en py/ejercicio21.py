# Se pide el numero que deseo calcular su cubo
numero=int(input("Ingrese un numero: "))
# Se define la función con lambda
funcion_cubo=lambda numero: numero**3
# Se llama a la funcion y su resultado de guarda en la variable cubo
cubo=funcion_cubo(numero)
print("El cubo del número es: ", cubo)