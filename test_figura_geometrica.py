from HerenciaMultiple import Cuadrado, Rectangulo

cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcular_area())

# MRO - Method Resolution Order - Para saber el orden en que se ejecutan los métodos
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(15, 10, 'verde')
print(rectangulo1.calcular_area())
print(rectangulo1)
