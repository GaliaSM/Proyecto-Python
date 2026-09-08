# Se importa la función reduce de la libreria correspondiente
from functools import reduce
cadena="El mejor dia de mi vida"
# funcion que cuenta todos los carcteres dentro de la cadena incluyendo los espacios en blanco
funcion_contar=lambda contador, caracter: contador+1
# aplicamos reduce para que itere en la cadena comenzando en la posición 0
longitud=reduce(funcion_contar,cadena,0)
print("La longitud de la cadena es: ", longitud)