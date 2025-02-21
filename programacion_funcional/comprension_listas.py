# La comprensión de listas en Python es una forma de crear una nueva secuencia a partir de una secuencia ya existente.

# Existen cuatro tipos principales de comprensiones en Python:

# Comprensión de la lista

# Comprensión del diccionario

# Establecer la comprensión

# Comprensión del generador


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Comprensión de la lista
# La sintaxis para la comprensión de listas es:

# [ <expression> for x in <sequence> if <condition>]
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x * 2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)

# El ejemplo dado proporciona diferentes formas en las que las comprensiones de lista se pueden utilizar para actualizar la lista o generar una nueva lista. Las comprensiones proporcionan una forma corta y elegante de actualizar secuencias. Como puede resultar evidente, el mismo código se puede escribir al utilizar el bucle "for" convencional y las condiciones "if else".

# Por ejemplo, en el caso del ejemplo 1:
# List comprehension:
data = [x+3 for x in data]

# Regular for loop:
for x in range(len(data)):
 data[x] = data[x] + 3
