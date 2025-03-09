# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod


class Bank(ABC):
    
    def basicinfo (self)->str:
        print("This is a generic bank")
        # return "Generic Bank : 0"
    
    @abstractmethod
    def withdraw(self,amount):
        pass
    
    
class Swiss(Bank):
    def  __init__(self) -> None:
        super().__init__()
        self.bal=1000
    
    def basicinfo (self)->str:
        print("This is a Swiss bank")
        # return f"Swiss Bank: {self.bal}"
    
    def withdraw(self,amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        else:
            self.bal -= amount
            print(f"Withdrawn amount: {self.bal}")
            print(f"New balance: {self.bal}")
            return self.bal
    

# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()