class PersonaEncapsulamiento:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre  # Atributo al que no se debe acceder en código en producción
        self.__apellido = apellido  # Atributo que no se puede modificar
        self._edad = edad

    # Decorador @property para que no se pueda acceder al atributo de _, ya no hay que llamar este método como función
    # sino como un atributo
    # Métodos getter
    @property
    def nombre(self):
        print('LLamando método get nombre')
        return self._nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def edad(self):
        return self._edad

    # Métodos setter
    @nombre.setter
    def nombre(self, nombre):
        print('LLamando método set nombre')
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self, intro):
        print(f'{intro} {self._nombre} {self.__apellido} {self.edad}')


persona1 = PersonaEncapsulamiento('Germán', 'Estrade', 42)
persona1._nombre = 'Pepe'  # Se debe evitar es mala práctica
persona1.__apellido = 'Díaz'  # Se debe evitar es mala práctica, no se refleja la modificación porque no se produce
persona1.mostrar_detalle('Detalle:')
print(persona1.nombre)

persona1.nombre = 'Manolo'
print(persona1.nombre)

persona1.apellido = 'Lara'
persona1.edad = 24
persona1.mostrar_detalle('Info:')