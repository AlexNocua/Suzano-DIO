# El siguiente codigo va a dar a conocer algunas funciones integradas para saber la relacion entre idferetes clases

class A:
    a =1
    
class B(A):
    a =1
    
    
class C(B):
    a =1
    
print(issubclass(A,B))#Da a entender si la clase A es subclase de B