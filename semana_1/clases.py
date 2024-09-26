class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("No se puede colocar 0 como denominador")
        for num in range(1, min(numerador, denominador) + 1):
            if numerador % num == 0 and denominador % num == 0:
                numerador /= num
                denominador /= num
            self.numerador = int(numerador)
            self.denominador = int(denominador)
    
    def representar(self):
        if self.denominador != 1: #SI EL DENOMINADOR ES DIFERENTE DE 1
            return f"{self.numerador}/{self.denominador}" #ME RETORNA ESTO
        else: #SINO
            return self.numerador #ESTO

    def sumar(self, otra_fraccion):
        numerador = self.numerador * otra_fraccion.denominador + self.denominador * otra_fraccion.numerador
        denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(numerador=numerador, denominador=denominador)

    def restar(self, otra_fraccion):
        numerador = self.numerador * otra_fraccion.denominador - self.denominador * otra_fraccion.numerador
        denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(numerador=numerador, denominador=denominador)
    
    def convertir_a_float(self):
        return self.numerador / self.denominador
    
    def invertir(self):
        return Fraccion(self.denominador, self.numerador)
