from clases import Pila
from clases import Cola

def prueba_pila():
    pila1 = Pila()
    print(f"{pila1.esta_vacia()=}")
    for num in range (10):
        pila1.apilar(num)
    print(f"{pila1.desapilar()=}")
    print(f"{pila1.cima()=}")
    print(f"{pila1.tamanio()=}")

    pila2 = Pila()
    for letra in "AMOR":
        pila2.apilar(letra)
    while pila2.tamanio() != 0:
        print(f"{pila2.desapilar()=}")
    
    pila3 = Pila()
    expresion = "(1+3) - 4*5*(1-3) + (6"
    print(expresion)
    for caracter in expresion:
        if caracter == "(":
            pila3.apilar(caracter)
        elif caracter == ")":
            pila3.desapilar()
    if pila3.tamanio() == 0:
        print("todos los paréntesis son correctos")
    else:
        print("Los paréntesis son incorrectos")

    pila4 = Pila()
    expresion = "(1+3) - 4*5*(1-3) + 6^(1/2)"
    print(expresion)
    for caracter in expresion:
        if caracter == "(":
            pila4.apilar(caracter)
        elif caracter == ")":
            pila4.desapilar()
    if pila4.tamanio() == 0:
        print("todos los paréntesis son correctos")
    else:
        print("Los paréntesis son incorrectos")

def prueba_cola():
    cola1 = Cola()
    for numero in range(10):
        cola1.encolar(numero)
    print(f"{cola1.desencolar()=}")
    print(f"{cola1.tamanio()=}")
    print(f"{cola1.esta_vacia()=}")

    cola2 = Cola()
    #PROBLEMA DE FLAVIO JOSEFO
    for numero in range(1, 42):
        cola2.encolar(numero)
    iterador = 1
    print(cola2.elementos)
    while cola2.tamanio() != 2:
        elemento = cola2.desencolar()
        if iterador % 3 != 0:
            cola2.encolar(elemento)
        if cola2.tamanio() == 2:
            print(f"El soldado numero {elemento} se suicido")
        iterador += 1
    print(f"{cola2.elementos=}")
    print(f"{cola2.tamanio()=}")
    

if __name__ == "__main__":
    prueba_cola()