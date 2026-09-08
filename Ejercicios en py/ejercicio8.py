# Se maneja la excepcion de que el tipo de dato sea numerico
try:
  numerador=float(input("Ingrese el numerador: "))
  denominador=float(input("Ingrese el denominador: "))
except ValueError:
  print("Debe ingresar un número")
else:
 # Manejo de la división entre cero
  try:
    resultado=numerador/denominador
  except ZeroDivisionError:
    print("No se puede dividir por cero")

print(f"El resultado de la división es: {resultado:.2f}")