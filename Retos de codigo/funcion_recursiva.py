# una funcion recursiva consiste en brindar una solucion alterna al retorno iterativo de una funcion ejemplificando un bucle.
# un ejemplo con el calculo de un factorial


# esta es una solucion en base a un logica
def calcular_factorial(num):
    factorial = 1
    for n in range(num):
        factorial *= n + 1
    return factorial


print(calcular_factorial(0))

# Funcion recursiva con el llamado de la funcion en la misma funcion
def recursiva_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursiva_factorial(num - 1)


print(recursiva_factorial(5))
