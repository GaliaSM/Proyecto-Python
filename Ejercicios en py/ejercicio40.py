def calculoareas(figura, parametros):
  """
    Función que calcula el área de un figura geometrica
    Parámetros:
    figura(str): cadena que indica la figura a calcular.
    parametros(tuple): tupla con los datos necesarios para calcular el área de la figura.
    Retorna:
     el área de la figura
  """
  if figura=="circulo":
    r=parametros[0]
    area=PI*r**2
  elif figura=="rectangulo":
    a=parametros[0]
    b=parametros[1]
    area=a*b
  else:
    a=parametros[0]
    b=parametros[1]
    area=(a*b)/2
  return (area)

figura=input("Ingrese la figura (circulo, rectangulo o triangulo): ")
figura=figura.lower()
PI=3.141592653589793
if figura=="circulo":
  radio=float(input("Ingrese el radio del circulo:      "))
  parametros=(radio)
elif figura=="rectangulo":
  base=float(input("Ingrese la base del rectangulo: "))
  altura=float(input("Ingrese la altura del rectangulo: "))
  parametros=(base,altura)
else:
  base=float(input("Ingrese la base del triangulo: "))
  altura=float(input("Ingrese la altura del triangulo: "))
  parametros=(base,altura)

area=calculoareas(figura,parametros)
print("El area de la figura es: ", area)