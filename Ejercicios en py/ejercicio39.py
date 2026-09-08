# Programa que lleva la calificación numerica a una textual según las reglas proporcionadas
respuesta='S'
# Se repite hasta que el usuario desee salir
while respuesta.upper()=='S':
  # Validación de la entrada numerica en punto flotante
  while True:
    try:
      nota=float(input("Ingrese la nota del alumno: "))
      break
    except ValueError:
      print("Error: La nota debe ser un número punto flotante separado por punto")
      continue
  # Aplicamos las reglas proporcionadas para llevar la nota a texto
  if nota>0 and nota<=69:
    print("Insuficiente")
  elif nota>=70 and nota<=79:
    print("Bien")
  elif nota>=80 and nota<=89:
    print("Muy bien")
  elif nota>=90 and nota<=100:
    print("Excelente")
  else:
    print("Nota invalida")
  respuesta=input("¿Desea ingresar otra nota? (S/N):")

