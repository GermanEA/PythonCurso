# Para abrir un archivo, si no existe se crea de manera automática
# 'r' read
# 'a' append, crea el fichero si no existe
# 'w' writing, crea el fichero si no existe y sobreescribe su contenido
# 'w+' para escribir pero también para leer
# 'r+' para leer pero también para escribir
# 'x' create, crea el archivo si no existe
# 't' Text, para que el archivo sea solo texto
# 'b' Binary, para que el archivo sea en modo binario (imagenes, pdf, video, musica)
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adiós')
except Exception as e:
    print(e)
finally:
    archivo.close()