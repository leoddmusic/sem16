file=open('my_notes.txt', 'r')
# print(file)
lineas=file.readlines()
for l in lineas:
    print(l.replace('\n', ''))
# Cerrar el documento.
file.close()