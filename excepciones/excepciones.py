from personalizada import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))

    if a == b:
        raise NumerosIdenticosException('Exception idénticos')

    resultado = a / b
except ZeroDivisionError as e:
    print(f'Ocurrió un error: {e}, {type(e)}')
except TypeError as e:
    print(f'Error de tipos: {e}, {type(e)}')
except Exception as e:
    print(f'Error general: {e}, {type(e)}')
else:
    print('Solo se ejecuta cuando no se arroja ninguna excepción')
finally:
    print('Se ejecuta siempre haya o no una excepción')


print(f'Resultado: {resultado}')
print('Continuamos...')