# metodo read
with open("archivo.txt", "r") as file:
    # leer un archivo general
    print(file.read())
    # leer los primeros 40 caracteres
    print(file.read(40))

# metodo readline
with open("archivo.txt", "r") as file:
    # lee la primera linea del archivo
    print(file.readline())
    # lee los primeros 10 caracteres del archivo
    print(file.readline(10))

# metodo readlines
with open("archivo.txt", "r") as file:
    # lee todas las lineas del archivo
    print(file.readlines())
    # lee las primeras 2 lineas del archivo
    print(file.readlines(2))