def mostrar_opciones():
  """
    Función que muestra un menú con las opciones disponibles.
    Parámetros:
    No recibe parámetros.
    Retorna:
     la opción seleccionada por el usuario
  """
  print("1. Contar palabras \n")
  print("2. Reemplazar palabras \n")
  print("3. Eliminar palabras \n")
  print("4. Salir \n")
  opcion=int(input("Ingrese una opcion: "))
  return opcion

def contar_palabras(texto):
  """
    Función que cuenta las palabras en un texto.
    Parámetros:
    texto(str): cadena de texto.
    Retorna:
     un diccionario con las palabras y su frecuencia
  """
  palabras=texto.split()
  dic_palabras={}
  for palabra in palabras:
    # Normalizar la palabra (quitar signos de puntuación y convertir a minúsculas)
    palabra_limpia = palabra.strip('.,;!?').lower()
    if palabra_limpia:
      if palabra_limpia in dic_palabras:
        dic_palabras[palabra_limpia]+=1
      else:
        dic_palabras[palabra_limpia]=1
  return dic_palabras

def reemplazar_palabras(texto,palabra_reemplazar,palabra_nueva):
  """
    Función que reemplaza una palabra en un texto por otra palabra dada.
    Parámetros:
    texto(str): cadena de texto.
    palabra_reemplazar(str): palabra a reemplazar.
    palabra_nueva(str): palabra nueva.
    Retorna:
     el texto con la palabra reemplazada
  """
  palabras=texto.split()
  for i in range(len(palabras)):
    # Comparar sin distinguir mayúsculas
    if palabras[i].lower()==palabra_reemplazar.lower():
      palabras[i]=palabra_nueva
  # Concatena las palabras separando con espacios en blanco
  texto_reemplazado=" ".join(palabras)
  return texto_reemplazado

def eliminar_palabras(texto,palabra_eliminar):
  """
    Función que elimina una palabra en un texto.
    Parámetros:
    texto(str): cadena de texto.
    palabra_eliminar(str): palabra a eliminar.
    Retorna:
     el texto sin la palabra
  """
  palabras=texto.split()
  # Usar una lista de comprensión para crear la nueva lista sin la palabra a eliminar (comparando sin distinguir mayúsculas)
  palabras_filtradas = [p for p in palabras if p.lower() != palabra_eliminar.lower()]
  texto_eliminado=" ".join(palabras_filtradas)
  return texto_eliminado

def procesar_texto(**kwargs):
  """
    Función que procesa un texto según la opción especificada.
    Parámetros:
    **kwargs(dict): diccionario con los parámetros variables según la opción
    seleccionada y la función a aplicar
    Retorna:
     el texto procesado
  """
  opcion=kwargs.get("opcion")
  texto=kwargs.get("texto")
  palabra=kwargs.get("palabra")
  palabra_reemplazar=kwargs.get("palabra_reemplazar")
  # Estructura de desición múltiple que evalua la opción y llama a la función correspondiente
  if opcion==1:
    dic_palabras=contar_palabras(texto)
    print (dic_palabras, '\n')
  elif opcion==2:
    reemplazo=reemplazar_palabras(texto,palabra, palabra_reemplazar)
    print(reemplazo, '\n')
  elif opcion==3:
    eliminar=eliminar_palabras(texto,palabra)
    print(eliminar, '\n')
  elif opcion==4:
    print("Gracias por usar el programa \n")
  else:
    print("Opcion no valida \n")

opcion=0
# Se repite la ejecución del programa hasta que el usuario desee salir
while opcion!=4:
  # Se muestran las opciones
  opcion=mostrar_opciones()
  # Se llama a procesar texto y se pasan los argumentos según lo que se requiere hacer
  if opcion==1:
    texto=input("Ingrese el texto: ")
    procesar_texto(opcion=opcion, texto=texto)
  elif opcion==2:
    texto=input("Ingrese el texto: ")
    palabra=input("Ingrese la palabra a reemplazar: ")
    palabra_nueva=input("Ingrese la nueva palabra: ")
    procesar_texto(opcion=opcion, texto=texto, palabra=palabra, palabra_reemplazar=palabra_nueva)
  elif opcion==3:
    texto=input("Ingrese el texto: ")
    palabra=input("Ingrese la palabra a eliminar: ")
    procesar_texto(opcion=opcion, texto=texto, palabra=palabra)
  elif opcion==4:
    procesar_texto(opcion=opcion)
    break
    print("Opcion no valida \n")