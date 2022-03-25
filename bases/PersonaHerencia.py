class Persona:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._edad}')

    def __str__(self):
        return f'{self.nombre} {self.edad}'