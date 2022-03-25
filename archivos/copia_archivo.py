try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())
except Exception as e:
    print(e)
else:
    archivo.close()
    archivo2.close()