from PersonaHerencia import Persona


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} {self.sueldo}'


empleado1 = Empleado('Germán', 42, 24000)
print(empleado1)