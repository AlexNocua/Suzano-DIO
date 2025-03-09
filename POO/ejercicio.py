# class Recipes:
#     def __new__(cls: type[Self])->Self:
#         pass
#     def __init__(self)->None:
#         pass

class MyFirstClass:
    print ("who wrote this?")
    index = "Author-Book"

    def hand_list(self,philosopher,book):
        print(MyFirstClass.index)
        print(f"{philosopher} wrote the book: {book}")
    
_class = MyFirstClass()
_class.hand_list("Alex","Republic of  America")