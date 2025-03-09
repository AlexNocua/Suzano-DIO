class Operaciones:
    def suma(self, a, b):
        return a +b 
    def resta   (self, a, b):
        return a - b
    def multiplicacion(self, a, b):
        return a * b
    def division(self, a, b):
        return a / b
    
operaciones = Operaciones()
print(operaciones.suma(5, 3))  # Salida: 8
print(operaciones.resta(5, 3))  # Salida: 8
print(operaciones.multiplicacion(5, 3))  # Salida: 8
print(operaciones.division(5, 3))  # Salida: 8