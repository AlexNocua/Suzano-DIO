
"""_summary_
    En Python, el MRO se basa en el algoritmo C3 Linearization, que define el orden en el que se buscan los métodos en una jerarquía de clases.
 """
class A:
    def saludar(self):
        print("Saludo desde A")

class B(A):
    def saludar(self):
        print("Saludo desde B")

class C(A):
    def saludar(self):
        print("Saludo desde C")

class D(B, C):
    pass

# Crear una instancia de D
objeto = D()

# Llamar al método saludar
objeto.saludar()

"""
Explicación del MRO:
Jerarquía de clases:

D hereda de B y C.

B y C heredan de A.

Orden de resolución (MRO):

Cuando llamas a objeto.saludar(), Python sigue el MRO para determinar qué método ejecutar.

El MRO de la clase D se puede verificar con D.__mro__ o D.mro():

python
Copy
print(D.__mro__)
Esto devolverá:

Copy
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
Resultado:

Python busca el método saludar en D. Como no está definido, sigue el MRO y lo busca en B.

En B, encuentra el método saludar, lo ejecuta y muestra:

Copy
Saludo desde B
¿Qué pasa si eliminamos el método saludar de B?
Si eliminamos el método saludar de B, Python seguirá el MRO y buscará en C:

python
Copy
class B(A):
    pass  # Eliminamos el método saludar

objeto = D()
objeto.saludar()  # Ahora se ejecuta el método de C
Salida:

Copy
Saludo desde C
"""