class Persona:
    mi_atributo = 'Prueba'  # Atributo de clase

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  # Atributo de objeto o instancia
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self, intro):
        print(f'{intro} {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Germán', 'Estrade', 42)

print(persona1.nombre, persona1.apellido, persona1.edad)
print(persona1.mi_atributo)
print(Persona.mi_atributo)

persona1 = Persona('Nuevo', 'Nuevo', 21)
print(persona1.nombre, persona1.apellido, persona1.edad)

persona1.mostrar_detalle('Detalle:')
Persona.mostrar_detalle(persona1, 'Detalle2:')

# Agregar atributos a un objeto, pero no se compartirá con los otros objetos creados
persona1.telefono = '123456789'
print(persona1.telefono)