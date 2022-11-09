from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
class child(parent):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)

ob=child(5,8)
ob.add()
ob.sub()
