class Sumador:
    def sumar(self, a, b):
        return a + b

class Calculador(Sumador):
    def restar(self, a, b):
        return a-b

    def multiplicar(self, a, b):
            return a*b

    def dividir(self, a, b):
            return a/b

miCalculadora= Calculador()



