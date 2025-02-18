def invertir_cadena(cadena):
    return cadena[::-1]


print(invertir_cadena("alex"))


# Recursion
def recursion_str(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return recursion_str(cadena[1:]) + cadena[0]


print(recursion_str("Alex"))
