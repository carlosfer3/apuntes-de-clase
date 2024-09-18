from clases import Fraccion

if __name__ == "__main__":
    mi_fraccion = Fraccion(2,8)
    print(f"{mi_fraccion.representar()=}")

    fraccion_suma = mi_fraccion.sumar(Fraccion(2,8))
    print(f"{fraccion_suma.representar()=}")
    print(f"{mi_fraccion.convertir_a_float()=}")
    fraccion_invertida = mi_fraccion.invertir()
    print(f"{fraccion_invertida.representar()=}")
    otra_fraccion = Fraccion(5, 1)
    print(f"{otra_fraccion.representar()=}")
    