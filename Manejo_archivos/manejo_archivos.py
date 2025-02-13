file = open("text.txt", mode="r")
print(file.read())

file.close()


# la funcion with cierra el archivo automaticamente y es mejor para el manejo de las excepciones
with open("text.txt", mode="r") as file:
    print(file.read())


# cree un archivo y escriba en el
with open("nuevo.txt", mode="w") as file:
    file.write("Hola mundo")  # para escribir en una sola linea
    # para escribir en varias lineas
    file.writelines(["Esta es una linea creada", "\nEsta es otra linea creada"])
