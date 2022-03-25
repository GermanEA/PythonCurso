# Para el cierre automático de archivos, se conoce como manejo de contexto with, es una sentencia simplificada
# Con with se llama el método __enter__ y al salir el método __exit__
# Esto nos evita tener que utilizar la claúsula finally en el try except
from archivos.ManejoArchivos import ManejoArchivos

# with open('prueba.txt', 'r', 'utf8') as archivo:

try:
    with ManejoArchivos('prueba.txt') as archivo:
        print(archivo.read())
except Exception as e:
    print(e)