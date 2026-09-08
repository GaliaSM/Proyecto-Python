frase = input("Ingrese una frase: ")
palabras = frase.split() # Divide la frase en una lista de palabras
# Usa map con la función len para obtener la longitud de cada palabra
longitudes = list(map(len, palabras))
print(longitudes)