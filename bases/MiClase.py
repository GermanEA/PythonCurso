class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)


print(MiClase.variable_clase)

miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

miClase2 = MiClase('Otro valor variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'Valor variable clase 2'
print(miClase2.variable_clase2)

miClase2.variable_clase3 = 'Valor variable clase 3'
print(miClase2.variable_clase3)
# print(miClase.variable_clase3)  # No es posible crear una variable de clase con una instancia u objeto

MiClase.metodo_estatico()
miClase.metodo_estatico()

MiClase.metodo_clase()

miClase.metodo_instancia()