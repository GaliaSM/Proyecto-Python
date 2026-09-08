def crear_diccionario():
  """
    Crea un diccionario con los datos de estudiante: nombre, edad, calificación.
    Estos datos se ingresan por teclado para tantos estudiantes como se deseen.

    Parámetros:
    No son necesarios

    Retorna:
    la lista de los estudiantes nuevos, compuesta por diccionarios
    """
  respuesta="S"
  estudiantes_nuevos = [] # Lista para guardar los diccionarios de estudiantes
  while respuesta.upper()=="S":
    estudiante_actual = {} # Crear un nuevo diccionario para cada estudiante
    estudiante_actual["nombre"] = input("Ingrese el nombre del estudiante: ")
    # Convertir la edad y la calificación a int
    estudiante_actual["edad"] = int(input("Ingrese la edad del estudiante: "))
    estudiante_actual["calificacion"] = int(input("Ingrese la calificacion del estudiante: "))
    estudiantes_nuevos.append(estudiante_actual)
    respuesta=input("¿Desea agregar otro estudiante? (S/N): ")
  return estudiantes_nuevos # Devolver la lista de diccionarios de estudiantes

def califica(estudiante):
  """
    Toma la calificacion del estudiante y compara si es mayor o igual a 90.

    Parámetros:
    estudiante (dict): diccionario con los datos del estudiante

    Retorna:
    estudiante["calificacion"] (int): la calificacion del estudiante,
    si cumple con la condición, si no devuelve False
    """
  return estudiante["calificacion"]>=90

# Asignar la lista de estudiantes devuelta por la función
lista_de_estudiantes = crear_diccionario()

# Usar filter() para extraer a los estudiantes con calificación >= 90
calificacion_alta = list(filter(califica, lista_de_estudiantes))
if (calificacion_alta!=[]):
    print("Estudiantes con calificación mayor o igual a 90:")
    for estudiante in calificacion_alta:
        print(estudiante)
else:
    print("No hay estudiantes con calificaciones mayor a 90")