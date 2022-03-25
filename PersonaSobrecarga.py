class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # obj1.__add__(obj2)
    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad


persona1 = Persona('Pedro', 26)
persona2 = Persona('Carlos', 20)
print(persona1 + persona2)
print(persona1 - persona2)