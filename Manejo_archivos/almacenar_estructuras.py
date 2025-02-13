import random


with open("nombres.txt", "r") as archivo:

    lista_nombres = archivo.read()
    nombres = lista_nombres.split("\n")
    print(nombres)
    nombre = random.choice(nombres)
    print(nombre)
