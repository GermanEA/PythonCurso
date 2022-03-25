try:
    # archivo = open('D:\\Program\\Cursos\\Python\\POO\\archivos\\prueba.txt', 'r', encoding='utf8')
    archivo = open('prueba.txt', 'r', encoding='utf8')
except Exception as e:
    print(e)
else:
    print(archivo.read(5))  # lee los 5 primeros caracteres y se queda el puntero en el siguiente
    print(archivo.readline())  # para leer una línea completa
    print(archivo.read())  # lee el archivo completo, el puntero se queda al final del archivo
finally:
    archivo.close()

try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
except Exception as e:
    print(e)
else:
    # iterar líneas de un archivo
    for linea in archivo:
        print(linea)
finally:
    archivo.close()

try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
except Exception as e:
    print(e)
else:
    # readlines() nos devuelve una lista cuyos elementos son las líneas del archivo
    print(archivo.readlines()[1])
    print(archivo.readlines())
finally:
    archivo.close()