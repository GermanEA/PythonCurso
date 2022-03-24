class FiguraGeometrica:

    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @alto.setter
    def alto(self, alto):
        self._alto = alto


class Color:

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):
        # super().__init__(lado)  No se utiliza porque puede generar confusión ya que tenemos dos padres
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho