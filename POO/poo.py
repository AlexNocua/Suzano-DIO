# 1. Polimorfismo
# El polimorfismo permite que una misma operación se comporte de manera diferente según el tipo de dato.
def mostrar_longitud(dato):
    print(f"La longitud de {dato} es: {len(dato)}")

# Ejemplos de polimorfismo con la función `mostrar_longitud`
mostrar_longitud("Hola")       # Cadena de texto
mostrar_longitud([1, 2, 3])   # Lista
mostrar_longitud((1, 2, 3))   # Tupla
# Salida:
# La longitud de Hola es: 4
# La longitud de [1, 2, 3] es: 3
# La longitud de (1, 2, 3) es: 3


# 2. Encapsulamiento
# El encapsulamiento protege los datos de un objeto, controlando el acceso a ellos.
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado (no accesible directamente desde fuera)

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo  # Método público para acceder al saldo

# Ejemplo de encapsulamiento
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print(f"Saldo actual: {cuenta.obtener_saldo()}")  # Salida: Saldo actual: 1500
# print(cuenta.__saldo)  # Esto daría un error, ya que __saldo es privado


# 3. Herencia
# La herencia permite crear una nueva clase basada en una clase existente.
class Animal:  # Clase base
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):  # Clase derivada
    def hacer_sonido(self):
        print("El perro ladra")  # Sobrescribe el método de la clase base

# Ejemplo de herencia
mi_perro = Perro()
mi_perro.hacer_sonido()  # Salida: El perro ladra


# 4. Abstracción
# La abstracción oculta los detalles complejos y muestra solo la funcionalidad esencial.
from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass  # Método abstracto que debe ser implementado por las subclases

class Circulo(Figura):  # Clase concreta
    def __init__(self, radio):
        self.radio = radio

    def area(self):  # Implementación del método abstracto
        return 3.1416 * (self.radio ** 2)

# Ejemplo de abstracción
mi_circulo = Circulo(5)
print(f"Área del círculo: {mi_circulo.area()}")  # Salida: Área del círculo: 78.54