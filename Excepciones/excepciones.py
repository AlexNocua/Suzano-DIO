"""

IndexError
El siguiente código presenta un problema. Intenta localizar un elemento de la lista que no existe. Al ejecutar el código se generará IndexError. Agregue la gestión de excepciones para evitar que se produzca el error y se devuelva un mensaje más sencillo para el usuario, como "El elemento no existe en la lista".

    """

# Starter code
try:
    items = [1, 2, 3, 4, 5]
    item = items[6]
    print(item)
except IndexError as e:
    print("El elemento no existe en la lista")
    print(e)


"""

ZeroDivisionError
En matemáticas existen reglas sobre dividir por cero. El siguiente código intenta hacerlo y mostrará un ZeroDivisionError. Agregue la gestión de excepciones para devolver 0 en lugar de permitir que se produzca el error.
"""
try:
    # Starter code
    def divide_by(a, b):
        return a / b

except ZeroDivisionError as e:
    print("No es posible Dividir por cero")


ans = divide_by(40, 0)
print(ans)

"""
FileNotFoundError

El código siguiente busca un archivo que no existe. Agregue la gestión de excepciones para detectar este error y devolver el siguiente mensaje "No se pudo encontrar el archivo".

"""

try:
    # Starter code
    with open("file_does_not_exist.txt", "r") as file:
        print(file.read())

except FileNotFoundError as e:
    print("El archivo no existe")
