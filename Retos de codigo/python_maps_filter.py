menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]


def definir_cafes(cafe):
    if cafe[0] == "c":
        return cafe


# esta funcion mapea cada uno de los resltados de la busqueda con el fin de encontrar algo segun el determiando valor
# esta funcion pasa la funcion creada como argumento, con el fin de iterar la lista
mapp_coffe = map(definir_cafes, menu)
print(mapp_coffe)

for item in mapp_coffe:
    print(item)

# esto tambien se puede realizar con filter

filter_coffe = filter(definir_cafes, menu)
print(filter_coffe)
for item in filter_coffe:
    print(item)

"""
salida
<map object at 0x000001DC55240070>
None
None
None
cappuccino
cortado
None
<filter object at 0x000001DC552400D0>
cappuccino
cortado
"""