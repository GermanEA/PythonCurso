class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo


# baseUsuario = input('Proporciona la base: ')
# alturaUsuario = input('Proporciona la altura: ')
# rectanguloUsuario = Rectangulo(int(baseUsuario), int(alturaUsuario))
# print(f'El área es: {rectanguloUsuario.calcular_area()}')

anchoUsuario = input('Proporciona el ancho: ')
altoUsuario = input('Proporciona el alto: ')
profundoUsuario = input('Proporciona la profundidad: ')
cuboUsuario = Cubo(int(anchoUsuario), int(altoUsuario), int(profundoUsuario))
print(f'El área es: {cuboUsuario.calcular_volumen()}')