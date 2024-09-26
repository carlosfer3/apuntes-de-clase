from clases import ColaDoblementeEnlazada

def prueba_dobleCola():
    cola1 = ColaDoblementeEnlazada()
    print(f"{cola1.esta_vacia()=}")
    print(f"{cola1.insertar_al_frente(1)}")
    print(f"{cola1.insertar_al_frente(4)}")
    print(f"{cola1.representar()=}")

if __name__ == "__main__":
    prueba_dobleCola()