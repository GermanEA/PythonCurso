class Aritmetica:
    """
    Documentación con DocString
    Clase Aritmética para realizar las operaciones de sumar, restar, etc...
    """

    def __init__(self, operando_a, operando_b):
        self.operando_a = operando_a
        self.operando_b = operando_b

    def sumar(self):
        return self.operando_a + self.operando_b

    def restar(self):
        return self.operando_a - self.operando_b

    def multiplicar(self):
        return self.operando_a * self.operando_b

    def dividir(self):
        return self.operando_a / self.operando_b


artimetica1 = Aritmetica(1, 3)
print(artimetica1.sumar())
print(artimetica1.restar())
print(artimetica1.multiplicar())
print(f'{artimetica1.dividir():.2f}')  # :.2f para mostrar solo dos decimales cuando usamos f''