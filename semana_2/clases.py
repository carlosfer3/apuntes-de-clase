class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if self.tamanio() == 0:
            return None
        else:
            return self.elementos.pop()

    def cima(self):
        if self.tamanio() == 0:
            return None
        return self.elementos[-1]

    def tamanio(self):
        return len(self.elementos)
    
    def esta_vacia(self):
        if self.tamanio() == 0:
            return True
        return False



class Cola:
    def __init__(self):
        self.elementos = []
    
    def encolar(self, elemento):
        self.elementos.append(elemento)
    
    def desencolar(self):
        if self.tamanio() == 0:
            return None
        return self.elementos.pop(0)
    
    def tamanio(self):
        return len(self.elementos)
    
    def esta_vacia(self):
        if self.tamanio() == 0:
            return True
        return False
