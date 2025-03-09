class Noteboocks ():
    def __init__(self, resolucion, tipo_teclado):
        self.resolucion = resolucion
        self.tipo_teclado = tipo_teclado
    def encender(self):
        print("Encendiendo")

    def apagar(self):
        print("Apagando")

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio}"
    
class ComputadorasAsus (Noteboocks):
    def __init__(self, resolucion, tipo_teclado):
        super().__init__(resolucion, tipo_teclado)
    
    def referencia (self):
        print("Referencia: 1234")
        
Alex = ComputadorasAsus("1920x1080", "mecanico")
print(Alex.resolucion)
print(Alex.referencia())