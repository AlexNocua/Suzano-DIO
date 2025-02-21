# Comprensión del generador
# Las comprensiones de generadores también son muy similares a las listas, solo que utilizan corchetes curvos en lugar de cuadrados. También son más eficientes en memoria que las comprensiones de listas. Por ejemplo:

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")

# salida:
# <generator object <genexpr> at 0x102a87d60>
# <class 'generator'>
# 2 3 5 7 11 13 17 19 23 29 31

# En breve veremos la diferencia entre la función "map()" y las comprensiones de listas. Supongamos que sabemos que hay alguna función denominada "square()" que existe como se muestra a continuación:


def square(num):
    return num * 2


newdata = map(square, data)

newdata = [x + 3 for x in data]
