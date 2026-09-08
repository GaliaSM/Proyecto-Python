# Programa para verificar que la edad esté entre 0 y 120
try:
  edad = int(input("Ingrese su edad: "))
  if edad < 0 or edad > 120:
    print("Edad incorrecta")
  else:
    print(f"Su edad es: {edad}")
except ValueError:
  print("Debe ingresar un número entero")