class Producto:
    contador_productos = 0

    @classmethod
    def _aumentar_contador(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre, precio):
        self._id_producto = self._aumentar_contador()
        self._nombre = nombre
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'[{self._id_producto}, {self._nombre}, {self._precio}]'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalón', 150.00)
    print(producto1)
    print(producto2)