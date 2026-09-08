# función para determinar si dos palabras son anagramas
def anagrama(palabra1, palabra2):
   """
    Determina si dos palabras son anagramas

    Parámetros:
    palabra1 (str): cadena de texto.
    palabra2 (str): cadena de texto.

    Retorna:
     Mensaje si las palabras son anagramas o no
    """
   longitud_palabra1=len(palabra1)
   longitud_palabra2=len(palabra2)
   if longitud_palabra1!=longitud_palabra2:
    return False
   else:
    palabra1=palabra1.lower()
    palabra2=palabra2.lower()
    palabra1=sorted(palabra1)
    palabra2=sorted(palabra2)
   if palabra1==palabra2:
    return True
   else:
    return False

palabra1="Amor"
palabra2="Roma"
resultado=anagrama(palabra1,palabra2)
if resultado==False:
  print("Las palabras no son anagramas")
else:
  print("Las palabras son anagramas")