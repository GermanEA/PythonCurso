# Un operador puede funcionar de maneras distintas, por ejemplo el operador +
# operador +
a = 2
b = 3
print(a + b)

a = 'Hola '
b = 'Mundo'
print(a + b)

a = [1, 2, 3]
b = [6, 7, 8]
print(a + b)

# Se pueden sobrecargar los operadores relacionados con clases, sobreescribiendo los siguientos métodos:
# +   __add__(self, other)
# -   __sub__(self, other)
# *   __mul__(self, other)
# /   __truediv__(self, other)
# //  __floordiv__(self, other)
# %   __mod__(self, other)
# **  __pow__(self, other)