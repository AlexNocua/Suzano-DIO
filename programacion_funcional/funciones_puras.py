##################################################
"""

Esta no es un funcion pura ya que se manipulan los datos globlaes como la lista.
una funcion pura no tiene por que afectar los valores externos o variables.

"""
mi_lista = [1, 2, 3, 4]


def añadir_valor_lista(valor):
    return mi_lista.append(valor)


añadir_valor_lista(54)
print(mi_lista)
##################################################
"""
Fucion pura sin alterar directamente el valor de la lista original
"""
mi_lista = [1, 2, 3, 4]
print(mi_lista)


def añadir_valor_lista(lista, valor):
    new_list = lista.copy()
    new_list.append(valor)
    return new_list


nueva_lista = añadir_valor_lista(mi_lista, 6)
print(nueva_lista)
