# Programa que calcula el descuento y muestra el precio final con descuento
precio=float(input("Ingrese el precio del producto: "))
respuesta=input("¿Tiene un cupon de descuento? (Si/No): ")
if respuesta.lower()=="si":
  descuento=float(input("Ingrese el porcentaje de descuento: "))
  if descuento>0:
    precio_final=precio*(1-descuento/100)
else:
  precio_final=precio
print("El precio final del producto es: ", precio_final)