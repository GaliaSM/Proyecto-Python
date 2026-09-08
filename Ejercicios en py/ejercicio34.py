# Clase Arbol con atributos tronco, ramas
class Arbol:
    """
    Clase que representa a un arbol.
    """
    def __init__(self, tronco, ramas):
        """
        Constructor de la clase Arbol.
        Args:
            tronco (int): longitud del tronco.
            ramas (lista): lista de ramas.
        """
        # Creamos atributos y asignamos el valor de los parámetros del método constructor
        self.tronco = tronco
        self.ramas = ramas
    # 2. Método crecer_tronco para aumentar la longitud del tronco en una unidad.
    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en una unidad.
        """
        self.tronco += 1
    # 3. Método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    def nueva_rama(self):
        """
        Agrega una nueva rama de longitud 1 a la lista de ramas.
        """
        self.ramas.append(1)
    # 4.  Método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    def crecer_ramas(self):
        """
        Aumenta en una unidad la longitud de todas las ramas existentes.
        """
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    # 5. Método quitar_rama para eliminar una rama en una posición específica
    def quitar_rama(self, posicion):
        """
        Elimina una rama en una posición específica.
        Args:
            posicion (int): posición de la rama a eliminar.
        """
        if posicion >= 0 and posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print("Posición inválida")

    # 6. Método  info_arbol para devolver información sobre la longitud del tronco,
    # el número de ramas y las longitudes de las mismas.
    def info_arbol(self):
        """
        Devuelve información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
        Returns:
            str: información del árbol.
        """
        info = f"Longitud del tronco: {self.tronco}\n"
        info += f"Número de ramas: {len(self.ramas)}\n"
        info += "Longitudes de las ramas:\n"
        for rama in self.ramas:
            info += f"- {rama}\n"
        return info

# 1. Inicializar un arbol con logitud de tronco 1 y una lista de ramas vacia
tronco1=1
lista_ramas=[]
arbol1=Arbol(tronco1,lista_ramas)
# Llamado de cada metodo de la clase según el orden solicitado
arbol1.crecer_tronco()
arbol1.nueva_rama()
arbol1.crecer_ramas()
for i in range(3):
  arbol1.nueva_rama()
arbol1.quitar_rama(2)
print(arbol1.info_arbol())





