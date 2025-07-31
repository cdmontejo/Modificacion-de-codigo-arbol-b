class NodoB:
    def __init__(self, orden):
        self.orden = orden              # Orden del árbol (grado máximo de hijos)
        self.claves = []               # Lista de claves en el nodo
        self.hijos = []                # Lista de hijos
        self.hoja = True               # Se inicializa como hoja
