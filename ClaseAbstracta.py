# ABC - Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Alto: {self._alto}, Ancho: {self._ancho}]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False


class Color:

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color [Color: {self._color}]'


class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):
        # super().__init__(lado)  No se utiliza porque puede generar confusión ya que tenemos dos padres
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

    def calcular_area(self):
        return self.alto * self.ancho


class Rectangulo(Color, FiguraGeometrica):

    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

    def calcular_area(self):
        return self.ancho * self.alto