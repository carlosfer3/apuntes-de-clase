class Vector:
    
    def __init__(self):
        self.elementos = []

    def insert(self, posicion, elemento):
        if self.tamanio() != 0:
            aux = self.elementos[posicion]
            self.elementos[posicion] = elemento
            self.elementos.append(aux)
        else:
            pass

