class ColaDoblementeEnlazada:

    def __init__(self):
        self.elementos = []

    def representar(self):
        return '(' + ','.join(str(elemento) for elemento in self.elementos) + ')'

    def tamanio(self):
        return len(self.elementos)

    def esta_vacia(self):
        return self.tamanio() == 0

    def insertar_al_frente(self, elemento):
        self.elementos.insert(0, elemento)

    def insertar_al_final(self, elemento):
        self.elementos.append(elemento)

    def remover_de_frente(self):
        if self.tamanio() == 0:
            return None
        return self.elementos.pop(0)

    def remover_al_final(self):
        if self.tamanio() == 0:
            return None
        return self.elementos.pop

