# metodos de instancia
class PaysLists:
    def __init__(self,name, payment, amount)->None:
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment = "yes"    
    
    def status(self):
        if self.payment == "yes":
            return f"{self.name} is paid {str(self.amount)}"
        else:
            return f"{self.name} is not paid yet"
        
alex = PaysLists("Alex","no", 1000)
eduardo = PaysLists("Alex","yes", 1000)
    
print(alex.status()+ "\n" + eduardo.status())