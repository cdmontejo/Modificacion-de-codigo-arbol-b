from node import  NodoB
class ArbolB:
    def __init__(self, orden):
        self.orden = orden                     # Orden del árbol
        self.max_claves = orden - 1            # Máximo de claves por nodo
        self.min_claves = (orden // 2) - 1     # Mínimo de claves por nodo (no utilizado pero útil para validaciones)
        self.raiz = NodoB(orden)               # Inicialmente, raíz vacía

    def insertar(self, clave):
        nodo_raiz = self.raiz

        # Si la raíz está llena, se debe dividir
        if len(nodo_raiz.claves) == self.max_claves:
            nueva_raiz = NodoB(self.orden)
            nueva_raiz.hoja = False
            nueva_raiz.hijos.append(self.raiz)

            # Dividir la raíz
            self.dividir(nueva_raiz, 0)

            # Insertar en la nueva raíz
            self.insertar_en_nodo(nueva_raiz, clave)

            # Actualizar raíz
            self.raiz = nueva_raiz
        else:
            # Insertar directamente si la raíz no está llena
            self.insertar_en_nodo(nodo_raiz, clave)

    def insertar_en_nodo(self, nodo_actual, clave):
        # Si el nodo es hoja, insertar y ordenar
        if nodo_actual.hoja:
            nodo_actual.claves.append(clave)
            nodo_actual.claves.sort()
        else:
            # Buscar el hijo adecuado para insertar
            i = 0
            while i < len(nodo_actual.claves) and clave > nodo_actual.claves[i]:
                i += 1

            # Si el hijo está lleno, dividirlo antes de continuar
            if len(nodo_actual.hijos[i].claves) == self.max_claves:
                self.dividir(nodo_actual, i)

                # Recalcular la posición del hijo tras la división
                if clave > nodo_actual.claves[i]:
                    i += 1

            # Insertar recursivamente en el hijo adecuado
            self.insertar_en_nodo(nodo_actual.hijos[i], clave)

    def dividir(self, nodo_padre, i):
        orden = self.orden
        max_claves = self.max_claves
        nodo_hijo = nodo_padre.hijos[i]

        nuevo_nodo = NodoB(orden)
        nuevo_nodo.hoja = nodo_hijo.hoja

        # índice de la clave del medio
        medio = max_claves // 2

        # Clave que se subirá al padre
        clave_mitad = nodo_hijo.claves[medio]

        # Asignar claves al nuevo nodo (parte derecha)
        nuevo_nodo.claves = nodo_hijo.claves[medio + 1:]
        nodo_hijo.claves = nodo_hijo.claves[:medio]

        # Si no es hoja, también dividir los hijos
        if not nodo_hijo.hoja:
            nuevo_nodo.hijos = nodo_hijo.hijos[medio + 1:]
            nodo_hijo.hijos = nodo_hijo.hijos[:medio + 1]

        # Insertar clave del medio en el padre
        nodo_padre.claves.insert(i, clave_mitad)

        # Insertar el nuevo nodo como hijo del padre
        nodo_padre.hijos.insert(i + 1, nuevo_nodo)

    def mostrar(self, nodo_actual=None, nivel=0):
        if nodo_actual is None:
            nodo_actual = self.raiz
        print("  " * nivel + str(nodo_actual.claves))
        for hijo in nodo_actual.hijos:
            self.mostrar(hijo, nivel + 1)

    def buscar(self, clave, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        i = 0
        while i < len(nodo_actual.claves) and clave > nodo_actual.claves[i]:
            i += 1

        if i < len(nodo_actual.claves) and nodo_actual.claves[i] == clave:
            print(f"Clave {clave} encontrada en el nodo: {nodo_actual.claves}")
            return True

        if nodo_actual.hoja:
            print(f"Clave {clave} no encontrada.")
            return False

        return self.buscar(clave, nodo_actual.hijos[i])


# Ejemplo de uso:
arbol = ArbolB(orden=3)  # Árbol B de orden 3 (máx. 2 claves por nodo)

# Insertar varios valores
for valor in [50, 65, 78, 19, 10, 21, 55, 62, 28, 90, 82, 75]:
    print(f"\nInsertando {valor}:")
    arbol.insertar(valor)
    arbol.mostrar()
    print("-" * 30)

# Buscar claves
print("\n Buscando claves:")
arbol.buscar(50)  # Clave presente
arbol.buscar(15)  # Clave no presente
