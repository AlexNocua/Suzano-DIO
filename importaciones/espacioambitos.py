animal = "Dog" #variable global

def a():
    animal = "Cat" #variable local
    print("Inside a() before calling b():", animal)
    def b():
        nonlocal animal #variable no local
        animal = "Rabbit"
        print("Inside b():", animal)
    b()
print("Before calling a():", animal)
a()
